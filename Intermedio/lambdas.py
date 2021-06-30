def palindromo(string):
    return string == string[::-1]

if __name__ == "__main__":
    palin_2 = lambda string : string == string[::-1]
    print(palin_2("lucho"))
    print(palindromo("ana"))