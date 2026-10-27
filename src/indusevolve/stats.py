"""Corpus summary statistics."""

import math
from collections import Counter


def describe(records) -> dict:
    texts = len(records)
    all_signs: list[str] = []
    lengths: list[int] = []
    initials: list[str] = []
    finals: list[str] = []

    for rec in records:
        signs = rec.signs
        lengths.append(len(signs))
        all_signs.extend(signs)
        if len(signs) >= 2:
            initials.append(signs[0])
            finals.append(signs[-1])

    tokens = len(all_signs)
    counts = Counter(all_signs)
    sign_types = len(counts)
    hapax_types = sum(1 for c in counts.values() if c == 1)

    length_hist = dict(sorted(Counter(lengths).items()))
    mean_length = round(sum(lengths) / texts, 3) if texts else 0.0
    max_length = max(lengths) if lengths else 0

    if tokens:
        entropy = 0.0
        for c in counts.values():
            p = c / tokens
            entropy -= p * math.log2(p)
        unigram_entropy_bits = round(entropy, 3)
    else:
        unigram_entropy_bits = 0.0

    def top_n(counter: Counter, n: int) -> list[list]:
        return [[s, c] for s, c in counter.most_common(n)]

    return {
        "texts": texts,
        "tokens": tokens,
        "sign_types": sign_types,
        "hapax_types": hapax_types,
        "mean_length": mean_length,
        "max_length": max_length,
        "length_hist": {str(k): v for k, v in length_hist.items()},
        "unigram_entropy_bits": unigram_entropy_bits,
        "top_signs": top_n(counts, 10),
        "top_initial": top_n(Counter(initials), 5),
        "top_final": top_n(Counter(finals), 5),
    }
