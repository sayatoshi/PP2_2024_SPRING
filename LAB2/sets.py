fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)       #use update to add new list in previous in random order(only unical)

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")   #in this sample same with "remove"
print(fruits)
