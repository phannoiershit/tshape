import turtle

def pentagon(size=50, color="black"):
    t = turtle.Turtle()
    t.color(color)
    for i in range(5):
        t.fd(size)
        t.rt(72)

def main():
    side_length = int(input("Nhập độ dài cạnh của hình ngũ giác: "))
    color = input("Nhập màu sắc: ")
    pentagon(side_length, color)

if __name__ == '__main__':
    main()
