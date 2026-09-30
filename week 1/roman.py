class translator:

    def deciToRoman(self, num):
        mapping = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        roman = ""
        for value, symbol in mapping:
            if num == 0:
                break
            count, num = divmod(num, value)
            roman += symbol * count
        return roman
    def romanToDeci(self, s):
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        n = len(s)
        for cha in range(n):
            if cha + 1 < len(s) and roman_map[s[cha]] < roman_map[s[cha + 1]]:
                total -= roman_map[s[cha]]
            else:
                total += roman_map[s[cha]]
        return total

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))