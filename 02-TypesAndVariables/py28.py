a = int(input("write your height"))
b = int(input("write your weight"))

bmiindex = b/(a*a)

print(bmiindex)

if bmiindex >= 0.00185 and bmiindex <=0.0025 :
    print("your bmi is ok")
else :
    print("your bmi is not ok")