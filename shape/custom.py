import turtle

def regular(n, size=50, color="black"):
    t = turtle.Turtle()
    t.color(color)
    for i in range(n):
        t.fd(size)
        t.rt(360 / n)

def main():
    num_sides = int(input("Nhập số cạnh của đa giác đều: "))
    side_length = int(input("Nhập độ dài cạnh: "))
    color = input("Nhập màu sắc: ")
    regular(num_sides, side_length, color)

if __name__ == '__main__':
    main()
