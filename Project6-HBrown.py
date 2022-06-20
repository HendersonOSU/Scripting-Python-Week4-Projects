iterations = int(input("Number of iterations: "))


d = 1
t = 0
x = 1

while(x <= iterations):
    if(x % 2 == 1):
        t = t +(1 / d)

    else:
        t = t -(1/d)
    x = x + 1
    d = d + 2

print("The approximation is: ", t * 4)

    
