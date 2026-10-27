#!/usr/bin/env bash
set -euo pipefail

INDUS_WEBSITE_COMMIT=2434249618b1e74de3f26d28b90dfde093c3dd94
CISI_MAYIG_COMMIT=ad2f1e218a34b8c33c57de0d6cb8d99272765bbb
CDLI_COMMIT=d66b12b065af39a57d640576b4c7e098db5dac7f

fetch_pinned() {
  local URL="$1"
  local DIR="$2"
  local COMMIT="$3"

  mkdir -p "$(dirname "$DIR")"

  if [ ! -d "$DIR" ]; then
    GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 "$URL" "$DIR"
  fi

  git -C "$DIR" fetch --depth 1 origin "$COMMIT"
  GIT_LFS_SKIP_SMUDGE=1 git -C "$DIR" checkout --detach "$COMMIT"

  local HEAD
  HEAD="$(git -C "$DIR" rev-parse HEAD)"
  if [ "$HEAD" != "$COMMIT" ]; then
    echo "error: $DIR HEAD is $HEAD, expected $COMMIT" >&2
    exit 1
  fi
  echo "$DIR: $COMMIT OK"
}

fetch_pinned https://github.com/yajnadevam/indus-website.git raw/indus/indus-website "$INDUS_WEBSITE_COMMIT"
fetch_pinned https://github.com/mayig/indus-valley-script-corpus.git raw/indus/cisi-mayig "$CISI_MAYIG_COMMIT"
fetch_pinned https://github.com/cdli-gh/data.git raw/cdli/data "$CDLI_COMMIT"

if ! git lfs version >/dev/null 2>&1; then
  echo "error: git lfs is required to download CDLI LFS files (git lfs version failed)" >&2
  exit 1
fi
git -C raw/cdli/data lfs pull

ATF=raw/cdli/data/cdliatf_unblocked.atf
CSV=raw/cdli/data/cdli_cat.csv
MIN=$((1024 * 1024))
for f in "$ATF" "$CSV"; do
  size=$(wc -c < "$f" | tr -d ' ')
  if [ "$size" -le "$MIN" ]; then
    echo "error: $f is only $size bytes (likely a Git LFS pointer stub); expected > 1 MB" >&2
    exit 1
  fi
  echo "$f: $size bytes"
done
