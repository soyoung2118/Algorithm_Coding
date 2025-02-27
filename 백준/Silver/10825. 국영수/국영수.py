N = int(input())

students = []

for _ in range(N):
  student = input().split()

  name = student[0]  
  scores = list(map(int, student[1:])) 

  student = [name] + scores
  students.append(student)


students = sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in students:
  print(student[0])