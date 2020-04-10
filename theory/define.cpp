#include <iostream>

using std::cout;

#define a (x+1)


int x = 2;

void b() {
    x = a;

    cout << "B: [x: " << x << "]\n";
}

void c() {
    int x = 1;

    cout << "C: [x: " << a << "]\n";
}

int main(int argc, char const *argv[]){
    
    b();
    c();

    return 0;
}
