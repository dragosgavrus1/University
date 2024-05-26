#include "SortedSet.h"
#include "SortedSetIterator.h"

// Theta(1)
SortedSet::SortedSet(Relation r) {
	this->relation = r;
	this->head = -1;
	this->tail = -1;
	this->elems = new TElem[capacity];
	this->next = new int[capacity];
	this->prev = new int[capacity];
	this->firstFree = 0;
	this->nrElems = 0;
}

// Complexity Theta(2*n)
void SortedSet::resize()
{
	capacity *= 2;

	// Allocate new arrays with the new capacity
	TElem* newElems = new TElem[capacity];
	int* newNext = new int[capacity];
	int* newPrev = new int[capacity];

	// Copy the existing elements and node indices to the new arrays
	for (int i = 0; i < capacity / 2; i++) {
		newElems[i] = elems[i];
		newNext[i] = next[i];
		newPrev[i] = prev[i];
	}

	// Initialize the remaining node indices in the new arrays
	for (int i = capacity / 2; i < capacity; i++) {
		newNext[i] = i + 1;
		newPrev[i] = i - 1;
	}
	newNext[capacity - 1] = -1;
	
	// Update the firstFree index and delete the old arrays
	firstFree = capacity / 2;
	delete[] elems;
	delete[] next;
	delete[] prev;

	elems = newElems;
	next = newNext;
	prev = newPrev;
}


// Best case: Theta(1) The first element is added
// Worst case: Theta(n) The last element is added
// Complexity O(n)
bool SortedSet::add(TComp elem) {
	// Check if the arrays need to be resized
	if (nrElems == capacity)
		resize();

	// Traverse the sorted set to find the position to insert the new element
	int current = head;
	int prevNode = -1;

	while (current != -1 && relation(elems[current], elem))
	{
		if (elems[current] == elem)
			return false;
		prevNode = current;
		current = next[current];
	}

	if (elems[current] == elem)
		return false;

	// Create new node
	int newNode = firstFree;
	firstFree = next[firstFree];
	elems[newNode] = elem;
	next[newNode] = current;

	// Check if node position is before the head
	if (prevNode == -1)
		head = newNode;
	else
		next[prevNode] = newNode;

	// Check if node position is after the tail
	if (current == -1)
		tail = newNode;
	else
		prev[current] = newNode;
	
	prev[newNode] = prevNode;
	nrElems++;

	return true;
}

// Best case: Theta(1) the element is the head
// Worst case: Theta(n) the element is the last one in the set
// Complexity: O(n)
bool SortedSet::remove(TComp elem) {
	int current = head;

	// Traverse the sorted array and search for the element to delete
	while (current != -1 && relation(elems[current], elem))
	{
		if (elems[current] == elem)
		{
			// Save the previous and next nodes if found
			int prevNode = this->prev[current];
			int nextNode = this->next[current];

			if (prevNode == -1)		// if node is the head change the head
			{
				head = nextNode; 
			}
			else
			{
				next[prevNode] = nextNode;		// so we don't use next[-1]
			}

			if (nextNode == -1)		// if node is the tail change the tail
			{
				tail = prevNode;
			}
			else
			{
				prev[nextNode] = prevNode;		// so we don't use prev[-1]
			}

			next[current] = firstFree;		// next for the current released space is the first free
			firstFree = current;		//  the first free space is now the current position
			nrElems--;
			return true;
		}
		current = next[current];
	}

	return false;
}

// Best case: Theta(1) the searched element is the head
// Worst case: Theta(n) the searched element is the tail
// Complexity: O(n)
bool SortedSet::search(TComp elem) const {
	int current = head;

	// Traverse the sorted array and search for the element
	while (current != -1 && relation(elems[current], elem))
	{
		if (elems[current] == elem)
			return true;
		current = next[current];
	}
	return false;
}

// Theta(1)
int SortedSet::size() const {
	return nrElems;
}


// Theta(1)
bool SortedSet::isEmpty() const {
	if (nrElems == 0)
		return true;
	return false;
}

// Theta(1)
SortedSetIterator SortedSet::iterator() const {
	return SortedSetIterator(*this);
}

// Best case: Theta(1) the sorted set s has only one element and the current set is empty
// Worst case: Theta(n) all of the elements of the set s are added to the end of the set
// Complexity: O(n)
void SortedSet::uni(const SortedSet& s)
{
	SortedSetIterator si(s);
	si.first();

	int elem = si.getCurrent();
	// Traverse the sorted set to find the position to insert the new element
	int current = head;
	int prevNode = -1;
	while (si.valid())
	{
		elem = si.getCurrent();
		if (nrElems == capacity)
			resize();

		while (current != -1 && relation(elems[current], elem))
		{
			if (elems[current] == elem)
				break;
			prevNode = current;
			current = next[current];
		}

		if (elems[current] == elem)
			break;

		// Create new node
		int newNode = firstFree;
		firstFree = next[firstFree];
		elems[newNode] = elem;
		next[newNode] = current;

		// Check if node position is before the head
		if (prevNode == -1)
			head = newNode;
		else
			next[prevNode] = newNode;

		// Check if node position is after the tail
		if (current == -1)
			tail = newNode;
		else
			prev[current] = newNode;

		prev[newNode] = prevNode;
		nrElems++;
		si.next();
	}
	
}

// Theta(1)
SortedSet::~SortedSet() {
	delete[] elems;
	delete[] next;
	delete[] prev;
}


