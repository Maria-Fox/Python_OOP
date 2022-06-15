"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    ''' add the class summary here ''' 

# read file
# makes an attribute of a list of words (one per line)
# prints out "[number of words read] words read"

# includes random() method - returns randon word from that list- reading the already-read-in list of words

# def __init__(self, path):
#     dict_file = open(path)

    def __init__ (self, file_path):
    '''Opens file/path to read mode. Initializes a list of words read in file and returns a statement with a count of letter read. '''
        chosen_file = open(file_path)

        self.words = self.parse(chosen_file)

        print(f"{len(self.words)} words read")

    def __repr__ (self):
        '''Show representation'''

        return f"<WordFinder uses the file submitted and returns a random word chosen from the file.>"

    def parse(self, chosen_file):
        '''Parse chosen_file, converts to a list of words'''

        import random
        for word in chosen_file:
            word.strip()
        return [word]

        # return [word.strip()for word in chosen_file]


    def random(self):
        '''Returns a random word from word list'''

        return random.choice(self.words)
        # returns ran element from non-empty sequence

class SpecialWordFinder:
    ''' Class uses WordFinder and improces upon functionality by ensuring the return value is not either an empty line or a comment line'''

    def parse(self,chosen_file):
        '''Parse chosen_file into a list of words, skipping blanks and comments'''

        # for word in chosen_file:
        #     if word.strip() and not word.startswith("#")
        #     return word.strip()

    return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
    



