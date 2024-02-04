import requests
Word = input("Enter the word you want to search for: ")
url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+Word
meaning = requests.get(url).json()
Word_meaning = str(meaning[0]['meanings'][0]['definitions'][0]['definition'])
print(Word_meaning)
