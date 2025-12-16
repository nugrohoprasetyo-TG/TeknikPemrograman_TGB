#System print header
print("================================================")
print("======== Family Age Aaverage Calculator ========")
print("================================================")
print("")

#User input ammount of familly members
members = int(input("Please input the ammount of family members: "))
print("")

#Initialize total age variable
total_age = 0

#Input each member's age and add to total
for i in range(members):
    age = int(input(f"Enter the age of member {i+1}: "))
    total_age += age

#System calculate the average age
average_age = total_age / members

#System display the average age
print("")
print(f"the average age of the family is {average_age:.2f}")
