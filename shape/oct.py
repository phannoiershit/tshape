import turtle

def octagon(size=50, color="black"):
    t = turtle.Turtle()
    t.color(color)
    for i in range(8):
        t.fd(size)
        t.rt(45)

def main():
    side_length = int(input("Nhập độ dài cạnh của hình bát giác: "))
    color = input("Nhập màu sắc: ")
    octagon(side_length, color)

if __name__ == '__main__':
    main()
