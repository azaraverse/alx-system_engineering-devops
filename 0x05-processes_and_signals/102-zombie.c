#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - an infinite while loop
 *
 * Return: 0
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - a function that creates five zombie process
 *
 * Return: 0
*/
int main(void)
{
	int i;
	pid_t zombie;

	i = 0;
	while (i <= 4)
	{
		zombie = fork();
		if (!zombie)
			return (0);

		printf("Zombie process created, PID: %u\n", zombie);
		i++;
	}

	infinite_while();

	return (0);
}
