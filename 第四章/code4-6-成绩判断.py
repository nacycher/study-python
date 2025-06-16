py_score = input("请输入你的Python成绩：")
c_score = input("请输入你的C成绩：")
if py_score.isdigit() and c_score.isdigit():
    py_score = int(py_score)
    c_score = int(c_score)
    if py_score >= 60 and c_score >= 60:
        print("考试通过")
    else:
        print("考试未通过")