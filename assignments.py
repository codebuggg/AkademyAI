#number of seconds in a week

#60 seconds makes a minute
minute = 60
#60 minutes make an hour
hour = 60*minute
#24 hours make a day
day = 24* hour
#7 days make a week
week = 7 * day
print(week )

#exercise 1.1
cover_price = 24.95
bookstore = cover_price - (0.40 * cover_price)
copies = 60
shipping = 0
if (copies == 1) :
        shipping = 3
else :
        shipping = shipping + (copies-1)*0.75
wholesaleCost = (copies*bookstore) + shipping
print(wholesaleCost)

#exercise 1.2
#runtime errors
cover_price = 24.95
bookstore = cover_price - (0.40 * cover_price)
copies = 60
shipping = 0
if (copies == 1) :
        shipping = 3
else :
        shipping = shipping + (copies-1)*0.75
wholesaleCost = (copies*bookstore) + shipping #+ discount #discount has not been defined
print(wholesaleCost)

#exercise 1.3
current_time = 14.00
alarm = current_time + 535
alarm_time = alarm%24
print(float(alarm_time))

#excercise 2.1
var1 = 2  #this is the first variable
var2 = 6 #this is the second variable
var3 = 5
average = (var1 + var2 + var3)/3 #this computes the average of the three variables

a = 7
c = "hello"
print(a,c)

x = 7
if x < 10:
    print("This line is only executed if x < 10.")
    print("And the same holds for this line.")
print("This line, however, is always executed.")

x = 11
if x < 10:
    print("This line is only executed if x < 10.")
    print("And the same holds for this line.")
print("This line, however, is always executed.")

def print_status(x):
    if x == 5: 
        print("x equals 5")
    if x > 4: 
        print("x is greater than 4")
    if  x >= 5:
        print("x is greater than or equal to 5")
    if x < 6: 
        print("x is less than 6") 
    if x <= 5:
        print("x is less than or equal to 5")
    if x != 6 :
        print("x does not equal 6")
        
print(print_status(9))


#function isOdd

def isOdd(x):
        if x % 2 == 0:
                print(x, "is an even number")
        else:
                print(x, "is an odd number")

isOdd(12)

#weight function
# Write a function that takes a parameter weight. If weight is greater than 20 (kilo's), 
#print: "There is a $25 surcharge for luggage that is too heavy." If weight is smaller than 20, 
#print: "Thank you for your business." If weight is exactly 20, 
#print: "Pfew! The weight is just right!". Test the function for different values of weightto make sure your code works.

def weight(x):
	if x > 20:
		print("There is a $25 surcharge for luggage that is too heavy")
	elif x < 20:
		print("Thank You for your business")
	else x == 20:
		print("Pfew! The weight is just right!")

weight(35)


