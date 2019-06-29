class SpellChecker:

    def print_first_word(self):
        print(self.dictionary.pop(1))

    def __init__(self, path_to_dictionary):
        with open(path_to_dictionary) as text:
            lines = text.readlines()
            self.dictionary = [word.strip('\n\r') for word in lines]
            self.print_first_word

