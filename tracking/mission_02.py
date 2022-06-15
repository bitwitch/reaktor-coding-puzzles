import json
from pprint import pprint
from math import sqrt

if __name__ == "__main__":
    with open("ppb.bin.log", "r") as f:
        raw = f.read()
    data = json.loads(''.join([chr(int(bin_str,2)) for bin_str in raw.split(' ')]))

    # calculate population and mean
    population = 0
    mean = 0
    for record in data:
        for reading in record['readings']:
            population += 1
            sum = 0
            for v in reading['contaminants'].values():
                sum += v
            mean += sum
            reading['total'] = sum

    mean /= population

    # calculate standard deviation
    std_dev = 0
    for record in data:
        for reading in record['readings']:
            sum = reading['total']
            std_dev += pow(sum-mean, 2)

    std_dev = sqrt(std_dev/population)

    # find anomolies
    anomolies = []
    for record in data:
        for reading in record['readings']:
            sum = reading['total']
            if sum >= mean+std_dev:
                anomolies.append(reading)

    print(f"pop: {population} mean: {mean}, std_dev: {std_dev}")
    print(f"Found {len(anomolies)} anomolies")

    # parse id of the anomoly readings
    for anomoly in anomolies:
        password = ""
        id = anomoly['id']
        i = 0
        while i < len(id)-1:
            password += chr(int(id[i:i+2],16))
            i+=2
        print(password)


