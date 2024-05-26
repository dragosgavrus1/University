#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_A9.h"
#include "AdminService.h"
#include "UserService.h"
#include "CsvShoppingBasket.h"
#include "HtmlShoppingBasket.h"

class A9 : public QMainWindow
{
    Q_OBJECT

public:
    A9(QWidget *parent = nullptr);
    ~A9();

private:
    Ui::A9Class ui;
    AdminService adminService;
    UserService userService;

public slots:
    void userMode();
    void adminMode();

};
