#pragma once

template <typename T>
class DynamicVector
{
private:
	int capacity, size;
	T* elements;

	void resize();

public:
	DynamicVector(int initial_capacity = 10);
	~DynamicVector();
	DynamicVector(const DynamicVector& dynamicVectorToCopy);
	DynamicVector& operator=(const DynamicVector& dynamicVector);
	void addElement(const T& element);
	void removeElement(int index);
	void updateElement(int indexOfItemToUpdate, T updatedItem);
	int getSize();
	T getElement(int position);
	int findPositionOfElement(T element);

};

template<typename T>
inline DynamicVector<T>::DynamicVector(int initial_capacity) : capacity{ initial_capacity }, size{ 0 }
{
	this->elements = new T[this->capacity];
}

template<typename T>
inline DynamicVector<T>::~DynamicVector()
{
	delete[] this->elements;
}

template<typename T>
inline DynamicVector<T>::DynamicVector(const DynamicVector& dynamicVectorToCopy)
{

	this->capacity = dynamicVectorToCopy.capacity;
	this->size = dynamicVectorToCopy.size;
	this->elements = new T[this->capacity];
	for (int i = 0; i < this->size; i++)
		this->elements[i] = dynamicVectorToCopy.elements[i];

}

template<typename T>
inline DynamicVector<T>& DynamicVector<T>::operator=(const DynamicVector<T>& dynamicVector)
{
	this->size = dynamicVector.size;
	this->capacity = dynamicVector.capacity;

	delete[] this->elements;
	this->elements = new T[this->capacity];

	for (int i = 0; i < this->size; i++)
		this->elements[i] = dynamicVector.elements[i];

	return *this;
}

template<typename T>
inline void DynamicVector<T>::resize()
{
	int auxiliar_capacity = this->capacity * 2;
	T* auxiliar_elements = new T[auxiliar_capacity];
	if (auxiliar_elements == nullptr)
		return;

	this->capacity = auxiliar_capacity;
	for (int i = 0; i < this->size; i++)
		auxiliar_elements[i] = this->elements[i];
	delete[] this->elements;
	this->elements = auxiliar_elements;
}

template<typename T>
inline void DynamicVector<T>::addElement(const T& element)
{
	if (this->size == this->capacity)
		this->resize();

	this->elements[this->size] = element;
	this->size++;
}

template<typename T>
inline void DynamicVector<T>::removeElement(int index)
{
	if (index<0 || index>this->size)
		return;
	T* auxiliar_elements = new T[this->capacity];
	for (int i = 0; i < index; i++)
		auxiliar_elements[i] = this->elements[i];

	for (int i = index; i < this->size-1; i++)
		auxiliar_elements[i] = this->elements[i + 1];

	delete[] this->elements;
	this->elements = auxiliar_elements;
	this->size--;
}

template<typename T>
inline void DynamicVector<T>::updateElement(int indexOfItemToUpdate, T updatedItem)
{
	this->elements[indexOfItemToUpdate] = updatedItem;
}

template<typename T>
inline int DynamicVector<T>::getSize()
{
	return this->size;
}

template<typename T>
inline T DynamicVector<T>::getElement(int position)
{
	return this->elements[position];
}

template<typename T>
inline int DynamicVector<T>::findPositionOfElement(T element)
{
	for (int i = 0; i < this->size; i++)
		if (element == this->elements[i])
			return i;
	return -1;
}





