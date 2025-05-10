import turtle

def square(size=50, color="black"):
    t = turtle.Turtle()
    t.color(color)
    for i in range(4):
        t.fd(size)
        t.rt(90)

def main():
    side_length = int(input("Nhập độ dài cạnh của hình vuông: "))
    color = input("Nhập màu sắc: ")
    square(side_length, color)

if __name__ == '__main__':
    main()
