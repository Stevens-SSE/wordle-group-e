import os
from csv import reader

# used for implementing linked list


class Node:
    def __init__(self, data: any = None) -> None:
        self.data = data
        self.next_value = None

# to create helper functions for automation of game


class Helper:

    def __init__(self):
        self.words = []

# extracts words from wordRank.csv to save into list of words
    def file_wordRank(self):
        src_file = 'wordRank.csv'
        src_dir = os.getcwd()
        src_file_location = os.path.join(src_dir, src_file)
        self.words = []
        try:
            with open(src_file_location, 'r') as f:
                r = reader(f)
                # print(r)
                list_of_rows = list(r)
                self.words.append(list_of_rows)
                self.words = [word[1] for word in list_of_rows]
                return self.words
        except Exception as e:
            # self.write_logs(f"ERROR : File Error {e}",True)
            print(e)
            return []

# generates good, bad and correct words based on previous chosen words
    def good_bad_correct_generate(self, wordle, word, stmt):
        good = []
        bad = []
        correct = ''
        wordle_set = set(wordle)
        word_set = set(word)
        good = list(word_set & wordle_set)
        bad = list(wordle_set - word_set)

        for i in range(len(stmt)):
            if stmt[i] == '`' or stmt[i] == '"':
                continue
            elif i+1 < len(stmt) and (stmt[i+1] == '`' or stmt[i+1] == '"'):
                correct += '_'
            else:
                correct += stmt[i]
        return good, bad, correct

# implementation of actusl logic to play wordle automatically based on previous inputs
    def possible_words(self, good, bad, correct, prev) -> list:

        for letter in bad:
            if letter in good:
                bad = list(filter(lambda i: i not in good, bad))
        self.file_wordRank()
        if (good == None or len(good) == 0) and (bad == None or len(bad) == 0) and (correct == None or len(correct) == 0):
            return self.words[:50]
        else:
            output = []
            for word in self.words:
                if word in prev:
                    continue
                if any(item in word for item in bad):
                    continue
                if not all(elem in word for elem in good):
                    continue
                f = True
                for idx, letter in enumerate(correct):
                    if letter == '_':
                        continue
                    if word[idx] != letter:
                        f = False
                        break
                if f:
                    output.append(word)
            return output
