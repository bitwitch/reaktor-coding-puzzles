import sys
from queue import Queue

if __name__ == "__main__":
    start = None
    finish = None
    finish_area = []

    # build graph
    graph = set()
    with open("android_links.txt", "r") as f:
        while 1:
            line = f.readline()
            if not line: 
                break
            parts = line.split(' ')
            c = parts[0].split(',')
            coord = (int(c[0]), int(c[1]))
            graph.add(coord)

            if len(parts) <= 1:
                continue

            path = parts[1].strip().split(',')
            for d in path:
                x, y = coord
                if d == 'L':
                    x = coord[0]-1
                elif d == 'R':
                    x = coord[0]+1
                elif d == 'D':
                    y = coord[1]+1
                elif d == 'U':
                    y = coord[1]-1
                elif d == 'S':
                    start = coord
                elif d == 'F':
                    finish_area.append(coord)
                else:
                    break

                coord = (x,y)
                graph.add(coord)

    # bfs to finish
    success = False
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    
    while not frontier.empty():
        current = frontier.get()
        if current in finish_area:
            success = True
            finish = current
            break
        for neighbor in [(current[0]-1,current[1]  ),
                         (current[0]+1,current[1]  ),
                         (current[0]  ,current[1]-1),
                         (current[0]  ,current[1]+1)]:
            if neighbor in graph and neighbor not in came_from:
                frontier.put(neighbor)
                came_from[neighbor] = current

    if not success:
        print("Failed to find neural path")
        sys.exit(1)

    print("FOUND TARGET!")

    # build path
    path = []
    current = finish
    while current != start:
        prev = came_from[current]
        if (current[0] == prev[0]):
            d = 'U' if current[1] < prev[1] else 'D'
        else:
            d = 'L' if current[0] < prev[0] else 'R'
        path.append(d)
        current = prev

    path.reverse()
    print(''.join(path))



