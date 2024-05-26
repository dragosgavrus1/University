#include "Set.h"
#include "SetIterator.h"
#include "ExtendedTest.h"
#include "ShortTest.h"
#include <stack>
#include <iostream>
using namespace std;




int main() {

	testAll();
	testAllExtended();

	Set s;
	s.add(3);
	s.add(2);
	s.add(5);
	s.add(7);

	SetIterator si = s.iterator();
	si.first();
	for (int i = 0; i < 3; i++)
	{
		cout << si.getCurrent() << " ";
		si.next();
	}
	cout << si.getCurrent() << " ";
	cout << "\n";
	for (int i = 0; i < 4; i++)
	{
		cout << si.getCurrent() << " ";
		si.previous();
	}

	cout << "\n" << "That's all!" << endl;
	system("pause");

}



