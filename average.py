#Program average: a program to average a specified set of numbers.
#
number_of_numbers = int (input ('How many numbers do you want me to average?'))
total = 0
#
#this part totals the numbers.
#
for i in range (1, number_of_numbers + 1):
  print ('Number', i)
  number = float (input ('Enter number.'))
  total = total + number
#
#the last bit gets the average.
#
print ('Average is', total / number_of_numbers)
  
