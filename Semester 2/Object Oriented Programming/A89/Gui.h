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

public:
    GUI(AdminService initial_adminService, UserService initial_userService, int initialArgumentCount = 0, char** initialArgumentVector = nullptr);
    int startScreen();
    int printAdminMenu();
    int printUserMenu();
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
    
};
