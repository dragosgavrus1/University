#include "Set.h"
#include "SetITerator.h"


// Theta(n)
void Set::resize()
{
	int newCapacity = capacity * 2;
	TElem* newElements = new TElem[newCapacity];
	bool* newDeleted = new bool[newCapacity];
	for (int i = 0; i < newCapacity; i++) {
		newElements[i] = NULL_TELEM;
		newDeleted[i] = false;
	}

	// Rehash the existing elements
	for (int i = 0; i < capacity; i++) {
		if (elements[i] != NULL_TELEM && !deleted[i]) {
			int position = hashFunction1(elements[i]);
			int step = hashFunction2(elements[i]);
			while (newElements[position] != NULL_TELEM) {
				position = (position + step) % newCapacity;
			}
			newElements[position] = elements[i];
		}
	}

	// Delete the old hashtable
	delete[] elements;
	delete[] deleted;

	// Update the capacity and pointers
	elements = newElements;
	deleted = newDeleted;
	capacity = newCapacity;
}


// Theta(n)
Set::Set() {
	capacity = 8; // Initial capacity of the hashtable (power of 2)
	nrElems = 0;
	elements = new TElem[capacity];
	deleted = new bool[capacity];
	for (int i = 0; i < capacity; i++) {
		elements[i] = NULL_TELEM;
		deleted[i] = false;
	}
}

// Best case: Theta(1) if the hash functions go trough the hash table in one iteration and the element is not a duplicate
// Worst case: Theta(n) if the hash functions have a low value and the hash table has a big capacity
// Complexity: O(log n) because of the hash functions
bool Set::add(TElem elem) {

	if (size() == capacity)
		resize();

	int position = hashFunction1(elem);
	int step = hashFunction2(elem);

	while (true) {
		if (elements[position] == elem && !deleted[position]) {
			return false;
		}

		position = (position + step) % capacity; // Probe the next position

		if (position == hashFunction1(elem))
		{
			break;
		}
	}

	while (elements[position] != NULL_TELEM && elements[position] != elem && !deleted[position]) {
		position = (position + step) % capacity; // Probe the next position
	}

	if (elements[position] == elem && !deleted[position])
		return false; // Element is already in the set

	elements[position] = elem;
	deleted[position] = false;
	nrElems++;

	return true;


}

// Best case: Theta(1) if the element of the first position of the first hash function needs to be deleted
// Worst case: Theta(n) if the hash functions have a low value and the hash table has a big capacity
// Complexity: O(log n) because of the hash functions
bool Set::remove(TElem elem) {
	int position = hashFunction1(elem);
	int step = hashFunction2(elem);

	while (true) {
		if (elements[position] == elem && !deleted[position]) {
			deleted[position] = true; // Mark the element as deleted
			nrElems--;
			return true; // Element removed successfully
		}

		position = (position + step) % capacity; // Probe the next position

		if (position == hashFunction1(elem))
			return false; // Element not found in the set
	}
}

// Best case: Theta(1) if the element of the first position of the first hash function needs to be deleted
// Worst case: Theta(n) if the hash functions have a low value and the hash table has a big capacity
// Complexity: O(log n) because of the hash functions
bool Set::search(TElem elem) const {
	int position = hashFunction1(elem);
	int step = hashFunction2(elem);

	while (true) {
		if (elements[position] == elem && !deleted[position]) {
			return true; // Element found
		}

		position = (position + step) % capacity; // Probe the next position

		if (position == hashFunction1(elem))
			return false; // Element not found in the set
	}


}

// Theta(1)
int Set::size() const {
	return nrElems;
}

// Theta(1)
bool Set::isEmpty() const {
	if (size() != 0)
		return false;
	return true;
}

// Theta(1)
Set::~Set() {
	delete[] elements;
	delete[] deleted;
}

// Theta(1)
SetIterator Set::iterator() const {
	return SetIterator(*this);
}


