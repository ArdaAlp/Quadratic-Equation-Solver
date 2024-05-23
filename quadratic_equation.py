print("Ax^2+Bx+C \nEnter the values in the format spesific format above!\n")

a = int(input("Value A: "))
b = int(input("Value B: "))
c = int(input("Value C: "))

discriminant = (b**2) - 4 * (a) * (c)

root1 = ((-b) + (discriminant ** 1/2)) / (2 * a)
root2 = ((-b) - (discriminant ** 1/2)) / (2 * a)

print("The Discriminant:", discriminant)

if (discriminant < 0):
    print("This Equation has no any real roots!")

elif (discriminant == 0):
    print("This Equation has two same real roots!")
    print("First Root:",root1, "Second Root:", root2)

else: 
    print("This Equation has two different real roots!")
    print("First Root:",root1, "Second Root:", root2)