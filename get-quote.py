# Open quotes.txt with access mode 'a'
file_object = open('quotes.txt', 'a')

# Append 'This quote is better than the last quote' at the end of the file
file_object.write('\n')
file_object.write('This quote is better than the last quote')

# Close quotes.txt
file_object.close()

import random
def primary():
  #print("Keep it logically awesome dude.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd = random.randint(0, last)
  print(quotes[rnd], end = "")
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  primary()
