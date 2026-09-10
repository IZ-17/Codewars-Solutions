def bmi(weight, height):
    total = weight/ (height ** 2)
    if total <= 18.5: return "Underweight"
    elif total <= 25: return "Normal"
    elif total <= 30: return "Overweight"
    else: return "Obese"