'''Print the grade sheet of a student for the given range of cgpa. Scan marks of
five subjects and calculate the percentage.'''

print(f"Sample Grade\n")
name=input("Enter Name ")
rn=int(input("Enter roll Number "))
sap_id=int(input("Enter SAPID "))
sem=int(input("Enter semester "))
crs=input("Enter Course ")

print(f"\nEnter subject marks")
pds=int(input("Marks in pds"))
python=pds=int(input("Marks in Python"))
chem=pds=int(input("Marks in Chemistry"))
eng=pds=int(input("Marks in English"))
phy=pds=int(input("Marks in Physics"))



print(f"Name: {name} \t Roll Number: {rn}\nSAPID: {sap_id}\t Semester: {sem}\n Course:{crs}")

per=(pds+python+chem+eng+phy)/5

print(f"\nPercentage{per:.2f}")

score=per/10
print(f"\nCGPA:{score:.2f}")

if 0 <= score <= 3.4:
    grade = "F"
elif 3.5 <= score <= 5.0:
    grade = "C+"
elif 5.1 <= score <= 6.0:
    grade = "B"
elif 6.1 <= score <= 7.0:
    grade = "B+"
elif 7.1 <= score <= 8.0:
    grade = "A"
elif 8.1 <= score <= 9.0:
    grade = "A+"
elif 9.1 <= score <= 10.0:
    grade = "O"
else:
    grade = "Invalid Score! Please enter a value between 0 and 10."

print(f"\nGRADE: {grade}")