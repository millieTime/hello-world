from functools import reduce
ascii = [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]
letters = map(lambda x: chr(x), ascii)
phrase = reduce(lambda a, b: a+b, letters)
print(phrase)