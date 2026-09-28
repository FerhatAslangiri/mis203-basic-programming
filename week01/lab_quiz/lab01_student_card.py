# lab01_student_card.py

print("=== Student Introduction Card Generator ===")
name = input("Enter your full name: ")
student_id = input("Enter your student ID: ")
department = input("Enter your department: ")
github = input("Enter your GitHub username: ")
goal = input("Enter your programming goal: ")

print("\n" + "=" * 42)
print("             STUDENT ID CARD              ")
print("=" * 42)
print(f" Name        : {name}")
print(f" Student ID  : {student_id}")
print(f" Department  : {department}")
print(f" GitHub      : github.com/{github}")
print(f" Goal        : {goal}")
print("=" * 42)
