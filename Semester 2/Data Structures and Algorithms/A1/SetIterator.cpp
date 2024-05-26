#include "SetIterator.h"
#include "Set.h"
#include <exception>

// Theta(1)
SetIterator::SetIterator(const Set& m) : set(m), currentPosition(0)
{
	first();
}

// Best case: Theta(1)
// Worst case: Theta(n) The element on the last position of the hashtable is the only element
void SetIterator::first() {
	currentPosition = 0;
	while (currentPosition < set.capacity && (set.elements[currentPosition] == NULL_TELEM || set.deleted[currentPosition])) {
		currentPosition++;
	}
}

// Best case: Theta(1)
// Worst case: Theta(n) The element on the last position of the hashtable is the next one
void SetIterator::next() {
	if (!valid()) {
		throw std::exception();
	}

	currentPosition++;
	while (currentPosition < set.capacity && (set.elements[currentPosition] == NULL_TELEM || set.deleted[currentPosition])) {
		currentPosition++;
	}
}

// Theta(1)
TElem SetIterator::getCurrent()
{
	if (!valid()) {
		throw std::exception();
	}

	return set.elements[currentPosition];
}

// Theta(1)
bool SetIterator::valid() const {
	if (currentPosition < set.capacity && currentPosition >= 0 && set.elements[currentPosition] != NULL_TELEM && !set.deleted[currentPosition])
		return true;
	return false;
}

void SetIterator::previous()
{
	if (!valid()) {
		throw std::exception();
	}

	currentPosition--;
	while (currentPosition < set.capacity && currentPosition >= 0 && (set.elements[currentPosition] == NULL_TELEM || set.deleted[currentPosition])) {
		currentPosition--;
	}
}



