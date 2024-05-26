#pragma once

#include <QWidget>
#include "ui_CollectorWindow.h"

#include "Observer.h"
#include "Service.h"

class CollectorWindow : public QWidget, public Observer
{
	Q_OBJECT

public:
	CollectorWindow(Service& service, string userName, QWidget *parent = nullptr);
	~CollectorWindow();

	void connectSignals();

	void update();
	void populateItemsList(vector<Item> itemsToPopulate);
	void populateComboBox();
	void populateOffersList(vector<Offer> offersToPopulate);

	void handleCategorySelection();
	void handleItemSelection();
	void handleBid();


private:
	Ui::CollectorWindowClass ui;

	Service& service;
	string userName;

	Item* lastSelectedItem;
};
