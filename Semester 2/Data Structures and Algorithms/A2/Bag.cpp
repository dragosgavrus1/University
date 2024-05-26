#include "Bag.h"
#include "BagIterator.h"
#include <exception>
#include <iostream>
using namespace std;

// O(1) ; constructor
Bag::Bag() {
	this->head = nullptr;
	this->nrElems = 0;
}

// Best case: O(1) ; the element to be added is the element in the head
// Worst case: O(n) ; the elem is not in the bag yet and is added to the end
void Bag::add(TElem elem) {

	this->nrElems++;

	if (head == nullptr)
	{
		Node* ptr = new Node;
		ptr->elem = elem;
		ptr->frequency = 1;
		ptr->next = nullptr;
		head = ptr;
	}
	else
	{
		Node* temp = head;
		Node* prev = nullptr;
		while (temp != nullptr) {
			if (temp->elem == elem)
			{
				temp->frequency++;
				return;
			}
			prev = temp;
			temp = temp->next;
		}

		if (temp == nullptr)
		{
			Node* ptr = new Node;
			ptr->elem = elem;
			ptr->frequency = 1;
			ptr->next = nullptr;
			prev->next = ptr;
		}
			
	}
	
}

// Best case: O(1) ; the bag is empty and returns false
// Worst case: O(n) ; the element is not in the bag and returns false after searching the whole container
bool Bag::remove(TElem elem) {
	Node* prev = nullptr;
	Node* curr = this->head;
	while (curr != nullptr) {
		if (curr->elem == elem) {
			if (curr->frequency > 1) {
				curr->frequency--;
				this->nrElems--;
			}
			else {
				if (prev == nullptr) {
					this->head = curr->next;
				}
				else {
					prev->next = curr->next;
				}
				delete curr;
				this->nrElems--;
			}
			return true;
		}
		prev = curr;
		curr = curr->next;
	}
	return false;
}


// Best case: O(1) ; the searched element is the head
// Worst case: O(n) ; the element does not exist in the bag
bool Bag::search(TElem elem) const {

	Node* curr = this->head;
	while (curr != nullptr) {
		if (curr->elem == elem) {
			return true;
		}
		curr = curr->next;
	}
	return false; 
}

// Best case: O(1) ; the searched element is the head
// Worst case: O(n) ; the element does not exist in the bag
int Bag::nrOccurrences(TElem elem) const {

	Node* curr = this->head;
	while (curr != nullptr) {
		if (curr->elem == elem) {
			return curr->frequency;
		}
		curr = curr->next;
	}
	return 0; 
}


// O(1) ; returns the number of elements
int Bag::size() const {
	return nrElems;
}

// O(1) ; checks if bag is empty with size function 
bool Bag::isEmpty() const {
	if (this->size() == 0)
		return true;
	return false;
}

// O(1) ; iterator
BagIterator Bag::iterator() const {
	return BagIterator(*this);
}

// Best case: O(1) ; the bag is empty
// Worst case: O(n) ; the elems are not in the bag yet and are added to the end
void Bag::addOccurrences(int nr, TElem elem)
{
	if (nr < 0)
	{
		throw std::exception();
	}
	else if (nr == 0)
	{
		return;
	}
	else
	{
		this->nrElems+=nr;

		if (head == nullptr)
		{
			Node* ptr = new Node;
			ptr->elem = elem;
			ptr->frequency = nr;
			ptr->next = nullptr;
			head = ptr;
		}
		else
		{
			Node* temp = head;
			Node* prev = nullptr;
			while (temp != nullptr) {
				if (temp->elem == elem)
				{
					temp->frequency+=nr;
					return;
				}
				prev = temp;
				temp = temp->next;
			}

			if (temp == nullptr)
			{
				Node* ptr = new Node;
				ptr->elem = elem;
				ptr->frequency = nr;
				ptr->next = nullptr;
				prev->next = ptr;
			}

		}
	}
}

// O(n) ; deletes all the elements
Bag::~Bag() {
	while (this->head != nullptr)
	{
		Node* aux = this->head;
		this->head = this->head->next;
		delete aux;
	}
}

