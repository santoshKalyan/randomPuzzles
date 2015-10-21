

import sys
"""

"""


""" a dictionary """
def wordCountList(filename):
 
  
  word_count = {}  
  input_file = open(filename, 'r')
  for line in input_file:
    words = line.split()
    for word in words:
      word = word.lower()
      if not word in word_count:
        word_count[word] = 1
      else:
        word_count[word] = word_count[word] + 1
  input_file.close()  
  return word_count



""" a fcuntion to print a word and count """

def printingWords(filename):
  
  word_count = wordCountList(filename)
  words = sorted(word_count.keys())
  
  for word in words:
    print word, word_count[word]


def getCount(word_count_tuple):
  return word_count_tuple[1]


""" function getting the top 10,20 etc. words """

def topWords(filename):
  
  word_count = wordCountList(filename)

  #sortingitems
  items = sorted(word_count.items(), key=getCount, reverse=True)

  # Print
  for item in items[:20]:
    print item[0], item[1]


def main():
  

  flag = sys.argv[1]
  filename = sys.argv[2]

  if flag == '--wordcount':
    printingWords(filename)
  
  elif flag == '--top':
    topWords(filename)
  
  else:
    print 'comeon ! look out for parameters buddy'  
    sys.exit(1)
  

if __name__ == '__main__':
  main()
