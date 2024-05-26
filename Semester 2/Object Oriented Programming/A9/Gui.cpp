#include "Gui.h"
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QFormLayout>
#include <QDialog>
#include <iostream>


GUI::GUI(AdminService initial_adminService, UserService initial_userService, int initialArgumentCount, char** initialArgumentVector)
    : adminService{ initial_adminService }, userService{ initial_userService }, argumentCount{ initialArgumentCount }, argumentVector{ initialArgumentVector }
{
}

GUI::~GUI()
{
    delete[] argumentVector;
}

int GUI::startScreen()
{
    QApplication app(argumentCount, argumentVector);

    QWidget window{};
    window.setStyleSheet("background-color: lightgray; color: black;");
    window.setWindowTitle("Trench Coats");

    QVBoxLayout* layout = new QVBoxLayout{};
    QLabel* titleLabel = new QLabel("Trench Coats Application");
    titleLabel->setAlignment(Qt::AlignCenter);
    titleLabel->setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 20px;");

    QPushButton* userButton = new QPushButton("User Mode");
    QPushButton* adminButton = new QPushButton("Admin Mode");

    connect(userButton, &QPushButton::clicked, this, &GUI::printUserMenu);
    connect(adminButton, &QPushButton::clicked, this, &GUI::printAdminMenu);

    layout->addWidget(titleLabel);
    layout->addWidget(userButton);
    layout->addWidget(adminButton);

    window.setLayout(layout);
    window.resize(300, 200);
    window.show();
    return app.exec();
}

void GUI::handleUserMode()
{
    QListWidget* item = qobject_cast<QListWidget*>(QObject::sender()); // Get the clicked item
    QString txt = item->currentItem()->text();
    try {
        if (txt.startsWith("1"))
            nextButtonClicked();
        if (txt.startsWith("2"))
            buyButtonClicked();
        if (txt.startsWith("3"))
            shoppingBasketButtonClicked();
        if (txt.startsWith("4"))
            saveShoppingBasketButtonClicked();
        if (txt.startsWith("5"))
            openShoppingBasketButtonClicked();
        if (txt.startsWith("6"))
            changeFileTypeButtonClicked();
    }
    catch (std::exception& e) {

    }
}


void GUI::handleAdminMode()
{
    QListWidget* item = qobject_cast<QListWidget*>(QObject::sender()); // Get the clicked item
    QString txt = item->currentItem()->text();
    try {
        if (txt.startsWith("1"))
            add();
        if (txt.startsWith("2"))
            remove();
        if (txt.startsWith("3"))
            update();
        if (txt.startsWith("4"))
            printCoats();
    }
    catch (std::exception& e) {

    }

}


void GUI::nextButtonClicked()
{
    userIndex++;
    if (userIndex == filteredList.size())
    {
        userIndex = 0;
    }
    userSizeLabel->setText(QString("Size: ") + filteredList[userIndex].getSize().c_str());
    userColourLabel->setText(QString("Colour: ") + filteredList[userIndex].getColour().c_str());
    userPriceLabel->setText(QString("Price: ") + QString::number(filteredList[userIndex].getPrice()));
    userQuantityLabel->setText(QString("Quantity: ") + QString::number(filteredList[userIndex].getQuantity()));
    userLinkLabel->setText(QString("Link: ") + filteredList[userIndex].getLink().c_str());
}

void GUI::buyButtonClicked()
{
    userService.buyCoat(filteredList[userIndex]);
    totalPriceBasket->setText(QString("Price: ") + QString::number(userService.getTotalPrice()));
}

void GUI::shoppingBasketButtonClicked()
{
    QDialog* popup = new QDialog();
    QListWidget list{ popup };
    list.setStyleSheet("background-color: lightgray; color: black;");
    for (auto& coat : userService.getShoppingBasket()->getAllCoats())
    {
        std::string coatString = "Size: " + coat.getSize() + ", Colour: " + coat.getColour() + ", Price: " + std::to_string(coat.getPrice()) + ", Quantity: " + std::to_string(coat.getQuantity()) + ", Link: " + coat.getLink() + "\n";
        QListWidgetItem* item = new QListWidgetItem(coatString.c_str(), &list);
    }
    list.resize(1000, 700);
    list.show();
    popup->exec();
    return;
}

void GUI::saveShoppingBasketButtonClicked()
{
    userService.saveShoppingBasket();
}

void GUI::openShoppingBasketButtonClicked()
{
    userService.openShoppingBasket();
}

