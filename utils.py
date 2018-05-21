import codecs


def read_files(file_list):
    data_list = []
    for file in file_list:
        with codecs.open(file, encoding='latin-1') as input_file_a:
            word_set = set()
            for line in input_file_a:
                line = line.strip().split()
                word_set.update(line)
        data_list.append(word_set)

    return data_list


def task_format_print(files, plagiarism_table):
    for i, file in enumerate(files):
        top_plagiarism_score = max(plagiarism_table[i])
        print(file.name, "- plagiarism of", files[plagiarism_table[i].index(top_plagiarism_score)].name, "with",
              top_plagiarism_score, "%")
