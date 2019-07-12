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

