#include "HtmlShoppingBasket.h"
#include "Exception.h"
#include <Windows.h>

void HtmlShoppingBasket::writeToFile()
{
	std::ofstream outStream{ filename };
	if (!outStream.is_open())
		throw std::runtime_error{ "File is not opened!" };
	outStream << "<!DOCTYPE html>\n"
		<< "<html>\n"
		<< "	<head>\n"
		<< "		<title> Shopping Basket </title>\n"
		<< "	</head>\n"
		<< "<body>\n"
		<< "	<table border = ""1"">\n"
		<< "		<tr>\n"
		<< "			<td>" << "Size" << "</td>" << std::endl
		<< "			<td>" << "Colour" << "</td>" << std::endl
		<< "			<td>" << "Price" << "</td>" << std::endl
		<< "			<td>" << "Quantity" << "</td>" << std::endl
		<< "			<td>" << "Link" << "</td>" << std::endl
		<< "		</tr>" << std::endl;
	for (auto& coat : coats)
	{
		outStream<< "<tr>\n"
			<< "	<td>" << coat.getSize() << "</td>" << std::endl
			<< "	<td>" << coat.getColour() << "</td>" << std::endl
			<< "	<td>" << coat.getPrice() << "</td>" << std::endl
			<< "	<td>" << coat.getQuantity() << "</td>" << std::endl
			<< "	<td>" << "<a href=\"" << coat.getLink() << "\">" << "Link" << "</a>" << "</td>" << std::endl
			<< "</tr>" << std::endl;
	}
	outStream << "</table>\n"
		<< "</body>\n"
		<< "</html>\n";
	outStream.close();
}

void HtmlShoppingBasket::displayShoppingBasket()
{
	char buffer[MAX_PATH];
	GetCurrentDirectoryA(MAX_PATH, buffer);
	std::string path(buffer);
	path += "\\" + filename;
	std::string command = "start \"\" \"" + path + "\"";
	system(command.c_str());
}
