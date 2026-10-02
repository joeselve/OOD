def is_palindrome(inp : str, i = 0):
    if i >= len(inp) - i - 1:
            return True
    if inp[i] != inp[len(inp) - i - 1]:
        return False

    return is_palindrome(inp, i + 1)

print(is_palindrome("radar"))
print(is_palindrome("python"))
print(is_palindrome("abxa"))