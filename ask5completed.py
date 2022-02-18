import re
from collections import Counter

input_file = input("Please enter ASCII file")
f = open(input_file, "r+")
lines= f.read()
f.close()

#TEXT WITH LOWER LETTERS AND SPACES ONLY
lines = re.sub(r'[^a-zA-Z," ",]','', lines)
lines = re.sub(r'\n', '', lines)
lines = re.sub(r'[^\w\s]', '', lines)
lines = re.sub(' +', ' ',lines)
new_file = lines.lower().split(" ")

# 10 MOST POPULAR WORDS
word_counter = {}
for word in new_file:
   if word in word_counter:
      word_counter[word] += 1
   else:
       word_counter[word] = 1
popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
top_10 = popular_words[:10] 
print("10 MOST POPULAR WORDS :" , top_10)

# 2 MOST COMMON INITIAL LETTERS
first2 =[]
for i in range(len(new_file)):
    if len(new_file[i]) > 1:
        first2.append(new_file[i][0:2])
common2 = Counter(first2).most_common(3)
print("2 MOST COMMON INITIAL LETTERS : ",common2)

# 3 MOST COMMON INITIAL LETTERS
first3 = []
for i in range(len(new_file)):
    if len(new_file[i]) > 2 :
        first3.append(new_file[i][:3])
common3 = Counter(first3).most_common(3)
print ("3 MOST COMMON INITIAL LETTERS : ",common3)
