h = float(input("Enter height where ball is dropped: "))
bx = float(input("Enter bounce index: "))
bs = int(input("Enter the amount of bounces for the ball: "))

d = h

for b in range(bs-1):
    h *= bx
    d += 2*h

d += h * bx

print("Distanced traveled is: " +str(d))
      
