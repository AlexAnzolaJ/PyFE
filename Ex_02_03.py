# Exercise 2.3: Write a program to prompt the user for hours and rate per hour to compute gross pay.

hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("Enter Rate:")
rate = float(rate)
pay = hrs * rate
print("Pay:", pay)