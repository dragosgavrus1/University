#include "SortedSetIterator.h"
#include <exception>

using namespace std;

// Theta(1)
SortedSetIterator::SortedSetIterator(const SortedSet& m) : multime(m)
{
	this->current = this->multime.head;
}

// Theta(1)
void SortedSetIterator::first() {
	this->current = this->multime.head;
}

// Theta(1)
void SortedSetIterator::next() {
	if (valid())
	{
		current = this->multime.next[current];
	}
	else
	{
		throw std::exception();
	}
}

// Theta(1)
TElem SortedSetIterator::getCurrent()
{
	if (valid())
	{
		return this->multime.elems[current];
	}
	else
	{
		throw std::exception();
	}
}

// Theta(1)
bool SortedSetIterator::valid() const {
	if (current != -1)
		return true;
	return false;
}

