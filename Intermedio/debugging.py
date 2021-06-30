def run():
    try:
        num = int(input("Put your number: "))
        print(divisors(num))
    except ValueError as ve:
        print("Tienes que colocar un valor de tipo numerico")
        exit(0)

def divisors(num):
    return [ x for x in range(1,num +1) if num % x == 0]

if __name__ == "__main__":
    run()

#asserts
#raise