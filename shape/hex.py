import turtle

def hexagon(size=50, color="black"):
    t = turtle.Turtle()
    t.color(color)
    for i in range(6):
        t.fd(size)
        t.rt(60)

def main():
    side_length = int(input("Nhập độ dài cạnh của hình lục giác: "))
    color = input("Nhập màu sắc: ")
    hexagon(side_length, color)

if __name__ == '__main__':
    main()
