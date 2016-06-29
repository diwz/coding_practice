class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.map = dict()
        for str in dictionary:
            abbr = self.abbreviateWord(str)
            if abbr in self.map:
                if self.map[abbr] != str:
                    self.map[abbr] = ""
            else:
                self.map[abbr] = str

    def abbreviateWord(self, word):
        if len(word) <= 2:
            return word
        return word[0] + str(len(word)-2) + word[-1]
    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr = self.abbreviateWord(word)
        return (abbr not in self.map) or (self.map[abbr] == word)


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
