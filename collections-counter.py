from collections import Counter
import re

word_finder = re.compile("[\w']+")

#
# Find the frequency of words in Pride & Prejudice
#
text = open("pride-and-prejudice.txt").read()
words = word_finder.finditer(text)
word_counter = Counter(w.group(0).lower() for w in words)

print "bennet:", word_counter['bennet']
print "gutenberg:", word_counter['gutenberg']

#
# Disregard words from the preamble & postamble
#
boilerplate_counter = Counter()
boilerplate_counter.update
words = word_finder.finditer(open("preamble.txt").read())
boilerplate_counter.update(w.group(0).lower() for w in words)
words = word_finder.finditer(open("postamble.txt").read())
boilerplate_counter.update(w.group(0).lower() for w in words)

word_counter.subtract(boilerplate_counter)
print "bennet:", word_counter['bennet']
print "gutenberg:", word_counter['gutenberg']
