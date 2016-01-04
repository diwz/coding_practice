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
        def process(cur_line, cur_line_total_len, maxWidth, lastLine=False):
            word_cnt = len(cur_line)
            space_cnt = word_cnt - 1
            if lastLine:
                endSpace = maxWidth - cur_line_total_len - space_cnt
                for i in range(space_cnt):
                    cur_line[i] = cur_line[i] + " "
                cur_line[-1] = cur_line[-1] + " " * endSpace
            elif word_cnt == 1:
                return cur_line[0] + " " * (maxWidth - cur_line_total_len)
            else:
                spaceNum = (maxWidth - cur_line_total_len) // space_cnt
                remainder = maxWidth - cur_line_total_len - spaceNum * space_cnt
                for i in range(space_cnt):
                    cur_line[i] = cur_line[i] + " " * spaceNum
                for i in range(remainder):
                    cur_line[i] = cur_line[i] + " "
            return "".join(cur_line)


        cur_line_total_len = 0
        res = []
        cur_line = []
        for i in range(len(words)):
            word = words[i]
            if cur_line_total_len + len(word) + len(cur_line) <= maxWidth:
                cur_line.append(word)
                cur_line_total_len += len(word)
            else:
                res.append(process(cur_line, cur_line_total_len, maxWidth))
                cur_line = [word]
                cur_line_total_len = len(word)

        # Last line
        res.append(process(cur_line, cur_line_total_len, maxWidth, True))
        return res
