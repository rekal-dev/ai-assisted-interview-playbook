#!/usr/bin/env python3
"""The screenshots' Cracking the Safe example as runnable modeling code."""
import argparse


def de_bruijn(n, k):
    if n < 1 or not 1 <= k <= 10 or k ** n > 100_000:
        raise ValueError("Use n >= 1, 1 <= k <= 10, and k**n <= 100000")
    start = "0" * (n - 1)
    next_symbol = {}
    stack = [(start, None)]
    reverse_labels = []
    while stack:
        node, incoming = stack[-1]
        symbol = next_symbol.get(node, 0)
        if symbol < k:
            next_symbol[node] = symbol + 1
            label = str(symbol)
            edge = node + label
            target = edge[1:] if n > 1 else ""
            stack.append((target, label))
        else:
            stack.pop()
            if incoming is not None:
                reverse_labels.append(incoming)
    return start + "".join(reversed(reverse_labels))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=2)
    parser.add_argument("--k", type=int, default=2)
    args = parser.parse_args()
    sequence = de_bruijn(args.n, args.k)
    print("Graph nodes: length n-1 suffixes =", args.k ** (args.n - 1))
    print("Graph edges: length n passwords =", args.k ** args.n)
    print("Sequence:", sequence)
    print("Length:", len(sequence), "(minimum =", args.k ** args.n + args.n - 1, ")")
    print("Windows:", " ".join(sequence[i:i + args.n]
                              for i in range(len(sequence) - args.n + 1)))
