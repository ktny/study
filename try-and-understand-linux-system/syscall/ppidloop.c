// 親プロセスのIDを表示するプログラム
// CPUのカーネル時間が支配的になることを確認するために使います。

#include <sys/types.h>
#include <unistd.h>

int main(void)
{
    for (;;)
        getppid();
}
