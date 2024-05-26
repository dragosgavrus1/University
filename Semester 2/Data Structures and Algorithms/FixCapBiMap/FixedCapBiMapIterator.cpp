#include "FixedCapBiMap.h"
#include "FixedCapBiMapIterator.h"
#include <exception>
using namespace std;


FixedCapBiMapIterator::FixedCapBiMapIterator(const FixedCapBiMap& d) : map(d)
{
	//TODO - Implementation
	this->index = 0;
}


void FixedCapBiMapIterator::first() {
	this->index = 0;
}


void FixedCapBiMapIterator::next() {
	if (valid() == true)
		this->index++;
	else
		throw std::exception();
}


TElem FixedCapBiMapIterator::getCurrent(){
	if (valid() == true)
		return map.elements[index];
	else
		throw std::exception();
}


bool FixedCapBiMapIterator::valid() const {
	if (this->index < this->map.nrElements)
		return true;
	return false;
}



