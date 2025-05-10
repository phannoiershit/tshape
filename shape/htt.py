import turtle

def heptagon(size=50, color="black"):
    t = turtle.Turtle()
    t.color(color)
    for i in range(7):
        t.fd(size)
        t.rt(360 / 7)

def main():
    side_length = int(input("Nhập độ dài cạnh của hình thất giác: "))
    color = input("Nhập màu sắc: ")
    heptagon(side_length, color)

if __name__ == '__main__':
    main()
