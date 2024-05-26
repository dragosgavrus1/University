#include "AdministratorWindow.h"

#include "StringOperations.h"

#include <QMessageBox>


AdministratorWindow::AdministratorWindow(Service& service, string userName, QWidget* parent)
    : QWidget(parent), service{ service }, userName{ userName }
{
    ui.setupUi(this);

    this->connectSignals();
    this->setWindowTitle(QString::fromStdString(userName));

    this->populateItemsList(this->service.getAllItems());
    this->populateComboBox();
}


void AdministratorWindow::connectSignals()
{
    connect(ui.categoriesComboBox, &QComboBox::currentTextChanged,
        this, &AdministratorWindow::handleCategorySelection);

    connect(ui.addItemButton, &QPushButton::clicked,
        this, &AdministratorWindow::addItem);

    connect(ui.itemsList, &QListWidget::clicked,
        this, &AdministratorWindow::handleItemSelection);
}



void AdministratorWindow::populateItemsList(vector<Item> itemsToPopulate)
{
    ui.itemsList->clear();

    for (auto& item : itemsToPopulate)
    {
        QListWidgetItem* currentItem = new QListWidgetItem{QString::fromStdString(item.toString()) };

        ui.itemsList->addItem(currentItem);
    }
}

void AdministratorWindow::populateComboBox()
{
    ui.categoriesComboBox->clear();

    ui.categoriesComboBox->addItem("All");

    set<string> allCategories = this->service.getAllCategories();

    for (auto& category : allCategories)
    {
        ui.categoriesComboBox->addItem(QString::fromStdString(category));
    }
}

void AdministratorWindow::populateOffersList(vector<Offer> offersToPopulate)
{
    ui.offersList->clear();

    for (auto& offer : offersToPopulate)
    {
        QListWidgetItem* currentOffer = new QListWidgetItem{ QString::fromStdString(offer.toString()) };
        ui.offersList->addItem(currentOffer);
    }
}

void AdministratorWindow::update()
{
    this->populateItemsList(this->service.getAllItems());
    this->populateComboBox();
}

void AdministratorWindow::handleCategorySelection()
{
    string requiredCategory = ui.categoriesComboBox->currentText().toStdString();

    if (requiredCategory == "")
        return;

    this->populateItemsList(service.getAllItemsFromCategory(requiredCategory));
    ui.offersList->clear();
}

void AdministratorWindow::addItem()
{
    string name = ui.nameInput->text().toStdString();
    string category = ui.categoryInput->text().toStdString();
    int price = ui.priceInput->text().toInt();

    try
    {
        service.addItem(name, category, price);
    }
    catch (std::exception& e)
    {
        QMessageBox alert;
        alert.setText(e.what());
        alert.exec();
    }
}

void AdministratorWindow::handleItemSelection()
{
    string selectedItem = ui.itemsList->selectedItems().at(0)->text().toStdString();
    string itemName = splitString(selectedItem, ' | ')[0];

    Item& requiredItem = service.getItemByName(itemName);
    this->populateOffersList(service.getItemOffers(requiredItem));
}


AdministratorWindow::~AdministratorWindow()
{}
