fruits = ["apple", "banana", "cherry"]
print(fruits[1])    #use [1] to print second item in a given list


fruits = ["apple", "banana", "cherry"]
fruits[0]= "kiwi"
print(fruits)     #use append to replace first item in a given list

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)     #use append to add new item in a given list

fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")
print(fruits)   #use the insert method to add given as the second item in the fruits list

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")   
print(fruits)   #use remove to delete an item from list

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])   #use [-1] to print list in reverse order

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])  #use [2:5] to print from 3 for 5 items form list 

fruits = ["apple", "banana", "cherry"]
print(len(fruits))  #use len() to print length of a given list