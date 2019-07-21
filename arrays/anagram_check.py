###
# Problem
# Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters
# (so you can just rearrange the letters to get a different phrase or word).

# For example:

# "public relations" is an anagram of "crap built on lies."

# "clint eastwood" is an anagram of "old west action"

# Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".
####

def anagram_check(s1,s2):

  '''
  Input: two strings s1, s2
  Output: True: if s1 and s2 are anagrams
  '''

  # Remove any spaces between the characters
  # and convert to lower case
  s1 = s1.replace(' ','').lower()
  s2 = s2.replace(' ','').lower()

  # create a dictionary called "counter"
  counter = {}

  # Edge-case check
  if len(s1) != len(s2):
    return False

  # add each char in as keys to dictionary & its 
  # frequency as value (counting each char)
  for char in s1:
    if char in counter:
      counter[char] += 1
    else:
      counter[char] = 1

  # reduce the count of each char 
  # encountered from the dictionary "counter"
  for char in s2:
    if char in counter:
      counter[char] -= 1
    else:
      return False

  # Not an anagram if  each value!=0, 
  for char in counter:
    if counter[char] != 0:
      return False

  return True
  
