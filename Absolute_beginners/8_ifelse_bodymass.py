# to calculate body mass index on Python

print("Body mass index calculation program ")
height = float(input("Enter height(m): "))
weight = int(input("Enter Weight(kg): "))

index = weight/(height* height)

if index <=18:
    print(f"\n underweight BMI: {index}")
elif index > 18 and index <=25:
    print(f"\n overweight BMI: {index}")
elif index > 25 and index <= 30:
    print(f"\n obese BMI: {index}")
elif index > 30:
    print(f"\n severely obese BMI: {index}")