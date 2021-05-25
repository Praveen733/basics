thisdict={
    "brand":"Ford",
    "model":"Mustag",
    "year":1964,
    "year":2021
}
"""
print(thisdict["brand"])

#Duplicate values will overwrite existing values:
print(thisdict)
print(len(thisdict))

#The values in dictionary items can be of any data type
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

#get the values from dictionary
print(thisdict["model"])
print(thisdict.get("model"))

#The keys() method will return a list of all the keys in the dictionary
print(thisdict.keys())

#The values() method will return a list of all the values in the dictionary
print(thisdict.values())


#add values to the dict
thisdict["color"]="white"
print(thisdict)


#change the values of orginal list
thisdict["brand"]="swift"
print(thisdict)


#The items() method will return each item in a dictionary, as tuples in a list
print(thisdict.items())


if "model" in thisdict:
  print("yes")



#Update the "year" of the car by using the update() method
thisdict.update({"year":2020})
print(thisdict)



#The pop() method removes the item with the specified key name
thisdict.pop("model")
print(thisdict)


#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
thisdict.popitem()
print(thisdict)


#The del keyword removes the item with the specified key name
del thisdict["model"]
print(thisdict)


#The clear() method empties the dictionary:
print(thisdict.clear())



#Print all key names in the dictionary, one by one
for x in thisdict:
  print(x)


#You can also use the values() method to return values of a dictionary
for x in thisdict.values():
  print(x)



#Loop through both keys and values, by using the items() method
for x,y in thisdict.items():
  print(x,y)



"""
#A dictionary can contain dictionaries, this is called nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)