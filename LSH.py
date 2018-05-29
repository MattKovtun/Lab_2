from random import shuffle


class LSH:
    def __init__(self, data_list, desired_fingerprint_length=100, shingles_length=3):
        """
        Constructor
        :param data_list: 2d matrix (array of sets) n by m, where n - number of examples (documents)
        m - number of words in set
        :param desired_fingerprint_length:
        """
        self.data_list = data_list
        self.desired_fingerprint_length = desired_fingerprint_length
        self.shingles_length = shingles_length

    def rough_jaccard_test(self):
        return self._generate_plagiarism_table(self.data_list)

    def min_hashing(self, shingles_mode=False):
        all_words_dictionary = set()
        for word_set in self.data_list:
            all_words_dictionary = set.union(all_words_dictionary, word_set)

        min_hash_fingerprints = []
        permutation = list(all_words_dictionary)

        for i in range(self.desired_fingerprint_length):
            shuffle(permutation)
            min_hash_fingerprints.append(self._formhashes(permutation))

        min_hash_fingerprints_T = list(map(list, zip(*min_hash_fingerprints)))

        if not shingles_mode:
            return self._generate_plagiarism_table(min_hash_fingerprints_T)

        shingle_fingerprints = [[] for i in min_hash_fingerprints_T]
        for i, fingerprint in enumerate(min_hash_fingerprints_T):
            for j in range(0, len(fingerprint), 3):
                shingle = [str(min_hash) for min_hash in fingerprint[j:min(j + 3, len(fingerprint))]]
                shingle_fingerprints[i].append("".join(shingle))

        return self._generate_plagiarism_table(shingle_fingerprints)

    def _formhashes(self, word_permutation):
        """
        Function which generates min hashes
        :param word_permutation: word order for specific minhashing
        :return:
        """
        hashlayer = [float('inf') for i in range(len(self.data_list))]
        for index, word in enumerate(word_permutation):
            for j, word_set in enumerate(self.data_list):
                if word in word_set:
                    hashlayer[j] = min(index, hashlayer[j])
        return hashlayer

    def _generate_plagiarism_table(self, data_list):
        """
        Function which generates plagiarism table
        :param data_list: 2d matrix n by m, where n is a number of samples and m is a number of jaccard features
        :return: 2d matrix where a[i][j] is plagiarism % between ith and jth document
        """
        resulting_table = [[-1 for i in range(len(data_list))] for j in range(len(data_list))]
        for i, file_word_set_a in enumerate(data_list):
            for j, file_word_set_b in enumerate(data_list):
                if i == j: continue
                resulting_table[i][j] = LSH.jaccard(file_word_set_a, file_word_set_b)
        return resulting_table

    @staticmethod
    def jaccard(set_a, set_b):
        """
        Function which accepts two sets or two lists and calculates jaccard
        distance between them
        :param set_a:  list or set
        :param set_b:  list or set
        :return:
        """
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
    assert (0.84 > LSH.jaccard([2, 1, 1, 2, 1, 1], [2, 1, 1, 1, 1, 1]) > 0.83)
    assert (LSH.jaccard({"a", "b", "c", "d", "e", "f", "g"}, {"a", "b", "c", "d", "e", "f", "h"}) == 0.75)
    assert (0.17 > LSH.jaccard([0, 8, 0, 3, 0, 4], [1, 0, 0, 0, 11, 0]) > 0.16)
