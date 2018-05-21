from LSH import LSH
from pathlib import Path
from utils import read_files, task_format_print


def main():
    root = Path("corpus-20090418")
    files = list(root.iterdir())

    lsh = LSH(files, read_files(files))
    plagiarism_table = lsh.rough_jaccard_test()
    task_format_print(files, plagiarism_table)


if __name__ == "__main__":
    main()
