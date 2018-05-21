class LSH:




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
