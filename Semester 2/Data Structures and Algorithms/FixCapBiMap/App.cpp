#include "ExtendedTest.h"
#include "ShortTest.h"

#include "FixedCapBiMap.h"
#include "FixedCapBiMapIterator.h"

#include <iostream>
using namespace std;


int main() {
	testAll();
//	testAllExtended();

	FixedCapBiMap map(10);
	map.add(11, 3);
	map.add(12, 8);
	map.add(13, 7);
	map.add(14, 1);
	map.add(15, 4);

	FixedCapBiMapIterator mapIter =  map.iterator();

	for (int i = 0; i < map.size(); i++)
	{
		TElem element = mapIter.getCurrent();
		mapIter.next();
		cout << element.first << " " << element.second;
		cout << " \n";
	}


	cout << "That's all!" << endl;
	system("pause");
	return 0;
}


