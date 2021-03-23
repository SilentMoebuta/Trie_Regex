import re


class Trie:
    """
    change strings to a tree type regex pattern
    """
    def __init__(self):
        self.data = {}

    def add(self, word):
        ref = self.data
        for char in word:
            ref[char] = char in ref and ref[char] or {}  # char in ref: ref[char] else: {}
            ref = ref[char]
        ref[''] = 1

    def dump(self):
        return self.data

    def _pattern(self, pData):
        data = pData
        if "" in data and len(data.keys()) == 1:
            return None
        alt = []
        cc = []
        q = 0
        for char in sorted(data.keys()):
            if isinstance(data[char], dict):
                try:
                    recurse = self._pattern(data[char])
                    alt.append(re.escape(char)+recurse)
                except:
                    cc.append(re.escape(char))
            else:
                q = 1
        cconly = not len(alt) > 0

        if len(cc) > 0:
            if len(cc) == 1:
                alt.append(cc[0])
            else:
                alt.append('[' + ''.join(cc) + ']')

        if len(alt) == 1:
            result = alt[0]
        else:
            result = "(?:" + "|".join(alt) + ")"

        if q:
            if cconly:
                result += "?"
            else:
                result = "(?:%s)?" % result
        return result

    def pattern(self):
        return self._pattern(self.dump())


def trie_regex_from_words(words):
    trie = Trie()
    for w in words:
        trie.add(w)
    return re.compile(trie.pattern(), re.IGNORECASE)


if __name__ == '__main__':
    strs = ["123", "134"]
    print(trie_regex_from_words(strs))
