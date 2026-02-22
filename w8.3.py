dict={1:"blue",2:"black",3:"white",4:"grey",5:"peach"}
print("keys in dictionary: ",dict.keys())
print("values in dictionary: ",dict.values())
print("items in dictionary: ",dict.items())
dict.pop(1)
print("after pop(): ",dict)
for key in list(dict.keys()):
    if dict[key]=="grey":
        del dict[key]
print("after deletion: ",dict)