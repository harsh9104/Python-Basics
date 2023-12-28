students = ["ram", "shyam", "radha", "kishan", "radhika"]

#Break Statement
for student in students:
    if student == "radha":
        break
    print(student)

#Continue Statement
for student in students:
    if student == "shyam":
        continue
    print(student)
