#include <stdio.h>
#include <unistd.h>
#include <string.h>

char password[] = "treeCTF{ice_melts_(sometimes?)}";

int main (int argc, char* argv[], char* envp[]){

puts("What's the password?");
char input[sizeof(password)];
read(0, input, sizeof(password));

int i;
for (i = 0; i < strlen(password); i++){
  if (input[i] != password[i]){
    puts("WRONG!");
    return 1;
  }
}

puts("You got it!");
return 0;

}
