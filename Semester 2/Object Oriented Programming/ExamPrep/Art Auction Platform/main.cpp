#include "AdministratorWindow.h"
#include <QtWidgets/QApplication>

#include "UserRepository.h"
#include "ItemsRepository.h"
#include "Service.h"
#include "CollectorWindow.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    UserRepository users{ "users.txt" };
    ItemsRepository items{ "items.txt" };
    
    Service service{ users, items };

    vector<AdministratorWindow*> admins;
    vector<CollectorWindow*> collectors;

    for (auto& user : users.getAll())
        if (user.getType() == "administrator")
            admins.push_back(new AdministratorWindow{ service, user.getName() });
        else
            collectors.push_back(new CollectorWindow{ service, user.getName() });


    for (auto& window : admins) 
    {
        service.addObserver(window);
        window->show();
    }

    for (auto& window : collectors)
    {
        service.addObserver(window);
        window->show();
    }

    return a.exec();
}
