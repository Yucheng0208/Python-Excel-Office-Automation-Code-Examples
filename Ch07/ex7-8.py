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