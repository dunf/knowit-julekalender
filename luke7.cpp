#include <iostream>
#include <fstream>
#include <string>

using namespace std;

class Position {
    private:
        int x, y;
    public:
        Position() { x = 0; y = 0; }
        void setX(int a) { x = a; }
        void setY(int a) { y = a; }
        int getX() { return x; }
        int getY() { return y; } 
        void display() { cout << getY() << ", " << getX(); }
        void move(int distance, string direction) {
            if (direction == "north")
                setY(getY() + distance);
            else if (direction == "south")
                setY(getY() - distance);
            else if (direction == "east")
                setX(getX() - distance);
            else
                setX(getX() + distance);
        }
};

int main() {
    Position julenisse;
    int distances[10000];
    string directions[10000];
    ifstream file("luke7file");
    string w, m, direction;
    int distance = 0;
    int i = 0;
    while (file >> w >> distance >> m >> direction) {
        distances[i] = distance;
        directions[i++] = direction;
    }
    for (int i = 0; i < 10000; i++) 
        julenisse.move(distances[i], directions[i]);
    julenisse.display();
    cout << endl;
    return 0;
}