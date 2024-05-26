#pragma once

#include <QtWidgets/QWidget>
#include "ui_AdministratorWindow.h"

#include <string>

#include "Observer.h"
#include "Service.h"

using std::string;

class AdministratorWindow : public QWidget, public Observer
{
    Q_OBJECT

public:
    AdministratorWindow(Service& service, string userName, QWidget *parent = nullptr);
    ~AdministratorWindow();

    void connectSignals();

    void populateItemsList(vector<Item> itemsToPopulate);
    void populateComboBox();
    void populateOffersList(vector<Offer> offersToPopulate);

    void update();

    void handleCategorySelection();
    void addItem();

    void handleItemSelection();


private:
    Ui::AdministratorWindowClass ui;
    Service& service;
    string userName;
};
