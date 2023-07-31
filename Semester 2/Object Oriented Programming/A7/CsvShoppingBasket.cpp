#include "CsvShoppingBasket.h"
#include <fstream>
#include <exception>
#include "Exception.h"
#include <Windows.h>
#include <shellapi.h>

void CsvShoppingBasket::writeToFile()
{
	std::ofstream outStream(filename);
	if(!outStream.is_open())
		throw std::runtime_error{ "File is not opened!" };
	for (const auto& currentCoat : coats)
	{
		outStream << currentCoat;
	}
	outStream.close();
}

void CsvShoppingBasket::displayShoppingBasket()
{
	ShellExecuteA(NULL,
		"open",
		"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
		filename.c_str(),
		NULL,
		SW_MAXIMIZE
	);
}
