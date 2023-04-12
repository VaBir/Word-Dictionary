from PyDictionary import PyDictionary
print ('WELCOME TO WORD DICTIONARY!')
dictionary = PyDictionary()


while True:  
  
  word = input('Enter your word: ')
  if word == '':
    break
  print(dictionary.meaning(word))

