import turtle

def star(size=50, color="black"):
    t = turtle.Turtle()
    t.color(color)
    for i in range(5):
        t.fd(size)
        t.rt(144)

def main():
    side_length = int(input("Nhập độ dài cạnh của hình ngôi sao: "))
    color = input("Nhập màu sắc: ")
    star(side_length, color)

if __name__ == '__main__':
    main()
