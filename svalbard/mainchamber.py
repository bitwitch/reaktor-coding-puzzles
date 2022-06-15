import sys

const = "AIUEO"

rules = {
    "GN": "G",
    "NT": "R",
    "RH": "N",
    "TG": "H",
    "HH": "T",
}


def mutate(gen):
    new_gen = ""
    i = 0
    while i < len(gen):
        c = gen[i]
        if c in const:
            new_gen += c
            i = i+1
            continue

        # if the last element is a pair
        if i == len(gen) -1:
            break

        pair = gen[i:i+2]

        if pair not in rules:
            print(f"Error: found unknown pair: {pair}")
            sys.exit(1)

        new_gen += rules[pair]

        i = i+2
    return new_gen


if __name__ == "__main__":
    gen_6 = "HHGNHHGNGNRHNTTGHHGNHHGNGNRHNTTGGNRHNTTGRHHHHHGNNTTGTGTGTGTGGNRHUNTTGTGTGTGTGGNRHTGTGGNRHTGTGGNRHTGTGGNRHTGTGGNRHGNRHNTTGRHHHHHGNTGTGGNRHTGTGGNRHGNRHNTTGRHHHHHGNTGTGGNRHTGTGGNRHGNRHNTTGRHHHHHGNORHHHHHGNHHGNHHGNHHGNHHGNGNRHNTTGHHGNHHGNGNRHNTTGHHGNHHGNGNRHNTTGGNRHNTTGRHHHHHGNNTTGTGTGTGTGGNRHRHHHHHGNHHGNHHGNHHGNHHGNGNRHNTTGATGTGGNRHTGTGGNRHGNRHNTTGRHHHHHGNTGTGGNRHTGTGGNRHGNRHNTTGRHHHHHGNHHGNHHGNGNRHNTTGHHGNHHGNGNRHNTTGGNRHNTTGRHHHHHGNNTTGTGTGTGTGGNRHERHHHHHGNHHGNHHGNHHGNHHGNGNRHNTTGHHGNHHGNGNRHNTTGHHGNHHGNGNRHNTTG"

    gen = gen_6
    for i in range(0,6):
        gen = mutate(gen)
        print(f"Generation {i}: {gen}")


