#include <iostream>
#include <string>
#include <cstring>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

int main() {
    int clientSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (clientSocket == -1) {
        std::cerr << "Failed to create socket" << std::endl;
        return 1;
    }

    sockaddr_in serverAddress{};
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_port = htons(8888);
    if (inet_pton(AF_INET, "127.0.0.1", &(serverAddress.sin_addr)) <= 0) {
        std::cerr << "Invalid address/Address not supported" << std::endl;
        return 1;
    }

    if (connect(clientSocket, (struct sockaddr*)&serverAddress, sizeof(serverAddress)) < 0) {
        std::cerr << "Connection failed" << std::endl;
        return 1;
    }

    char buffer[1024];
    while (true) {
        memset(buffer, 0, sizeof(buffer));
        ssize_t bytesRead = recv(clientSocket, buffer, sizeof(buffer), 0);
        if (bytesRead <= 0) {
            std::cerr << "Failed to receive data" << std::endl;
            break;
        }
        std::string data(buffer);
        std::cout << data << std::endl;
        if (data.find("The game is starting") != std::string::npos) {
            break;
        }
    }

    char table[30];
    while (true) {
        memset(buffer, 0, sizeof(buffer));
        ssize_t bytesRead = recv(clientSocket, buffer, sizeof(buffer), 0);
        if (bytesRead <= 0) {
            std::cerr << "Failed to receive data" << std::endl;
            break;
        }
        std::string data(buffer);
        std::cout << data << std::endl;
        if (data.find("Your turn") != std::string::npos) {
            std::string position;
            std::cout << "Enter your move (0-8): ";
            std::cin >> position;
            memset(table, 0, sizeof(table));
            send(clientSocket, position.c_str(), position.size(), 0);
            ssize_t bytesRead = recv(clientSocket,table, 30*sizeof(char), 0);
            std::string data(table);
            std::cout << data << std::endl;
        }
        if (data.find("wins!") != std::string::npos || data.find("It's a draw") != std::string::npos) {
            break;
        }
    }

    close(clientSocket);

    return 0;
}