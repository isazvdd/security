#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("<file>");
    }
    else
    {
        char *file = argv[1];
        char command[255];
        for (int i = 0; i < 257; i++)
        {
            sprintf(command, "./caesar -%d %s > out.out", i, file);
            system(command);
            printf("key: %d\n", i);
            system("file out.out");
            sprintf(command, "./caesar -148 encrypted/vevxaYL8 > decrypted/vevxaYL8_%d", i);
            system(command);
        }
    }
    
    return 0;
}
