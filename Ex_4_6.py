def computepay(h, r):
    if h <= 40:
        pay = h * r
    else:
        pay = 40 * r + (h - 40) * r * 1.5
    return pay

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
pay = computepay(h, r)
print("Pay", pay) 
