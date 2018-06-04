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
    result = 0
    boom = []
    for i in range(len(int)):
        for letter, value in values:
            if int[i] == letter:
                boom.append(value)
    boom.append(0)
    for i in range(len(int)):
        if boom[i] >= boom[i+1]:
            result = result + boom[i]
        else:
            result = result - boom[i]
    return result
    
def toRoman(num):

    roman = ''

    while num > 0:
        for j, i in values:
            while num >= i:
                roman += j
                num -= i
    return roman