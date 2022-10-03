'''


You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.

Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.

Note:

    The frequency of a letter x is the number of times it occurs in the string.
    You must remove exactly one letter and cannot chose to do nothing.

 

Example 1:                                 

Input: word = "abcc"
Output: true
Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.

Example 2:

Input: word = "aazz"
Output: false
Explanation: We must delete a character, so either the frequency of "a" is 1 and the frequency of "z" is 2, or vice versa. It is impossible to make all present letters have equal frequency.

 

Constraints:

    2 <= word.length <= 100
    word consists of lowercase English letters only.


'''


    def equalFrequency(self, word: str) -> bool:
        my_dict = {}
        if len(set(word))==1:
            return 1
        for ch in word:
            if ch in my_dict.keys():
                my_dict[ch] +=1
            else:
                my_dict[ch] = 1
        freq_sets = set(my_dict.values())
        freq_list = list(my_dict.values())
        if len(freq_sets) == 1 and freq_list[0]==1 :
            return 1
        if len(freq_sets) > 2 or len(freq_sets) == 1:
            return 0       

        freq_list.sort()
        m = min(freq_list)
        M = max(freq_list)
        n_Max = 0
        n_min = 0
        for freq in freq_list:
            if freq == m:
                n_min += 1
            elif freq == M:
                n_Max += 1

        if n_Max == 1 and M == (m + 1):
            return 1
        elif n_min == 1 and m == (M - 1):
            return 1
        else:
            return 0

        print("n_min", n_min)
        print("n_max", n_Max)
