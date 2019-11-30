cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
avg_passengers = passengers / cars_driven

print("There are", cars, " cars Available")
print("There are only", drivers, " drivers Available")
print("There will be a", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "passengers today")
print("we need to put out", avg_passengers, "in each car")
