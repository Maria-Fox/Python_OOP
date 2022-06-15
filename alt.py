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
        self.file_path = open(file_path)

        for words in self.file:
        print(words)
        word_list = list(words)
        print("this is the word list", word_list)
        print("len(word_list) 'words read'")


    def random(self):
    '''Returns a random word from the word list'''

        import random 
        n = random.randint(0,len(word_list))
        final_word = word_list[n]
    return final_word.replace("/n", "")

# Double- check: Is this re-reading the entire list of words each time? Or just the alread-read-in list of words? 

class SpecialWordFinder:
    ''' Class uses WordFinder and improces upon functionality by ensuring the return value is not either an empty line or a comment line'''

    def __init__(self, file_path):
        super().__init__(file_path)

    for words in self.file:
        if word in self.file == type(str) and if "#" not in str:
            # the rest would be the same as the parent init. Does anything else need to be added?
        print("len(word_list) 'words read'") 

        # Because we used super we should have access to methods from the parent class. Correct? Nothing else needs to happen here. For example- random()
