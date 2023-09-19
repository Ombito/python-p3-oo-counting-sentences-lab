#!/usr/bin/env python3
import re
class MyString:
    def __init__(self, value = ""):
        if type(value) == str:
            self._value = value
        else: 
            print("The value must be a string.")

    def is_sentence(self):
        if self._value.endswith('.'):
            return True
        else:
            return False
    
    def is_question(self):
        if self._value.endswith('?'):
            return True
        else:
            return False
    
    def is_exclamation(self):
        if self._value.endswith('!'):
            return True
        else:
            return False

    def count_sentences(self):
        sentences = re.sub(r'[!?]', '.', self._value).split('.')
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)
    
string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.is_sentence()) 
print(string.is_question()) 
print(string.is_exclamation())  
print(string.count_sentences())