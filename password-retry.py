# 密碼重試程式
# 先在程式碼中 設定好密碼 password = 'a123456'
# 讓使用者【最多輸入3次密碼】
# 不對的話，就印出"密碼錯誤! 還有__次機會!"
# 對的話，就印出"登入成功!"
# 進階挑戰：剩餘0次的時候不要印

password = 'a123456'
test_max = 3 # 剩餘次數

while test_max > 0:
	test_max -= 1
	user_input = input("請輸入密碼:")
	if user_input == password:
		print("登入成功!") # 跳出迴圈
		break
	elif test_max > 0:
		print("密碼錯誤! 還有", test_max, "次機會!")

	