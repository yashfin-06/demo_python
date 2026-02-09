# age = 21
# name = "Raj"
# city = "Pune"

# # Format method
# s = "Student name is {} and age is {} lives in {}.".format(name, age, city)
# print(s)

# s2 = "Student name is {n} and age is {a} lives in {c}.".format(a = age,n = name, c = city)
# print(s2)

# # Old way using % operator

# s3 = "Student name is %s and age is %d lives in %s." % (name, age, city)
# print(s3)

# # f-Strings (Python 3.6+)

# s4 = f"Student name is {name} and age is {age} lives in {city}."
# print(s4)

# Table creation using f-Strings

r = "Roll No"
n = "Name"
m = "Marks"

r1=1
n1 = "Jay"
m1 = 95
r2 =2
n2 = "Raj"
m2 = 88
print("-"*44)
print(f"|{r:^10}|{n:^20}|{m:^10}|")
print("-"*44)
print(f"|{r1:^10}|{n1:^20}|{m1:^10}|")
print("-"*44)
print(f"|{r2:^10}|{n2:^20}|{m2:^10}|")
print("-"*44)

# 1,20,400