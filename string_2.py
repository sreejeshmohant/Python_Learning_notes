print("Giraffe\nAccademy")   # \n  for new line

phrase = "Giraffe Academy"
print(phrase)

print(phrase + "is cool")   # concatination 

print(phrase.lower())   # lower case

print(phrase.upper())  # upper case

print(phrase.isupper())  # check if it is upper case or not and return a true or false value

print(phrase.islower()) # check if it is lower case of not and return a true or false value

print(phrase.upper().isupper()) # combination case will convert the string into Upper case and will retun a true value

print(len(phrase)) # how many characters are inside the string

print(phrase[0]) # to grab the first character of the string

print(phrase.index("d")) # will return the index of the character G in the string

print(phrase.index("Acad")) # Will retrun the starting index of the string we have given

# print(phrase.index("z")) # will throw an error if it is not present in the string

print(phrase.replace("Giraffe", "Elephant")) # to replace character or strings inside a string