void GUI::changeFileTypeButtonClicked()
{
    if (this->userShoppingBasketIsDefault == true) {
        userService.setShoppingBasketType("HTML");
        userShoppingBasketIsDefault = false;
        shoppingBasketType->setText("Shopping basket file type: HTML");
    }
    else
    {
        userService.setShoppingBasketType("CSV");
        userShoppingBasketIsDefault = true;
        shoppingBasketType->setText("Shopping basket file type: CSV");
    }
}

int GUI::printAdminMenu()
{
    QDialog* popup = new QDialog();
    QWidget window{ popup };
    window.setStyleSheet("background-color: lightgray; color: black;");
    QVBoxLayout layout{};
    QListWidget list;
    QLabel title("Admin mode");
    title.setAlignment(Qt::AlignCenter);
    QListWidgetItem* element1 = new QListWidgetItem("1. Add a new coat", &list);
    QListWidgetItem* element2 = new QListWidgetItem("2. Delete a coat", &list);
    QListWidgetItem* element3 = new QListWidgetItem("3. Update a coat", &list);
    QListWidgetItem* element4 = new QListWidgetItem("4. Display all coats", &list);
    layout.addWidget(&title);
    layout.addWidget(&list);
    window.setLayout(&layout);
    window.show();
    window.resize(800, 600);
    connect(&list, &QListWidget::itemClicked, this, &GUI::handleAdminMode);
    return popup->exec();

}

int GUI::printUserMenu()
{
    QDialog* popup = new QDialog();
    QWidget window{ popup };
    window.setStyleSheet("background-color: lightgray; color: black;");
    QFormLayout* formLayout = new QFormLayout{};
    QLabel title("User mode");
    title.setAlignment(Qt::AlignCenter);
    QLabel sizeLabel("Size filter");
    QLineEdit* sizeInput = new QLineEdit();
    sizeInput->setObjectName("filter");
    sizeLabel.setBuddy(sizeInput);
    QPushButton filterButton("Filter");
    connect(&filterButton, &QPushButton::clicked, this, &GUI::runUser);
    formLayout->addRow(&title);
    formLayout->addRow(&sizeLabel, sizeInput);
    formLayout->addWidget(&filterButton);
    window.setLayout(formLayout);
    window.show();
    return popup->exec();
}

int GUI::runUser()
{

    QDialog* popup = new QDialog();
    QWidget window{ popup };
    window.setStyleSheet("background-color: lightgray; color: black;");
    QVBoxLayout layout{};
    QListWidget list;
    QLabel title("User mode");
    title.setAlignment(Qt::AlignCenter);
    std::string filter = sender()->parent()->findChild<QLineEdit*>("filter")->text().toStdString();
    filteredList = userService.getFilteredCoatList(filter);

    userSizeLabel = new QLabel(QString("Size: ") + filteredList[userIndex].getSize().c_str());
    userColourLabel = new QLabel(QString("Colour: ") + filteredList[userIndex].getColour().c_str());
    userPriceLabel = new QLabel(QString("Price: ") + QString::number(filteredList[userIndex].getPrice()));
    userQuantityLabel = new QLabel(QString("Quantity: ") + QString::number(filteredList[userIndex].getQuantity()));
    userLinkLabel = new QLabel(QString("Link: ") + filteredList[userIndex].getLink().c_str());
    totalPriceBasket = new QLabel(QString("Basket Price: ") + QString::number(0));
    shoppingBasketType = new QLabel(QString("Shopping basket file type: CSV"));

    QListWidgetItem* element1 = new QListWidgetItem("1. Next", &list);
    QListWidgetItem* element2 = new QListWidgetItem("2. Buy", &list);
    QListWidgetItem* element3 = new QListWidgetItem("3. Show basket", &list);
    QListWidgetItem* element4 = new QListWidgetItem("4. Save basket to file", &list);
    QListWidgetItem* element5 = new QListWidgetItem("5. Open basket file", &list);
    QListWidgetItem* element6 = new QListWidgetItem("6. Change basket file type", &list);
    connect(&list, &QListWidget::itemClicked, this, &GUI::handleUserMode);
    layout.addWidget(&title);
    layout.addWidget(userSizeLabel);
    layout.addWidget(userColourLabel);
    layout.addWidget(userPriceLabel);
    layout.addWidget(userQuantityLabel);
    layout.addWidget(userLinkLabel);
    layout.addWidget(totalPriceBasket);
    layout.addWidget(shoppingBasketType);
    layout.addWidget(&list);
    window.setLayout(&layout);
    window.show();
    window.resize(800, 600);
    return popup->exec();
}

