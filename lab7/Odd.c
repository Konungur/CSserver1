#include <stdlib.h>
#include <stdio.h>

int main() 
{
    int a, b, i, m;
    printf("Enter two numbers:\n");
    scanf("%i", &a);
    scanf("%i", &b);
    if (a < b)
        for(i = a; i <= b; i++){
            m = i % 2;
            if (m == 0 && i > 9)
                printf("Even\n");
            else if(m != 0 && i > 9)
                printf("Odd\n");
            else
                printf("%d\n", i);
        }
    else
        printf("Unsuitable numbers");
    return 0;
}