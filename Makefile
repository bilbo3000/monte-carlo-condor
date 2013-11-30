
all: example_solution

example_solution: example_solution.c libassignment4.so
	gcc -fPIC -o example_solution example_solution.c -lassignment4 -L.

clean:
	rm example_solution

test: example_solution
	LD_LIBRARY_PATH=. ./example_solution
