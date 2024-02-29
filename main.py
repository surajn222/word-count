# Code to count frequency of words in a file
# Path: word_count.py
import re
from collections import Counter

def count_words(file_path):
    with open(file_path, 'r') as file:
        words = re.findall(r'\w+', file.read().lower())
        return Counter(words)
    
print(count_words('file.txt'))
