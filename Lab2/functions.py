def calculate_area(length, width):
    return length*width
print(f'Area: {calculate_area(12, 32)}')

def calculate_bmi(weight_kg, height_cm, round_to = 2):
    height_m = height_cm/100
    bmi = weight_kg/(height_m**2)
    return bmi

bmi = calculate_bmi(70, 170)
print(f'Your bmi is: {round(bmi, 2)}')

if(bmi>25):
    print("you are overweight")
elif bmi>18.5:
    print('You have a good weight')
else:
    print('You are underweight')