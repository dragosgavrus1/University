#include "Bag.h"
#include "ShortTest.h"
#include "ExtendedTest.h"
#include <iostream>

using namespace std;

int main() {

	testAll();
	cout << "Short tests over" << endl;
	testAllExtended();
	cout << "All test over" << endl;

	Bag b;
	b.add(5);
	b.addOccurrences(3, 10);
	cout << "Size: " << b.size();
	cout << "\nNr occurrences: " << b.nrOccurrences(10);
}