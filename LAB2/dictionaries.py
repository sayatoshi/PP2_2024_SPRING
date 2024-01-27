car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))  #use get to print "model" of car

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020        #changing year's value
print(car)

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]= "red"       #add car's value of color
print(car)


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")           #use "pop" to remove value in "car"
print(car)

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()          #use the clear method to empty the "car" dictionary.
print(car)
