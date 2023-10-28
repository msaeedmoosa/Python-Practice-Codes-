myDict = {
    "pankha": "Fan",
    "dabba": "Box",
    "vastu": "Item",    
}
a = input("Enter the hindi word\n")
# print("The meaning of your word is:", myDict[a])


# below line will not throw an error if the key is not preset in the dictionary
print("the meaning of your word is: ",  myDict.get(a))