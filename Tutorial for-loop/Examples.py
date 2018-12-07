#Here are some examples!
#You may look at the code and run the program to see how it is executed

#First I will show you how to print everything in the array.

favoritecars = ['350z', 'Acura TL', 'Mercedes e63', 
'Infiniti', 'Gsxr', 'Corvette']

for car in favoritecars:
    print(car)
    
#As you can see this listed out the cars as if it was a ordered list
print('')

#Now lets say we wanted to print out the letters of a specific car
for letters in favoritecars[1]:
    print(letters)
    
#Amazing! Noticed I used [1] at the end of favorite cars.
#This is considered the second spot of an array because it starts at 0 instead of 1
print('')

#This is the very basics of a for-loop and as you learn you will realize how much it is helpful!

#I will show you more for-loops for you to experiment with and see how it is executed
numbers = [[1, 2, 3, 4, 5],
           [1, 2, 3, 4, 5],
           [1, 2, 3, 4, 5]]

print([sum(x) for x in zip(*numbers)])

#This is using addition of mutliple collumns
print('')


