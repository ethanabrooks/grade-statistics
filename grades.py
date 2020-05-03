#! /usr/bin/env python
import pandas as pd
import sys
import argparse
from pathlib import Path
import numpy as np


def main(grades_csv: Path, max_score: int, round_to: int):
    df = pd.read_csv(str(grades_csv))
    grades = df["Total Score"].dropna()

    def percentile(x):
        return (grades.values >= x).sum() / len(grades) * 100

    print(
        f"""\
Maximum Possible Score: {max_score}
Maximum Achieved Score: {grades.max()} ({(grades == grades.max()).sum()} student)
Median: {grades.median()} ({percentile(grades.median()).round(round_to)}%)
Mean: {grades.mean().round(round_to)} ({percentile(grades.mean()).round(round_to)}%)
Std. Dev.: {grades.std().round(round_to)}\
"""
    )


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--max-score", type=int)
    parser.add_argument("--grades-csv", type=Path)
    parser.add_argument("--round-to", type=int, default=2)
    main(**vars(parser.parse_args()))
