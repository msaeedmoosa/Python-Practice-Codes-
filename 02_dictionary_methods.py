myDict = {
    "fast": "in a quick manner",
    "Musa": "a coder",
    "Marks": [1, 3, 5],
    "anotherdict": {'Musa': 'he is psycho'},
    1:2
}


print(list(myDict.keys())) # print the keys of the of the dictionary
print(myDict.values())     # print the keys of the dictionary 
print(myDict.items())     # print the (keys, value) of all the content of the dictionary 
print(myDict)

updateDict = {
    "lavish": "friend",
    "divya": "friend",
    "shubham": "friend",
    "Musa": "A Dancer"
}

myDict.update(updateDict) # updates the dictionary by adding key value pairs from updatedict 
print(myDict)

print(myDict.get("Musa")) #prints value associated with  key "Musa"
print(myDict["Musa"])   #prints value associated with  key "Musa"

# the syntax between .fet and [ ] syntax in Dictionaries ?

print(myDict.get("Musa2")) # return none as Musa2 as it is not present in the dictionary
print(myDict["Musa2"])   # throws an error as Musa2 is not present in the dictionary

