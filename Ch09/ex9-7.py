import turtle

t = turtle.Turtle()

# 畫第一個長方形
for _ in range(2):
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.right(90)

# 轉向以畫出第二個長方形
t.right(90)
t.forward(50)
t.left(90)

for _ in range(2):
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)

turtle.done()