#write a program that determines whether a year entered by the user in a leap year or not using if_elief_else statement
def isLeapYear(Year):
  if (Year % 4 == 0 and Year % 100 != 0) or Year % 400 == 0 :
    return True
  else:
    return False

Year=int(input("Enter a year:")) 
        
if isLeapYear(year):
 print('{} is a LeapYear.'.format(Year)) 
else: 
  print('{} is not a leap year year. '. format(year)) 