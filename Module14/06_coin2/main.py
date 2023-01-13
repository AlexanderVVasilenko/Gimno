def check_circle(x, y, radius):
    if (x**2 + y ** 2) ** 0.5 <= radius:
        print("Coin is near.")
    else:
        print("Coin isn't near")


print("Enter the coordinates of coin:")
x_ = float(input("X: "))
y_ = float(input("y: "))
r = float(input("Enter the circle radius: "))
check_circle(x_, y_, r)
