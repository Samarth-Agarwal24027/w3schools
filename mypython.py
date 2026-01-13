cars = ["Tata Motors", "Mahindra", "Maruti Suzuki", "Hyundai", "Kia", "Toyota"]
for i in cars:
    print(i)
    if i == "Hyundai":
        break
        print("This is inside the loop")
    else:
        print("This is outside the loop")