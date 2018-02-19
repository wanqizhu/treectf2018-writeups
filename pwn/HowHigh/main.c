#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>


void vulnFun() {
    char *argv[] = {"/bin/sh", 0};
    char *envp[] = {0};

    execve("/bin/sh", argv, envp);
}

void jump() {
    char buff[10];
    printf("You say jump.\n");
    printf("I say how high.\n");
    printf("How high?: ");
    fgets(buff, 48, stdin);
    int inp;
    int res = sscanf(buff, "%d", &inp);
    if(res == 0) {
        printf("You don't understand heights very well...\n");
    } else {
        printf("Not high enough!\n");
    }
}

int main() {
    jump();
    return 0;
}
