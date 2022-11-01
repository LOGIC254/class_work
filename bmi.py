def bmi():
    weight=int(input())
    height=int(input())
    v=height*height
    bmi1=weight/v
    if bmi1<18.5:
        return "Underweight"
    elif bmi>=18.5 and bmi1<=24.9:
        return "Normal Weight"
    elif bmi>25:
        return "Overweight"
    return bmi1
u=bmi()
print(u)