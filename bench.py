import cProfile
from triereg import *

with open("benchmark_article.txt", "r", encoding="utf8") as f:
    text = f.read()
with open("words.txt", "r", encoding="utf8") as f:
    words = f.read().strip().split("\n")


def normal_reg_from_words(words):
    words = [re.escape(x) for x in words]
    p = "|".join(words)
    return re.compile(p, re.IGNORECASE)


p1 = normal_reg_from_words(words)
p2 = trie_regex_from_words(words)


def normal_reg_search():
    for i in range(1000):
        p1.findall(text)


def trie_reg_search():
    for i in range(1000):
        p2.findall(text)


if __name__ == '__main__':
    cProfile.run("normal_reg_search()")
    cProfile.run("trie_reg_search()")
