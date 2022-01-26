import urllib.request
from collections import defaultdict
from random import randrange


class WRDLR():
    def __init__(self):
        with urllib.request.urlopen('https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt') as response:
            words = response.read().decode('utf-8').splitlines()

        self.words_sets = defaultdict(lambda: defaultdict(set))
        self.max_hints = 5
        self.known = list()
        self.hints = list()
        self.filtered_words = set()

        for word in words:
            for i, letter in enumerate(word):
                self.words_sets[i][letter].add(word)
        
        self.words_sets['all'] = set(words)

    def getWord(self, result: list = None) -> str:
        words = self.getWords(result)
        return list(words)[randrange(len(words))]

    def getWords(self, result: list = None) -> set:
        if not len(self.filtered_words):
            self.filtered_words = set(self.words_sets['all'])

        self._setKnownAndHints(result)
        self._filterByKnown(self.filtered_words)
        self._filterByHints(self.filtered_words)

        return self.filtered_words

    def _setKnownAndHints(self, result: list):
        self.known = list()
        self.hints = list()

        for pos in result:
            if pos.endswith('?'):
                self.known.append(None)
                self.hints.append(pos[0])
            elif pos == '.':
                self.known.append(None)
                self.hints.append(None)
            else:
                self.known.append(pos)
                self.hints.append(None)
    
    def _filterByKnown(self, words: set):
        if len(self.known) != 5:
            raise ValueError('Known list must have 5 positions')

        for i, letter in enumerate(self.known):
            if letter != None:
                self.max_hints -= 1
                words.intersection_update(self.words_sets[i][letter])

    def _filterByHints(self, words: set):
        num_hints = len([hint for hint in self.hints if hint != None])
        if num_hints == 0:
            return
        elif num_hints > self.max_hints:
            raise ValueError('Cannot have more hints than remaining unknowns')

        possibles = set()
        for i, letter in enumerate(self.known):
            if letter == None:
                for j, hint in enumerate(self.hints):
                    if hint == None:
                        continue
                    if i == j:
                        self._removeWordsByLetter(words=words, letter=hint, pos=i)
                    else:
                        possibles.update(self.words_sets[i][hint])
        
        words.intersection_update(possibles)

    def _removeWordsByLetter(self, words: set, letter: str, pos: int):
        to_remove = set()
        for word in words:
            if word[pos] == letter:
                to_remove.add(word)
        words.difference_update(to_remove)


def main():
    wrdlr = WRDLR()
    round = 1
    while round < 7:
        result = input(f'Enter the result of round {round}: ')
        result = [pos.strip() for pos in result.split(',')]
        while len(result) != 5:
            result = input(f'You must enter a total of 5 letters, hints, or periods separated by commas.\nEnter the result of round {round}: ')
        print(f'Try "{wrdlr.getWord(result=result)}"')
        round += 1

if __name__ == '__main__':
    main()
