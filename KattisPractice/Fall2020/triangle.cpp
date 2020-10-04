#include <iostream>
#include <cmath>
using namespace std;

int perimeter(int n)
{
    if (n == 0)
        return 1;
    return ceil(log10(3) + n * log10(1.5));
}

int main()
{
    int x;
    int i = 1;
    string line;
    while (getline(cin, line))
    {
        x = stoi(line);
        int result = perimeter(x);
        printf("Case %d: %d\n", i, result);
        i++;
    }
}
