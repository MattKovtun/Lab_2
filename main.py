from LSH import LSH
from pathlib import Path


def read_files(file_list):
    data_list = []
    for file in file_list:
        with open(file, encoding='utf8') as input_file_a:
            word_set = set()
            for line in input_file_a:
                line = line.strip().split()
                word_set.update(line)
        data_list.append(word_set)

    return data_list


def rough_jaccard_test(file_list):
    data_list = read_files(file_list)
    resulting_table = [[-1 for i in range(len(file_list))] for j in range(len(file_list))]
    for i, file_word_set_a in enumerate(data_list):
        for j, file_word_set_b in enumerate(data_list):
            resulting_table[i][j] = LSH.jaccard(file_word_set_a, file_word_set_b)
    return resulting_table


if __name__ == "__main__":
    root = Path("corpus-20090418")
    task = "g0pA_taska.txt"

    files = root.iterdir()
    next(files)
    print(rough_jaccard_test([root / task, next(files)]))
