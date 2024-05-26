#include "SortedBagIterator.h"
#include "SortedBag.h"
#include <exception>

using namespace std;

// Constructor
// Time complexity : O(1)
SortedBagIterator::SortedBagIterator(const SortedBag& b) : bag(b) {
	//TODO - Implementation
	this->index = 0;
}

// Returns the element from the bag at the current index if it is valid or throws an exception
// Time complexity: O(1)
TComp SortedBagIterator::getCurrent() {
	//TODO - Implementation
	if (valid() == true)
		return this->bag.elements[this->index];
	else
		throw std::exception();
}

// Checks if the index is valid
// Time complexity: O(1)
bool SortedBagIterator::valid() {
	//TODO - Implementation
	if (this->index >= 0 && this->index < this->bag.nrElements)
		return true;
	return false;
}

// Checks if it can increment the index or throws an exception
// Time complexity: O(1)
void SortedBagIterator::next() {
	//TODO - Implementation
	if (valid() == true)
		this->index++;
	else
		throw std::exception();

}

// Sets the index to 0
// Time complexity: O(1)
void SortedBagIterator::first() {
	//TODO - Implementation
	this->index = 0;
}

