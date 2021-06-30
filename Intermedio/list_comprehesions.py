#squared natural numbers challenge , list comprehesions
def run():
    return [x for x in range(1, 99999) if x % 36 == 0 ]
    

if __name__ == "__main__":
    print(run())