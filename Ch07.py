# Q4
str1 = input("請輸入第一個字串: ")
str2 = input("請輸入第二個字串: ")
print("連接後的字串:", str1 + str2)

# Q5
lst = [i + 1 for i in range(10)]
total = sum(lst)
average = total / len(lst)
print("總和:", total, "平均:", average)

# Q7
students = ["tom", "mary", "joe"]
scores = (85, 76, 58)

print("學生數:", len(students))
print("總分:", sum(scores))
print("平均:", sum(scores) / len(scores))

index = int(input("請輸入學號 (0~2): "))
if 0 <= index < len(students):
    print("學生:", students[index], "成績:", scores[index])
else:
    print("學號輸入錯誤")

# Q8
student_scores = {
    "tom": 85,
    "mary": 76,
    "joe": 58
}

name = input("請輸入學生姓名: ").lower()
if name in student_scores:
    print("學生:", name, "成績:", student_scores[name])
else:
    print("查無此學生")
