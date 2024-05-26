#include "SortedBag.h"
#include "SortedBagIterator.h"
#include <iostream>
#include "ShortTest.h"
#include "ExtendedTest.h"

using namespace std;

bool relation_main(TComp e1, TComp e2) {
	return e1 <= e2;
}

int main() {
	testAll();
	testAllExtended();

	SortedBag bag(relation_main);
	bag.add(3);
	bag.add(5);
	bag.add(5);
	bag.add(5);
	bag.add(5);
	bag.add(1);
	int count = bag.removeOccurrences(6, 5);
	cout << count << endl;

	cout << "Test over" << endl;
	system("pause");
}
