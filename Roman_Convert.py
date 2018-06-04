values = (('M',  1000),
         ('CM', 900),
         ('D',  500),
         ('CD', 400),
         ('C',  100),
         ('XC', 90),
         ('L',  50),
         ('XL', 40),
         ('X',  10),
         ('IX', 9),
         ('V',  5),
         ('IV', 4),
         ('I',  1))

def toArabic(int):
    arabic = 0
    carry = []
    for i in range(len(int)):
        for letter, value in values:
            if int[i] == letter:
                carry.append(value)
    carry.append(0)
    for i in range(len(int)):
        if carry[i] >= carry[i+1]:
            arabic = arabic + carry[i]
        else:
            arabic = arabic - carry[i]
    return arabic
    
def toRoman(num):

    roman = ''

    while num > 0:
        for j, i in values:
            while num >= i:
                roman += j
                num -= i
    return roman