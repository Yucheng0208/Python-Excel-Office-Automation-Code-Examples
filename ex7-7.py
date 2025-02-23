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