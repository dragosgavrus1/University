#include "SortedBag.h"
#include "SortedBagIterator.h"
#include <exception>
#include <cmath>
// Constructor, initializes the SortedBag object
// Time complexity: O(1) because it performs a fixed number of operations, regardless of the input size
SortedBag::SortedBag(Relation r) {
	//TODO - Implementation
	this->r = r; 
	this->nrElements = 0;
	this->capacity = 10;
	this->elements = new TComp[this->capacity];
}


// The add function inserts an element in the SortedBag object while maintaining the order imposed by the relation r
// If the dynamic array is full, it doubles its capacity
// The time complexity of this function is O(n), where n is the number of elements in the dynamic array
// In the worst case the function performs n shifts to the right
// Space complexity is O(n) because it might need to allocate a new dynamic array of twice the capacity
void SortedBag::add(TComp e) {
	//TODO - Implementation
	if (this->nrElements == this->capacity)
	{
		TComp* auxElements = new TComp[this->capacity * 2];
		for (int i = 0; i < this->nrElements; i++)
		{
			auxElements[i] = this->elements[i];
		}
		delete[] this->elements;
		this->elements = auxElements;
		this->capacity *= 2;
	}

	int index = this->nrElements - 1;
	while (index >=0 && this->r(e, this->elements[index]))
	{
		this->elements[index + 1] = this->elements[index];
		index--;
	}
	this->elements[index + 1] = e;
	this->nrElements++;
}


// The remove function removes the first occurrence of the element e in the SortedBag object
// The function has a time complexity of O(n), where n is the number of elements in the dynamic array
// In the worst case, when the element to be removed is at the beginning of the array, the function performs n shifts to the left.
bool SortedBag::remove(TComp e) {
	//TODO - Implementation
	bool found = false;
	
	for (int index = 0; index < this->nrElements; index++)
	{
		if (e == this->elements[index])
		{
			found = true;
		}
		if (found == true)
		{
			this->elements[index] = this->elements[index + 1];
		}
	}
	if (found == true)
	{
		this->nrElements--;
		return true;
	}
	else
	{
		return false;
	}
}


// The search function searches for the first occurrence of the element elem in the SortedBag object
// The function has a time complexity of O(log(n))
// Best case is O(1) when the element is at the middle of the bag
// Worst case is O(log(n)) when the element is not in the bag
bool SortedBag::search(TComp elem) const {
	//TODO - Implementation
	int r = this->nrElements - 1;
	int l = 0, mid = 0;

	while (l < r)
	{
		mid = (r + l) / 2;
		if (elem == this->elements[mid])
			return true;
		if (this->r(elem, this->elements[mid]))
		{
			r = mid - 1;
		}
		else
		{
			l = mid + 1;
		}
	}
	if (this->elements[l] == elem)
		return true;

	return false;
}

// The nrOccurrences function returns the number of occurrences of the element elem in the SortedBag object
// The function has a time complexity of O(n)
int SortedBag::nrOccurrences(TComp elem) const {
	//TODO - Implementation
	int index = this->nrElements - 1;
	int count = 0;
	while (index >= 0 && this->r(elem, this->elements[index]))
	{
		if (this->elements[index] == elem)
			count++;
		index--;
	}
	return count;
}


// The size function returns the number of elements in the SortedBag object
// The function has a time complexity of O(1) because it simply returns the nrElements variable
int SortedBag::size() const {
	return this->nrElements;
}

// The isEmpty function checks if the SortedBag object is empty or not
// The function has a time complexity of O(1) because it only checks if the nrElements variable is zero or not
bool SortedBag::isEmpty() const {
	if (this->size() == 0)
		return true;
	return false;
}

// The iterator function returns a SortedBagIterator object that can be used to iterate over the elements of the SortedBag object
// The function has a time complexity of O(1) because it simply creates and returns a SortedBagIterator object
SortedBagIterator SortedBag::iterator() const {
	return SortedBagIterator(*this);
}


// Best case nr is 0 and the function returns 0, time complexity O(1)
// Worst case time complexity is O(n)
int SortedBag::removeOccurrences(int nr, TElem elem)
{
	if (nr < 0)
		throw std::exception();
	if (nr == 0)
		return 0;
	int nr_occurences = nrOccurrences(elem);
	if (nr < nr_occurences)
		nr_occurences = nr;
	int found = -1;
	for (int index = 0; index < nrElements; index++)
	{

		if (this->elements[index] == elem )
		{
			found = index;
			break;
		}
	}
	for (int i = found; i+nr_occurences < nrElements; i++) {
		elements[i] = elements[i + nr_occurences];
		nrElements--;
	}
	return nr_occurences;
}

// Deconstructor
// Time complexity: O(1)
SortedBag::~SortedBag() {
	//TODO - Implementation
	delete[] this->elements;
}
