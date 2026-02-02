# Sets

ourset = {"Toyota", "Hyundai", "Lexus", "Tesla", "Changhan"}

ourset.add("Subaru")

print(ourset)

ourset.add("Toyota")
ourset.add("Chevrolet")

print(ourset)

ourset.remove("Tesla") # KeyError if value does not exist

print(ourset)