import math

def run():
    return {x : math.sqrt(x) for x in range(1,1001)}


if __name__ == "__main__":
    print(run())