def run(number_to_up):
    limit = 0;
    count = 0;
    while(True):
        limit += number_to_up ** count
        print(f"La potencia de {number_to_up} a la {count} es igual a {limit}")
        count += 1
        if(limit >=1000):
            print(f"Llegamos a limite de calculo")
            break

if __name__ == '__main__':
    run(int(input("Put your number to elevate: ")))