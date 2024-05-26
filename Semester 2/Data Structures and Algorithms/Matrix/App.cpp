
#include <iostream>
#include "Matrix.h"
#include "ExtendedTest.h"
#include "ShortTest.h"

using namespace std;


int main() {
	testAll();
	testAllExtended();
	cout << "Test End" << endl;
	Matrix m{ 4,4 };
	m.modify(1, 1, 3);
	m.modify(3, 1, 2);
	m.modify(3, 3, 5);
	m.resize(8, 8);
	m.modify(7, 5, 9);
	cout << m.nrColumns() << " " << m.nrLines() << " " << m.element(7, 5) << " " << m.element(6, 6) << "\n";
	m.resize(4,4);
	cout << m.nrColumns() << " " << m.nrLines() << "\n";
	try {
		m.element(7, 5);
	}
	catch (exception)
	{
		cout << "not valid\n";
	}
	system("pause");
}