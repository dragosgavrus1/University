#pragma once
#include <stdlib.h>
//DO NOT INCLUDE SETITERATOR

//DO NOT CHANGE THIS PART
#define NULL_TELEM -111111
typedef int TElem;
class SetIterator;

class Set {
	//DO NOT CHANGE THIS PART
	friend class SetIterator;

    private:
        int capacity;        // Capacity of the hashtable
        int nrElems;         // Number of elements in the set
        TElem* elements;     // Array to store the elements
        bool* deleted;       // Array to mark deleted slots

        // Hash functions
        int hashFunction1(TElem elem) const {
            return abs(elem) % capacity;
        }

        int hashFunction2(TElem elem) const {
            int h = abs(elem) % (capacity - 1) + 1;
            if (h % 2 == 0) {
                // Make sure h is odd
                h += 1;
            }
            return h;
        }

        void resize();

    public:
        //implicit constructor
        Set();

        //adds an element to the set
		//returns true if the element was added, false otherwise (if the element was already in the set and it was not added)
        bool add(TElem e);

        //removes an element from the set
		//returns true if e was removed, false otherwise
        bool remove(TElem e);

        //checks whether an element belongs to the set or not
        bool search(TElem elem) const;

        //returns the number of elements;
        int size() const;

        //check whether the set is empty or not;
        bool isEmpty() const;

        //return an iterator for the set
        SetIterator iterator() const;

        // destructor
        ~Set();

};





