class WordCounter:

    def __init__(self, sentence):
        self.sentence = sentence
    
    def count_words(self):
        self.count = len(self.sentence.split())
    
    def get_word_count(self):
        return self.count

    def get_shortest_word(self):
        words = self.sentence.split()
        minLength = len(words[0])
        for eachWord in words:
            if len(eachWord) < minLength:
                minLength = len(eachWord)
        return minLength
    
    def get_longest_word(self):
        words = self.sentence.split()
        maxLength = len(words[0])
        for eachWords in words:
            if len(eachWords) > maxLength:
                maxLength = len(eachWords)
        return maxLength

    # def get_shortest_word(self):
    #     words = self.sentence.split()
    #     return min(len(eachWord) for eachWord in words)
    
    # def get_longest_word(self):
    #      words = self.sentence.split()
    #      return max(len(eachWord) for eachWord in words)

        



        