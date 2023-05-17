N = int(input())
for i in range(1,N+1):
    inputs = input()
    year = int(inputs[0:4])
    month = int(inputs[4:6])
    day = int(inputs[6:8])
    if 1>month or month>12:
        print(f"#{i} -1")
        continue
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if 1>day or 31<day:
            print(f"#{i} -1")
            continue
    if month == 4 or month == 9 or month ==11 or month == 6:
        if 1>day or 30<day:
            print(f"#{i} -1")
            continue
    if month == 2:
        if 1>day or 28<day:
            print(f"#{i} -1")
            continue
    print(f"#{i} {inputs[0:4]}/{inputs[4:6]}/{inputs[6:8]}")