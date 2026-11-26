root = input("Enter root word: ")
delete = input ("Delete: ")
add = input ("Add: ")

result = root
if delete != "":
    result = result[:-len(delete)]
result = result + add

print("-----Table-----")
print("Root: ", root)
print("delete: ", delete)
print("Add:  ", add)
print("Result: ", result)


#Example 2: (Add a Suffix)
#nput:
root = input("Enter root word: ")
suffix = input("Enter suffix to add: ")
new_word = root + suffix
print("\n------ Result ------")
print("Root Word :", root)
print("Suffix :", suffix)
print("New Word :", new_word)

#Example 3: (Delete the Last Characters)
#Input:
word = input("Enter word: ")
n = int(input("How many letters to delete? "))
root = word[:-n]
print("\n Original Word :", word)
print("Root Word
 :", root)

 #Example 7:( Morphological Analysis)
#Input:
word = input("Enter a word: ")
if word.endswith("ing"):
print("Delete :", "ing")
print("Add :", "-")
print("Root :", word[:-3])
elif word.endswith("ed"):
print("Delete :", "ed")
print("Add :", "-")
print("Root :", word[:-2])
elif word.endswith("s"):
print("Delete :", "s")
print("Add :", "-")
print("Root :", word[:-1])
else:
print("No rule found")

#Example 6:(Using a List of Suffixes)
#Input:
root = input("Enter root word: ")
suffixes = ["s", "ed", "ing", "er"]
for suffix in suffixes:
print(root + suffix)

#Example 5: (Check and Remove Prefix)
#Input:
word = input("Enter word: ")
if word.startswith("un"):
root = word[2:]
print("Prefix Removed :", root)
else:
print("No prefix found")

#Example 4: (Delete and Then Add)
#Input:
word = input("Enter word: ")
delete = int(input("Delete last how many letters? "))
add = input("Enter letters to add: ")
root = word[:-delete]
new_word = root + add
print("\nRoot Word :", root)
print("New Word :", new_word)