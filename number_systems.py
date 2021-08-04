# calculates the decimal value of the binary integer represented by the string "11110101"
x = "11110101"
print(
    int(x[0]) * pow(2,7) +
    int(x[1]) * pow(2,6) +
    int(x[2]) * pow(2,5) +
    int(x[3]) * pow(2,4) +
    int(x[4]) * pow(2,3) +
    int(x[5]) * pow(2,2) +
    int(x[6]) * pow(2,1) +
    int(x[7]) * pow(2,0)
)

# doing the same with Python functionality
print(int("11110101",base = 2))

# calculates the decimal value of the hexadecimal integer represented by the string "FF2E"
hexdict ={
    "0":0,
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "A":10,
    "B":11,
    "C":12,
    "D":13,
    "E":14,
    "F":15
}
print(hexdict["F"]*(pow(16,3)) + hexdict["F"]*(pow(16,2)) + hexdict["2"]*(pow(16,1)) + hexdict["E"]*(pow(16,0)))

# doing the same with Python functionality
print(int("FF2E",base = 16))
