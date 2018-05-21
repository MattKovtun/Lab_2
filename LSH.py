class LSH:
    def __init__(self, file_list, data_list):
        self.file_list = file_list
        self.data_list = data_list

    def rough_jaccard_test(self):
        resulting_table = [[-1 for i in range(len(self.file_list))] for j in range(len(self.file_list))]
        for i, file_word_set_a in enumerate(self.data_list):
            for j, file_word_set_b in enumerate(self.data_list):
                if i == j: continue
                resulting_table[i][j] = LSH.jaccard(file_word_set_a, file_word_set_b)
        return resulting_table

    @staticmethod
    def jaccard(set_a, set_b):
        assert ((type(set_a) == type(list()) == type(set_b)) or (type(set_a) == type(set_b) == type(set())))

        common_items = 0
        different_items = 0
        jacc_set = False
        if type(set_a) == type(set_b) == type(set()):
            jacc_set = True

        if jacc_set:
            set_inter = set.intersection(set_a, set_b)
            common_items = len(set_inter)
            different_items = len(set.union(set_a, set_b)) - common_items
        else:
            for i, item in enumerate(set_a):
                if set_b[i] == item:
                    common_items += 1
                else:
                    different_items += 1

        return common_items / (common_items + different_items)


if __name__ == "__main__":
    # print(jaccard({"a" ,"b", "c", "d", "e", "f", "g"}, {"a" ,"b", "c", "d", "e", "f", "h"}))
    assert (0.84 > LSH.jaccard([2, 1, 1, 2, 1, 1], [2, 1, 1, 1, 1, 1]) > 0.83)
    assert (LSH.jaccard({"a", "b", "c", "d", "e", "f", "g"}, {"a", "b", "c", "d", "e", "f", "h"}) == 0.75)
