driving  = input('請問你有開過車嗎?')
if driving != '有' and driving != '沒':
    print('只能輸入 有/沒有')
    raise SystemExit

age = input('請問你的年齡?')
age = int(age)
if driving == '有':
    if age > 18:
        print('OK')
    else:
        print('NG')
elif driving == '沒':
    if age > 18:
        print('可考照')
    else:
        print('不可考照')
else:
    print('只能輸入 有/沒有')