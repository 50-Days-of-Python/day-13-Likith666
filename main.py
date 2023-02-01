#Write your code here.
try:
  price = int(input())
  VAT = int(input())
  print(round(price+(price*VAT)/100))
except:
  print("Invalid Input")
