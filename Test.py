data = {}
acc_exp = 0
for i in range(1, 201):
    if i == 1:
        exp = 10
    else:
        exp = int(((i-1) * 50 / 49) ** 1.5)
        acc_exp += exp
    data[i] = {'level': i, 'required_experience': exp, 'accumulated_experience': acc_exp}
print(data)