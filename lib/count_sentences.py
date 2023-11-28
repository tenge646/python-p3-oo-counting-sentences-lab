#!/usr/bin/env python3
class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            print("The value must be a string.")
            self.value = ""
        else:
            self.value = value
    def is_sentence(self):
        return self.value.endswith('.') if self.value else False

    def is_question(self):
        return self.value.endswith('?') if self.value else False

    def is_exclamation(self):
        return self.value.endswith('!') if self.value else False

    def count_sentences(self):
        if not self.value:
            return 0

        sentences = filter(None, self.value.split('.'))
        sentences = filter(None, sum((sentence.split('!') for sentence in sentences), []))
        sentences = filter(None, sum((sentence.split('?') for sentence in sentences), []))

        return sum(1 for _ in sentences)
