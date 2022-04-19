import os, random, sys

class Utility():
    def __init__(self):
        self.path = os.path.abspath("../../src/resources/")
        
    # reads the words file
    def readDictWords(self):
        try:
            words = open(self.path+"/words.txt", "r").read().split()
            return words
        except:
            print("Error:", sys.exc_info()[0], " in readDictWords, Utility module, occurred.".__str__())
            
    def readWordRankFile(self):
        try:
            words = open(self.path+"/wordRank.csv", "r").read().split()
            return words
        except:
            print("Error:", sys.exc_info()[0], " in readWordRankFile, Utility module, occurred.".__str__())
        
    # Create file with 5 letter words
    def createFiveLetterWordsFile(self):
        try:
            words = self.readDictWords()
            f = open(self.path+"/FiveLtterWord.txt", "w")
            for word in words:
                if len(word) == 5:
                    f.write(word)
                    f.write("\n")
            f.close()
        except:
            print("Error:", sys.exc_info()[0], " in createFiveLetterWordsFilemethod, Utility module, occurred.".__str__())
