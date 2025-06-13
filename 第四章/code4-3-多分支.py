score = 98

if score >= 98:
    print("A")
elif score >80 and score <90:
    print("B")
elif score >70 and score < 80:
    print("C")
else:
    print("D")

# bmi计算
w = float(input("请输入你的体重，单位KG："))
h = float(input("请输入你的身高，单位M："))
bmi = w / (h * h)
print(bmi)
if bmi < 18.5:
    print("偏瘦")
elif 18.5 <= bmi < 25:
    print("正常")
elif 25 <= bmi < 30:
    print("偏胖")
else:
    print("肥胖")