from LSH import LSH
from pathlib import Path
from utils import read_files, task_format_print


def main():
    root = Path("corpus-20090418")
    files = list(root.iterdir())
    # files = files[:2]

    lsh = LSH(read_files(files))
    # plagiarism_table = lsh.rough_jaccard_test()
    # task_format_print(files, plagiarism_table)

    # plagiarism_table_min_hash = lsh.min_hashing()
    # task_format_print(files, plagiarism_table_min_hash)

    plagiarism_table_min_hash = lsh.min_hashing(shingles_mode=True)
    task_format_print(files, plagiarism_table_min_hash)


if __name__ == "__main__":
    main()
