#include "CollectorWindow.h"
#include "StringOperations.h"

#include <QMessageBox>

CollectorWindow::CollectorWindow(Service& service, string userName, QWidget* parent)
	: QWidget(parent), service{ service }, userName{ userName }, lastSelectedItem{ nullptr }
{
	ui.setupUi(this);

	this->setWindowTitle(QString::fromStdString(userName));

	this->populateItemsList(service.getAllItems());
	this->populateComboBox();

	connectSignals();
}


void CollectorWindow::connectSignals()
{
	connect(ui.categoriesComboBox, &QComboBox::currentTextChanged,
		this, &CollectorWindow::handleCategorySelection);

	connect(ui.itemsList, &QListWidget::clicked,
		this, &CollectorWindow::handleItemSelection);

	connect(ui.bidButton, &QPushButton::clicked,
		this, &CollectorWindow::handleBid);
}


void CollectorWindow::update()
{
	this->populateItemsList(this->service.getAllItems());
	this->populateComboBox();

	if (lastSelectedItem != nullptr)
		populateOffersList(service.getItemOffers(*lastSelectedItem));
}


void CollectorWindow::populateItemsList(vector<Item> itemsToPopulate)
{
	ui.itemsList->clear();

	for (auto& item : itemsToPopulate)
	{
		QListWidgetItem* currentItem = new QListWidgetItem{ QString::fromStdString(item.toString()) };

		ui.itemsList->addItem(currentItem);
	}
}


void CollectorWindow::populateComboBox()
{
	ui.categoriesComboBox->clear();

	ui.categoriesComboBox->addItem("All");

	set<string> allCategories = this->service.getAllCategories();

	for (auto& category : allCategories)
	{
		ui.categoriesComboBox->addItem(QString::fromStdString(category));
	}
}


void CollectorWindow::populateOffersList(vector<Offer> offersToPopulate)
{
	ui.offersList->clear();

	for (auto& offer : offersToPopulate)
	{
		QListWidgetItem* currentOffer = new QListWidgetItem{ QString::fromStdString(offer.toString()) };
		ui.offersList->addItem(currentOffer);
	}
}


void CollectorWindow::handleCategorySelection()
{
	string requiredCategory = ui.categoriesComboBox->currentText().toStdString();

	if (requiredCategory == "")
		return;

	this->populateItemsList(service.getAllItemsFromCategory(requiredCategory));
	ui.offersList->clear();
}


void CollectorWindow::handleItemSelection()
{
	string selectedItem = ui.itemsList->selectedItems().at(0)->text().toStdString();
	string itemName = splitString(selectedItem, ' | ')[0];

	Item& requiredItem = service.getItemByName(itemName);
	lastSelectedItem = &requiredItem;

	this->populateOffersList(service.getItemOffers(requiredItem));
}


void CollectorWindow::handleBid()
{
	if (ui.itemsList->selectedItems().size() == 0)
	{
		QMessageBox alert;
		alert.setText("Please select an item!");
		alert.exec();
	}

	string selectedItem = ui.itemsList->selectedItems().at(0)->text().toStdString();
	string itemName = splitString(selectedItem, ' | ')[0];

	int bidValue = ui.bidInput->text().toInt();

	try
	{
		service.updateCurrentPriceForItem(this->userName, itemName, bidValue);
	}

	catch (std::exception& e)
	{
		QMessageBox alert;
		alert.setText(e.what());
		alert.exec();
	}
}


CollectorWindow::~CollectorWindow()
{}