#include <stdio.h>
#include <pthread.h>

pthread_mutex_t mutex;
main()
{
	pthread_t idA, idB;
	void *MyThread(void *);

	if (pthread_mutex_init(&mutex, NULL) < 0) {
		perror("pthread_mutex_init");
		return 1;
	}
	if (pthread_create(&idA, NULL, MyThread, (void *)"A") != 0) {
		perror("pthread_create");
		return 1;
	}
	if (pthread_create(&idB, NULL, MyThread, (void *)"B") != 0) {
		perror("pthread_create");
		return 1;
	}
	(void)pthread_join(idA, NULL);
	(void)pthread_join(idB, NULL);
	(void)pthread_mutex_destroy(&mutex);
}

int x = 0;

void *MyThread(void *arg) {
	char *sbName;

	sbName = (char *) arg;
	IncrementX();
	printf("X = %d in Thread %s\n", x, sbName);
}

IncrementX()
{
	int Temp;

	BeginRegion();
	Temp = x;
	Temp = Temp + 1;
	x = Temp;
	EndRegion();
}

BeginRegion()
{
	pthread_mutex_lock(&mutex);
}

EndRegion()
{
	pthread_mutex_unlock(&mutex);
}
