import turtle

def triangle(size=50, color="black"):
    t = turtle.Turtle()
    t.color(color)
    for i in range(3):
        t.fd(size)
        t.rt(120)

def main():
    side_length = int(input("Nhập độ dài cạnh của hình tam giác: "))
    color = input("Nhập màu sắc: ")
    triangle(side_length, color)

if __name__ == '__main__':
    main()
