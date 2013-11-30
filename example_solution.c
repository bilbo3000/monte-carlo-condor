#include <stdio.h> 
#include <time.h> 
#include <stdlib.h> 

int main(int argc, char *argv[]) {
	if (argc != 2) {
		return 1; 
	}
	
	srand(time(NULL)); 
	
	unsigned long long n;  // Numer of iterations 
	unsigned long long count = 0;  // Number of points fall into the shape
	n = atoi(argv[1]);

	while (n > 0) {
		double x = (rand() % 1001) / 1000.0; 
		double y = (rand() % 1001) / 1000.0; 
		
		if (f(x, y)) {
			count++; 
		}
		
		n--; 
	}
	
	printf("%llu\n", count);
 
	return 0; 
}
