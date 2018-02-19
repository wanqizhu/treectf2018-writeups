#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void print_flag() {
	char *flag = malloc(1024);
	char sym[42] = {'h', 'e', 'c', '_', 'z', 'v', '{', 'l', 'w', 'a', '}', 'l', '_', 'F', 'e', 'g', 's', 'f', 't', 'g', 'T', 'e', 'e', 'm', '_', 'c', '_', 'o', 'p', 'b', 'e', 'r', 'r', 'n', '_', 'i', 'C', 'i', 'a', 'l', 's', 't'};
	int ind[41] = {7, 9, 29, 36, 20, 13, 6, 33, 1, 5, 1, 31, 3, 2, 27, 23, 28, 35, 7, 1, 3, 16, 1, 2, 31, 1, 18, 16, 3, 8, 35, 18, 0, 3, 17, 7, 9, 15, 3, 15, 10};
	int i;

	for (i=0; i<41; i++) {
		flag[i] = sym[ind[i]];
	}

	printf("%s\n", flag);
	return;
}


int main() {
	char sym[4] = {'{', '}', '_', 'a'};
	char one[10], two[10];
	int i;

	for (i=0; i<10; i++) {
		one[i] = sym[rand() % 4];
		two[i] = sym[rand() % 4];
	}

	for (i=0; i<10; i++) {
		if (one[i] != two[i]) {
			printf("Good try\n");
			return 0;
		}
	}

	printf("Wow, you are real lucky today. Here you go!\n\n");
	print_flag();
}