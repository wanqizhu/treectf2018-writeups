
all: main

main: main.c
	gcc -fno-stack-protector -z execstack -no-pie -o main main.c

clean: 
	rm main
