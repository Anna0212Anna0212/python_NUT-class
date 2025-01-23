
   # 輸入體重和身高
weight = float(input("請輸入您的體重（公斤）："))
height = float(input("請輸入您的身高（公尺）："))

# 計算 BMI
bmi = weight / (height ** 2)

# 判斷體重分類
if bmi < 18.5:
    category = "過輕"
elif bmi < 24:
    category = "正常"
elif bmi < 27:
    category = "過重"
else:
    category = "肥胖"

# 顯示結果
print(f"您的 BMI 是：{bmi:.2f}")
print(f"您的體重分類為：{category}")
