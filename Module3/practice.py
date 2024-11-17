# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」

ans = 36

while True:
    try:
        num = int(input("請輸入1~100的數字:"))
    except ValueError:
        print("內容錯誤，請輸入數字")
        continue

    if num < 1 or num > 100:
        continue
    if num == ans:
        print("正確，密碼是" + str(ans))
        break
    elif num > ans:
        print("還要更小")
    else:
        print("還要更大")

    










