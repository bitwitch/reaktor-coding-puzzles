import json

if __name__ == "__main__":
    with open("flood.txt", "r") as f:
        data = json.loads(f.read())

    flood_dangers = []

    for region in data['regions']:
        for reading_item in region['readings']:
            reading = reading_item['reading']

            high_mark = (-1, -9999999)

            flood_danger = 0
            for x,y in enumerate(reading):
                if y >= high_mark[1]:
                    if x > high_mark[0]+1:
                        # get area of flood danger
                        for h in reading[high_mark[0]:x]:
                            flood_danger += high_mark[1] - h

                    high_mark = (x,y)


            right_mark = (-1, -9999999)
            # now go from right to left up to the high_mark to get remaining flood areas
            x = len(reading)-1
            while x >= high_mark[0]:
                y = reading[x]
                if y >= right_mark[1]:
                    if x < right_mark[0]-1:
                        # get area of flood danger
                        for h in reading[x+1:right_mark[0]]:
                            flood_danger += right_mark[1] - h
                    right_mark = (x,y)
                x -= 1

            reading_item['flood_danger'] = flood_danger

    # get password from flood danger regions
    password = ""
    for region in data['regions']:
        i = 0
        while i < len(region['readings']) - 1:
            reading_0 = region['readings'][i]
            reading_1 = region['readings'][i+1]
            if reading_1['flood_danger'] - reading_0['flood_danger'] > 1000:
                password += reading_1['readingID']
            i = i + 1
    print(password)




