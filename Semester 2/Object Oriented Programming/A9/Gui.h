#include <QMainWindow>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QSpinBox>
#include <QListWidget>
#include "AdminService.h"
#include "UserService.h"

class GUI : public QObject
{
    Q_OBJECT

private:
    AdminService adminService;
    UserService userService;
    int argumentCount;
    char** argumentVector;
    int userIndex = 0;
    bool userShoppingBasketIsDefault = true;
    std::vector<TrenchCoat> filteredList;

    QLabel* userSizeLabel;
    QLabel* userColourLabel;
    QLabel* userPriceLabel;
    QLabel* userQuantityLabel;
    QLabel* userLinkLabel;
    QLabel* totalPriceBasket;
    QLabel* shoppingBasketType;

public:
    GUI(AdminService initial_adminService, UserService initial_userService, int initialArgumentCount = 0, char** initialArgumentVector = nullptr);
    ~GUI();
    int startScreen();
    int printAdminMenu();
    int printUserMenu();
    int runUser();
    int add();
    int remove();
    int update();
    int printCoats();
    void displayError(const char* message);

private slots:
    void on_addButton_clicked();
    void on_removeButton_clicked();
    void on_updateButton_clicked();
    void handleUserMode();
    void handleAdminMode();
    void nextButtonClicked();
    void buyButtonClicked();
    void shoppingBasketButtonClicked();
    void saveShoppingBasketButtonClicked();
    void openShoppingBasketButtonClicked();
    void changeFileTypeButtonClicked();

    
};
