#!/usr/bin/env python3

import argparse
import json

from lib.search_utils import (
    clean,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    with open("./data/movies.json", "r") as file:
        movieDB = json.load(file)

    match args.command:
        case "search":
            print(f"Searching for: {args.query}")
            matchingMovies = []
            for movie in movieDB["movies"]:
                if clean(args.query) in clean(movie["title"]):
                    matchingMovies.append(movie)
            for index, movie in enumerate(sorted(matchingMovies, key=lambda m: m["id"])[:5]):
                print(f'{index + 1}. {movie["title"]}')

        case _:
            parser.print_help()


if __name__ == "__main__":
    main()