def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = { "fistname":"Ramon","lastname":"Aguado"}

    super_list = [
        { "fistname":"Ramon","lastname":"Aguado"},
        { "fistname":"Miguel","lastname":"Torres"},
        { "fistname":"Pepe","lastname":"Rodelo"},
        { "fistname":"Susana","lastname":"Martinez"},
        { "fistname":"Jose","lastname":"Garcia"},
    ]

    super_dict = {
        "natural_nums" : [1,2,3,4,5],
        "integer_nums" : [-2,-1,0,1,2],
        "floating_nums" : [1.1,4.5,6.43]
    }

    for key, value in super_dict.items():
        print(f"{key} - {value}")


if __name__ == "__main__":
    run()