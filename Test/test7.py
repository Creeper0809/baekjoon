
encypt = input()
alpha = {}

alpha["a"] = encypt[0]
alpha["b"] = encypt[1]
alpha["c"] = encypt[2]
alpha["d"] = encypt[3]
alpha["e"] = encypt[4]
alpha["f"] = encypt[5]
alpha["g"] = encypt[6]
alpha["h"] = encypt[7]
alpha["i"] = encypt[8]
alpha["j"] = encypt[9]
alpha["k"] = encypt[10]
alpha["l"] = encypt[11]
alpha["m"] = encypt[12]
alpha["n"] = encypt[13]
alpha["o"] = encypt[14]
alpha["p"] = encypt[15]
alpha["q"] = encypt[16]
alpha["r"] = encypt[17]
alpha["s"] = encypt[18]
alpha["t"] = encypt[19]
alpha["u"] = encypt[20]
alpha["v"] = encypt[21]
alpha["w"] = encypt[22]
alpha["x"] = encypt[23]
alpha["y"] = encypt[24]
alpha["z"] = encypt[25]


string_arr = input()
for i in string_arr:
    if 'a'<=i<='z':
        print(alpha[i],end="")
    elif 'A'<=i<='Z':
        print(alpha[i.lower()].upper(), end="")
    elif i == " ":
        print(" ",end="")


