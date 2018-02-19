#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>



void craft() {
    char buff[0x400];
    printf("Show me your crafting skills: ");
    fgets(buff, 0x4a0, stdin);
    printf("You have much to learn grasshopper.\n");
}

int main() {
    craft();
    return 0;
}
