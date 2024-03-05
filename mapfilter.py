# A List
my_list = [
    {"first_name": "Alex", "last_name": "Merced", "age": 37},
    {"first_name": "Tony", "last_name": "Merced", "age": 35}
    ]

# The long way

new_list = []

for person in my_list:
    new_list.append({
        "name": person["first_name"] + " " + person["last_name"],
        "age": person["age"] 
        })
    
print(new_list)

# Easier way ~ shorterish

def rebuildItem(person):
    return {
        "name": person["first_name"] + " " + person["last_name"],
        "age": person["age"] 
        }
new_list = list(map(rebuildItem, my_list))

print(new_list)
# <map object at 0x102cc6320> received this map object ~ added typle or list

# shortest way

new_list = list(map(
    lambda person:{"name": person["first_name"] + " " + person["last_name"], 
            "age": person["age"] }
            , my_list))

print(new_list)

# lambda parameters:returnvalue
# lambda x,y: x+y

# filter

# Tony isn't in this list, we want greater than 35
new_list = list(filter(lambda person:person["age"] > 35, my_list))

print(new_list)