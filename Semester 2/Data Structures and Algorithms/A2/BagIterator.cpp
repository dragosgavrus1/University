#include <exception>
#include "BagIterator.h"
#include "Bag.h"
#include <exception>

using namespace std;

// O(1) constructor
BagIterator::BagIterator(const Bag& c): bag(c)
{
	this->currElem = c.head;
	this->index = 0;
}

// O(1) ; sets the element to the first one
void BagIterator::first() {
	this->currElem = bag.head;
	this->index = 0;
}

// O(1) ; checks if the current element is valid and if the index of the element is the last one
void BagIterator::next() {

	if (valid() == true)
	{
		this->index++;
		if (this->index < currElem->frequency)
		{
			return;
		}
		else if(this->index == currElem->frequency)
		{
			currElem = currElem->next;
			this->index = 0;
		}
	}
	else
		throw std::exception();
}


// O(1) ; checks if the element is valid
bool BagIterator::valid() const {
	if (currElem != nullptr)
		return true;
	return false;
}


// O(1) ; returns the data from the current element if it's valid
TElem BagIterator::getCurrent() const
{
	if(valid() == true)
		return currElem->elem;
	else
		throw std::exception();
}
