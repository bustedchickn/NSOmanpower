def isPalindrome(text):
  textlist = []
  for letter in text:
    textlist.insert(letter, -1)
  newtext = textlist.join()
  return text == newtext
isPalindrome("racecar")