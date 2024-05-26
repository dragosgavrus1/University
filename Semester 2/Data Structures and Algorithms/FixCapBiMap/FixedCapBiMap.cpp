#include "FixedCapBiMap.h"
#include "FixedCapBiMapIterator.h"
#include <exception>


FixedCapBiMap::FixedCapBiMap(int capacity) {
	if (capacity <= 0) {
		throw std::exception();
	}
	this->capacity = capacity;
	nrElements = 0;
	elements = new TElem[capacity];

}

FixedCapBiMap::~FixedCapBiMap() {
	delete[] this->elements;
}

bool FixedCapBiMap::add(TKey c, TValue v){
	if (this->capacity == this->nrElements)
	{
		throw std::exception();
	}

	TElem element;
	element.first = c;
	element.second = v;
	int count = 0;
	for (int i = 0; i < this->nrElements; i++)
	{
		if (this->elements[i].first == c)
		{
			count++;
		}
	}
	if (count == 2)
		return false;
	else
	{
		this->elements[this->nrElements] = element;
		this->nrElements++;
		return true;
	}
}

ValuePair FixedCapBiMap::search(TKey c) const{
	int count = 0;
	ValuePair valuePair;
	valuePair.first = NULL_TVALUE;
	valuePair.second = NULL_TVALUE;
	for (int i = 0; i < nrElements; i++)
	{
		if (elements[i].first == c)
		{
			if (count == 0)
				valuePair.first = elements[i].second;
			else
			{
				valuePair.second = elements[i].second;
			}
			count++;
			
		}
	}
	if( count == 0)
		return std::pair<TValue, TValue>(NULL_TVALUE, NULL_TVALUE);
	return valuePair;
}

bool FixedCapBiMap::remove(TKey c, TValue v){
	bool found = false;
	for (int i = 0; i < nrElements; i++)
	{
		if (elements[i].first == c && elements[i].second == v)
		{
			found = true;
			elements[i] = elements[nrElements - 1];
			nrElements--; 
			break;
		}
	}
	return found;
}


int FixedCapBiMap::size() const {
	return nrElements;
}

bool FixedCapBiMap::isEmpty() const{
	if (nrElements == 0)
		return true;
	return false;
}

bool FixedCapBiMap::isFull() const {
	if (nrElements == capacity)
		return true;
	return false;
}

FixedCapBiMapIterator FixedCapBiMap::iterator() const {
	return FixedCapBiMapIterator(*this);
}



