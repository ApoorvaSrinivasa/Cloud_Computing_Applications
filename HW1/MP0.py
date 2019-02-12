import string
import random
import sys
stopWordsList = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
            "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
            "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
            "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
            "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
            "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
            "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", '']
def getIndexes(seed):
    random.seed(seed)
    n = 10000
    number_of_lines = 50000
    ret = []
    for i in range(0,n):
        ret.append(random.randint(0, 50000-1))
    return ret

translation_table = string.maketrans(string.uppercase,
                                     string.lowercase)
def split_mult(text, delimiters):
    L = []
    S = []
    for c in delimiters:
        S.append(c)
    S = set(S)
    res = ''
    for ch in text:
        if ch in S:
            L.append(res)
            res = ''
        else:
            res += ch
    return L


def get_words_from_line_list(text, delimiters):
    text = text.translate(translation_table)
    word_list = split_mult(text, delimiters)
    return word_list

def count_frequency(word_list):
    D = {}
    for new_word in word_list:
        if new_word in stopWordsList:
            continue
        if new_word in D:
            D[new_word] = D[new_word]+1
        else:
            D[new_word] = 1
    return D

def word_frequencies_for_file(delimiters, seed):
    line_list = []
    for line in sys.stdin:
        line_list.append(line)
    indexes = getIndexes(seed)
    L = []
    for i in indexes:
        L.append(line_list[i])
    res = ''
    for line in L:
        res += line
        res += '\n'
    word_list = get_words_from_line_list(res, delimiters)
    freq_mapping = count_frequency(word_list)

    return freq_mapping

delimiters = ' \t,;.?!-:@[](){}_*/\n\r'
seed = sys.argv[1]
D = word_frequencies_for_file(delimiters, seed)
L = []
for k, v in D.iteritems():
    L.append((v, k))
Ls = sorted(L, key=lambda x: (x[0]*-1, x[1]))
Lsm = [x[1] for x in Ls]
for i in range(20):
    print Lsm[i]
