categories = ["Sedan", "SUV", "Hatchback"]
cars = ["Tata Motors", "Mahindra", "Maruti Suzuki", "Hyundai", "Kia", "Toyota"]

for i in categories:
    #print(i)
    for j in cars:
        print(i, j)
        if j == "Kia":
            break