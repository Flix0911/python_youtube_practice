# List (array)
groceryList = ["eggs", "cheese", "cereal"]

# print(groceryList)
# print(groceryList[2]) # cereal

# this will pull each individual index. a=index[0] and etc
# a,b,c = groceryList
# print(a)
# print(b)
# print(c)

# METHODS!
# groceryList.append("milk") add to it
# groceryList.extend(["milk", "butter"]) add to it
# groceryList.pop(1) remove 
# print(groceryList)

# Learn about a Tuple (like a list but you can't change it)
# Why use it?: You don't want it to change. Benefits under the hood regarding speed
groceryList = ("eggs", "cereal")
# print(groceryList)
# print(groceryList[0])

# Set (can't change and can't have duplicates)
# Take a list and turn to a set to remove duplicates
groceryList = {"eggs", "cereal", "milk"}
print(groceryList)


endresult = list(set([1,2,3,3,3]))
print(endresult)

# Dictionary (key/value pair)
# Use to describe 1 single thing
groceryList = [
    {"name": "milk", "price": 37},
    {"name": "cheese", "price": 2},
    {"name": "cereal", "price": 3}
]
# print(item1["name"]) #will give you milk. Key is name and value is milk
for a,b in groceryList:
    # print(item["name"], item["price"])
    print(a,b)
    # print(item["name"])

a_dict = {"name": "milk", "price": 3.7}

print(a_dict.items())

for k,v in a_dict.items():
    print(k,v)