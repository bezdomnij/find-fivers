from pathlib import Path
import argparse
from findfivers.custom_argparse import ArgsNamespace
import pandas as pd

OUTPUT = "findfivers/data/result3.csv"


def write_result(result) -> None:
    """
    makes a dataframe from the result-set and writes it to a csv file
    :param result: a set of selected words
    :return: None / side effect: new csv file
    """
    df = pd.DataFrame(list(result), columns=['the_word'], index=None)
    df.to_csv(OUTPUT, sep=',', index=False)


def find_length(cliargs):
    """
    find words of specific length in the input file
    :param cliargs: a Namespace object with source filename and word-length arguments
    :return: a set of words of specified length
    """
    file = Path(cliargs.filename)
    result = set()
    with open(file, "r") as f:
        for line in f.readlines():
            one_line = [ln for ln in line.split(sep=" ") if len(ln) > 2]
            no_break = [w.strip() for w in one_line]
            fivers = {w.lower() for w in no_break if len(w) == cliargs.length and w.isalpha()}
            result.update(fivers)
    return result


def parse_cli_args() -> ArgsNamespace:
    """
    parses cli arguments
    :return: a custom Namespace object with parsed arguments
    """
    nsp = ArgsNamespace()
    parser = argparse.ArgumentParser(
        prog="findfivers",
        description="find five-letter words in text, or other as parameter given")
    parser.add_argument("filename", help="the path to the file that contains the words "
                                         "where we find the five(or 'x')-letter long words",
                        default="magyar-szavak.txt", nargs="?", type=str)
    parser.add_argument("-l", "--length", help="the number of characters in the word",
                        default=5, nargs="?", type=int)
    return parser.parse_args(namespace=nsp)


def main():
    args: ArgsNamespace = parse_cli_args()
    words: set = find_length(args)
    write_result(words)


if __name__ == '__main__':
    main()