int GUI::add()
{
    QDialog* popup = new QDialog();
    QWidget window{ popup };
    window.setStyleSheet("background-color: lightgray; color: black;");
    QFormLayout* formLayout = new QFormLayout{};
    QLabel label("Add a new coat");
    label.setAlignment(Qt::AlignCenter);
    QLabel sizeLabel("Size ");
    QLabel colourLabel("Colour ");
    QLabel priceLabel("Price ");
    QLabel quantityLabel("Quantity ");
    QLabel linkLabel("Link ");

    QLineEdit* sizeInput = new QLineEdit();
    sizeInput->setObjectName("size");
    sizeLabel.setBuddy(sizeInput);

    QLineEdit* colourInput = new QLineEdit();
    colourInput->setObjectName("colour");
    colourLabel.setBuddy(colourInput);

    QLineEdit* priceInput = new QLineEdit();
    priceInput->setObjectName("price");
    priceLabel.setBuddy(priceInput);

    QLineEdit* quantityInput = new QLineEdit();
    quantityInput->setObjectName("quantity");
    quantityLabel.setBuddy(quantityInput);

    QLineEdit* linkInput = new QLineEdit();
    linkInput->setObjectName("link");
    linkLabel.setBuddy(linkInput);

    formLayout->addRow(&label);
    formLayout->addRow(&sizeLabel, sizeInput);
    formLayout->addRow(&colourLabel, colourInput);
    formLayout->addRow(&priceLabel, priceInput);
    formLayout->addRow(&quantityLabel, quantityInput);
    formLayout->addRow(&linkLabel, linkInput);
    QPushButton addButton("Add");
    formLayout->addRow(&addButton);
    connect(&addButton, &QPushButton::clicked, this, &GUI::on_addButton_clicked);
    window.setLayout(formLayout);
    window.show();
    return popup->exec();

}

int GUI::remove()
{
    QDialog* popup = new QDialog();
    QWidget window{ popup };
    window.setStyleSheet("background-color: lightgray; color: black;");
    QFormLayout* formLayout = new QFormLayout{};
    QLabel label("Remove a coat");
    label.setAlignment(Qt::AlignCenter);
    QLabel sizeLabel("Size ");
    QLabel colourLabel("Colour ");

    QLineEdit* sizeInput = new QLineEdit();
    sizeInput->setObjectName("size");
    sizeLabel.setBuddy(sizeInput);
    QLineEdit* colourInput = new QLineEdit();
    colourInput->setObjectName("colour");
    colourLabel.setBuddy(colourInput);
    formLayout->addRow(&label);
    formLayout->addRow(&sizeLabel, sizeInput);
    formLayout->addRow(&colourLabel, colourInput);

    QPushButton removeBtn("Remove");
    formLayout->addRow(&removeBtn);
    connect(&removeBtn, &QPushButton::clicked, this, &GUI::on_removeButton_clicked);
    window.setLayout(formLayout);
    window.show();
    return popup->exec();
}

int GUI::update()
{
    QDialog* popup = new QDialog();
    QWidget window{ popup };
    window.setStyleSheet("background-color: lightgray; color: black;");
    QFormLayout* formLayout = new QFormLayout{};
    QLabel label("Update a coat");
    label.setAlignment(Qt::AlignCenter);

    QLabel oldSizeLabel("Old size ");
    QLabel oldColourLabel("Old colour ");
    QLabel newSizeLabel("New size ");
    QLabel newColourLabel("New colour ");
    QLabel newPriceLabel("New price ");
    QLabel newQuantityLabel("New quantity ");
    QLabel newLinkLabel("New link ");

    QLineEdit* oldSizeInput = new QLineEdit();
    oldSizeInput->setObjectName("oldSize");
    oldSizeLabel.setBuddy(oldSizeInput);
    QLineEdit* oldColourInput = new QLineEdit();
    oldColourInput->setObjectName("oldColour");
    oldColourLabel.setBuddy(oldColourInput);

    QLineEdit* newSizeInput = new QLineEdit();
    newSizeInput->setObjectName("newSize");
    newSizeLabel.setBuddy(newSizeInput);
    QLineEdit* newColourInput = new QLineEdit();
    newColourInput->setObjectName("newColour");
    newColourLabel.setBuddy(newColourInput);
    QLineEdit* newPriceInput = new QLineEdit();
    newPriceInput->setObjectName("newPrice");
    newPriceLabel.setBuddy(newPriceInput);
    QLineEdit* newQuantityInput = new QLineEdit();
    newQuantityInput->setObjectName("newQuantity");
    newQuantityLabel.setBuddy(newQuantityInput);
    QLineEdit* newLinkInput = new QLineEdit();
    newLinkInput->setObjectName("newLink");
    newLinkLabel.setBuddy(newLinkInput);

    formLayout->addRow(&label);
    formLayout->addRow(&oldSizeLabel, oldSizeInput);
    formLayout->addRow(&oldColourLabel, oldColourInput);
    formLayout->addRow(&newSizeLabel, newSizeInput);
    formLayout->addRow(&newColourLabel, newColourInput);
    formLayout->addRow(&newPriceLabel, newPriceInput);
    formLayout->addRow(&newQuantityLabel, newQuantityInput);
    formLayout->addRow(&newLinkLabel, newLinkInput);

    QPushButton updateBtn("Update");
    formLayout->addRow(&updateBtn);
    connect(&updateBtn, &QPushButton::clicked, this, &GUI::on_updateButton_clicked);
    window.setLayout(formLayout);
    window.show();
    return popup->exec();
}

