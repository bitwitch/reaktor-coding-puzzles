#include <stdio.h>
#include <iostream>
#include <fstream>
#include <cmath>
#include <cstring>
#include <unordered_map>
#include <queue>
#include <vector>

using namespace std;

struct Cell {
    int x, y;
    bool operator==(const Cell& other) const {
        return this->y == other.y && this->x == other.x;
    }
    bool operator!=(const Cell& other) const {
        return this->y != other.y || this->x != other.x;
    }

    struct hash_func {
        size_t operator()(const Cell& cell) const {
            size_t row = std::hash<int>()(cell.y);
            size_t col = std::hash<int>()(cell.x) << 1;
            return row ^ col;
        }
    };
};

enum Directions {
    RIGHT = 0,
    DOWN =  1,
    LEFT =  2,
    UP =    3
};

void generate_image() {
    int width = 129;
    int height = 121;

    ofstream out;
    out.open("maze.ppm");
    out << "P3" << '\n' << width << '\n' << height << '\n' << 255 << '\n';

    FILE *fp = fopen("maze_data.txt", "r");

    for (int j=0; j<height; ++j) {
        for (int i=0; i<width+1; ++i) {
            int r, g, b;
            int c = fgetc(fp);
            switch(c) {
                case '\n': continue;
                case '#': r = g = b = 0; break;
                case '.': r = g = b = 255; break;
                case '$': r = 250; g = 210; b = 10; break;
                case 'a':
                case 'b':
                case 'c':
                case 'd':
                case 'e':
                case 'f':
                case 'g':
                case 'h':
                case 'i':
                {
                    float x = (c - 97.0) / 8.0;
                    r = (int)(255.0 * (8.0 * (x+0.02) * exp(1.0 - 8.0 * (x+0.02))));
                    g = (int)(255.0 * (8.0 * (x-0.3)  * exp(1.0 - 8.0 * (x-0.3))));
                    b = (int)(255.0 * (8.0 * (x-0.6)  * exp(1.0 - 8.0 * (x-0.6))));
                    if (r<0) r = 0;
                    if (g<0) g = 0;
                    if (b<0) b = 0;
                    break;
                }
                case 'A':
                case 'B':
                case 'C':
                case 'D':
                case 'E':
                case 'F':
                case 'G':
                case 'H':
                case 'I':
                {
                    float x = (c - 65.0) / 8.0;
                    r = (int)(255.0 * (8.0 * (x+0.02) * exp(1.0 - 8.0 * (x+0.02))));
                    g = (int)(255.0 * (8.0 * (x-0.3) * exp(1.0 - 8.0 * (x-0.3))));
                    b = (int)(255.0 * (8.0 * (x-0.6) * exp(1.0 - 8.0 * (x-0.6))));
                    if (r<0) r = 0;
                    if (g<0) g = 0;
                    if (b<0) b = 0;
                    break;
                }
                default: r = 252; g = 100; b = 3; break;
            }
            out << r << ' ' << g << ' ' << b << ' ';
        }
        out << '\n';
    }
    out.close();
}

bool valid_move(vector<string> &grid, Cell cell) {
    char c = grid[cell.y][cell.x];

    // TODO(shaw): finish this implementation, based on keys held
    return (c == '.') || (c > 96 && c < 106) || (c == '>') || (c == '<');
}


void solve() {
    // TODO:
    // Pathfind to keys, then to their corresponding doors
    // pathfind to treasure
    // 
    //Cell keys[9];
    //Cell doors[9];


    int width = 129;
    int height = 121;

    // build a datastructure to represent the maze
    ifstream maze_file("maze_data.txt");
    vector<string> grid(height);
    for (int j=0; j<height; ++j) {
        std::getline(maze_file, grid[j]);
    }
    maze_file.close();

    bool success = false;
    Cell start = {1, 1};
    Cell target = {124, 117};

    // BFS to target
    queue<Cell> frontier;
    frontier.push(start);
    unordered_map<Cell, Cell, Cell::hash_func> came_from;

    while (frontier.size() > 0) {
        Cell current = frontier.front();
        frontier.pop();

        if (current == target) {
            success = true;
            break;
        }

        Cell neighbors[4] = {
            {current.x+1, current.y}, // right
            {current.x, current.y+1}, // down
            {current.x-1, current.y}, // left
            {current.x, current.y-1}  // up
        };

        for (auto cell : neighbors) {
            if (came_from.count(cell) == 0 && valid_move(grid, cell)) {
                frontier.push(cell);
                came_from[cell] = current;
            }
        }
    }

    if (!success) {
        printf("Failed to reach target.\n");
        return;
    }

    printf("REACHED TARGET!\n");

    Cell current = target;
    vector<int> directions;
    int dir;
    Cell previous;

    while (current != start) {
        previous = came_from[current];

        if (current.x == previous.x)
            dir = current.y < previous.y ? UP : DOWN;
        else
            dir = current.x < previous.x ? LEFT : RIGHT;

        directions.push_back(dir);
        current = previous;
    }


    printf("DATA ");
    int last = directions.size() - 1;
    for (int i=last; i>=0; --i)
        printf("%d,", directions[i]);
    printf("-1\n");
}

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("Usage: %s {image, solve}\n", argv[0]);
        return 1;
    }

    if (0 == strcmp(argv[1], "image"))
        generate_image();
    else if (0 == strcmp(argv[1], "solve"))
        solve();
    else
        printf("Unknown command: %s\n", argv[1]);

    return 0;
}
