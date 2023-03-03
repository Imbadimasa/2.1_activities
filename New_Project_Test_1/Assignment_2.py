# 1.
x = 5
y = 10
if 2 * x > 10:
    print("Question 1 works!")
else:
    print("Oooo needs some work")
    
#Oooo needs some work

# 2.
x = 5
y = 10
if len("Dog") < x: #3 < x
    print("Question 2 works!")
else:
    print("Still missing out")
    
#Question 2 works!

# 3.
age = 19
if age > 18:
    print("You are of drinking age!")
else:
    print("Argggggh! You think you can hoodwink me, matey?! You're too young to drink!")
    
#You are of drinking age!

# 4.
x = 2
y = 5
if (x ** 3 >= y) and (y ** 2 < 26): #** = ^ 2^3 = 8
    print("GOT QUESTION 4!")
else:
    print("Oh good you can count")
    
# GOT QUESTION 4!

# 5.
height = 66
age = 16
adult_permission = True

if (height > 70) and (age >= 18): #false
    print("Can ride all the roller coasters")
elif (height > 65) and (age >= 18): #false
    print("Can ride moderate roller coasters")
elif (height > 60) and (age >= 18): #false
    print("Can ride light roller coasters")
elif ((height > 50) and (age >= 18)) or ((adult_permission) and (height > 50)): #True
    print("Can ride bumper cars") #execute this line
else:
    print("Stick to lazy river")

    #Can ride bumper cars