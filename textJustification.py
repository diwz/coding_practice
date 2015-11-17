# Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
# For the last line of text, it should be left justified and no extra space is inserted between words.

# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.

# Return the formatted lines as:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Note: Each word is guaranteed not to exceed L in length.


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def process(curLine, curLineSumLen, maxWidth, lastLine=False):
            size = len(curLine)
            if lastLine:
                endSpace = maxWidth - curLineSumLen - (size - 1)
                for i in range(size-1):
                    curLine[i] = curLine[i] + " "
                curLine[-1] = curLine[-1] + " " * endSpace
            elif size == 1:
                return curLine[0] + " " * (maxWidth - curLineSumLen)
            else:
                spaceNum = (maxWidth - curLineSumLen) // (size - 1)
                remainder = maxWidth - curLineSumLen - spaceNum * (size - 1)
                for i in range(size-1):
                    curLine[i] = curLine[i] + " " * spaceNum
                for i in range(remainder):
                    curLine[i] = curLine[i] + " "
            return "".join(curLine)

        curLineSumLen = 0
        textFormat = []
        curLine = []
        for i in range(len(words)):
            word = words[i]
            if curLineSumLen + len(word) + len(curLine) <= maxWidth:
                curLine.append(word)
                curLineSumLen += len(word)
            else:
                textFormat.append(process(curLine, curLineSumLen, maxWidth))
                curLine = [word]
                curLineSumLen = len(word)

        textFormat.append(process(curLine, curLineSumLen, maxWidth, True))
        return textFormat