int GUI::printCoats()
{
    QDialog* popup = new QDialog();
    QListWidget list{ popup };
    list.setStyleSheet("background-color: lightgray; color: black;");
    for (auto& coat : adminService.getAllCoats())
    {
        std::string coatString = "Size: " + coat.getSize() + ", Colour: " + coat.getColour() + ", Price: " + std::to_string(coat.getPrice()) + ", Quantity: " + std::to_string(coat.getQuantity()) + ", Link: " + coat.getLink() + "\n";
        QListWidgetItem* item = new QListWidgetItem(coatString.c_str(), &list);
    }
    list.resize(1000, 700);
    list.show();
    return popup->exec();
}

void GUI::displayError(const char* message)
{
    if (strcmp(message, "invalid stoi argument") == 0)
        message = "Invalid input";
    QDialog* popup = new QDialog();
    QLabel label(message, popup);
    popup->setStyleSheet("background-color: lightgray; color: black;");
    label.setAlignment(Qt::AlignCenter);
    label.setFont(QFont("Courier", 15, 10));
    label.resize(300, 200);
    label.show();
    popup->exec();
}


void GUI::on_addButton_clicked()
{
    std::string size = sender()->parent()->findChild<QLineEdit*>("size")->text().toStdString();
    std::string colour = sender()->parent()->findChild<QLineEdit*>("colour")->text().toStdString();
    std::string price = sender()->parent()->findChild<QLineEdit*>("price")->text().toStdString();
    std::string quantity = sender()->parent()->findChild<QLineEdit*>("quantity")->text().toStdString();
    std::string link = sender()->parent()->findChild<QLineEdit*>("link")->text().toStdString();

    try
    {
        bool result = adminService.addToService(size, colour, stoi(price), stoi(quantity), link);
        std::cout << "Successful add\n";

    }
    catch (const std::exception& e)
    {
        displayError(e.what());
        QWidget* parentWindow = qobject_cast<QWidget*>(sender()->parent());
        parentWindow->close();
    }
    QWidget* parentWindow = qobject_cast<QWidget*>(sender()->parent()->parent());
    parentWindow->close();
}

void GUI::on_removeButton_clicked()
{
    std::string size = sender()->parent()->findChild<QLineEdit*>("size")->text().toStdString();
    std::string colour = sender()->parent()->findChild<QLineEdit*>("colour")->text().toStdString();
    try
    {
        adminService.removeFromService(size, colour);

    }
    catch (const std::exception& e)
    {
        displayError(e.what());
        QWidget* parentW = qobject_cast<QWidget*>(sender()->parent());
        parentW->close();
    }
    QWidget* parentW = qobject_cast<QWidget*>(sender()->parent()->parent());
    parentW->close();
}

void GUI::on_updateButton_clicked()
{
    std::string oldSize = sender()->parent()->findChild<QLineEdit*>("oldSize")->text().toStdString();
    std::string oldColour = sender()->parent()->findChild<QLineEdit*>("oldColour")->text().toStdString();
    std::string newSize = sender()->parent()->findChild<QLineEdit*>("newSize")->text().toStdString();
    std::string newColour = sender()->parent()->findChild<QLineEdit*>("newColour")->text().toStdString();
    std::string newPrice = sender()->parent()->findChild<QLineEdit*>("newPrice")->text().toStdString();
    std::string newQuantity = sender()->parent()->findChild<QLineEdit*>("newQuantity")->text().toStdString();
    std::string newLink = sender()->parent()->findChild<QLineEdit*>("newLink")->text().toStdString();
    try {
        adminService.updateToService(oldSize, oldColour, newSize, newColour, std::stoi(newPrice), std::stoi(newQuantity), newLink);
    }
    catch (std::exception& e)
    {
        displayError(e.what());
        QWidget* parentW = qobject_cast<QWidget*>(sender()->parent());
        parentW->close();
    }
    QWidget* parentWidget = qobject_cast<QWidget*>(sender()->parent()->parent());
    parentWidget->close();
}
