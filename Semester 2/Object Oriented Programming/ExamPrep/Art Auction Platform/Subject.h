#pragma once

#include <vector>

#include "Observer.h"

using std::vector;

class Subject
{
private:
	vector<Observer*> observers;

public:
	void addObserver(Observer* observerToAdd);
	void notify();
};

