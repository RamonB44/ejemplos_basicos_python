def run(name):
    for letter in name:
        print(letter.upper())
        
#comentario de prueba
if __name__  == '__main__':
    name = input("Put your frass: ")
    run(name)