print("Welcome to BMI and Health Advisor")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter you weight(kg): "))
height = float(input("Enter your height(m): "))

bmi = round(weight / height**2, 2)
print(f"Name: {name}")
print(f"Age: {age}")
print(f"BMI: {bmi}")

if bmi < 18.5:
    print("You are underweight")
    print("""Focus on gradually increasing your intake of nutrient-dense foods
          and incorporating strength training to safely build healthy muscle mass.""")
elif bmi < 25:
    print("You have healthy weight!")
    print("""Maintain your current well-being by continuing to eat a
          balanced diet and staying consistently active.""")
elif bmi < 30:
    print("You are overweight!")
    print("""Aim for a slow, sustainable reduction in weight by prioritizing portion
          control and increasing your daily physical activity.""")
else:
    print("You are obese!")
    print("""Consult a healthcare professional to develop a safe, personalized,
    and comprehensive plan for weight management and long-term health.""")
