#include "ShortTest.h"
#include "ExtendedTest.h"
#include "SortedSet.h"
#include "SortedSetIterator.h"
#include <iostream>

using namespace std;

bool relation(TComp e1, TComp e2) {
	if (e1 <= e2) {
		return true;
	}
	else {
		return false;
	}
}

int main() {
	testAll();
	testAllExtended();
	SortedSet s1(relation);
	SortedSet s2(relation);
	s1.add(1);
	s1.add(3);
	s1.add(5);

	s2.add(2);
	s2.add(4);
	s2.uni(s1);
	
	SortedSetIterator si = s2.iterator();
	si.first();
	cout << "\n" << s2.size() << "\n";
	while (si.valid())
	{
		cout << si.getCurrent() << " ";
		si.next();
	}

	cout << "Test end" << endl;
	system("pause");
}