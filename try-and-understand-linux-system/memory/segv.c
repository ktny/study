#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *p = NULL;
    puts("before invalid access");

    // SIGSEGVが起きるため、以下の行以降は実行されない
    *p = 0;
    puts("after invalid access");
    exit(EXIT_SUCCESS);
}
