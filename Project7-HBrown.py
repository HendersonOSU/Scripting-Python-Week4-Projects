year = int(input("Enter the number of years: "))
salary = float(input("Enter salary: "))
percent = float(input("Enter the annual increase: "))

print("Year   Salary")
print("----=---=--==-")

for y in range(1, year+1):
    print(y, end = " ")
    print("%.2f" %salary)
    salary = salary * (1+percent/100)
    
