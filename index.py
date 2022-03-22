number=input("Enter a number please: ")
sum=0
if number.isnumeric()==False:
  print("Warning! It is an invalid entry. Don't use non-numeric, float, or negative values!")
elif int(number) < 0:
    print("Warning! It is an invalid entry. Don't use non-numeric, float, or negative values!")
elif int(number) > 0:
  for i in range(len(number)):
    sum+=int(number[i])**len(number)
  if sum==int(number):
    print("{} is an Armstrong Number.".format(number))
  else:
    print("{} is not an Armstrong number.".format(number))
else:
  print("Warning! It is an invalid entry. Don't use non-numeric, float, or negative values!")
