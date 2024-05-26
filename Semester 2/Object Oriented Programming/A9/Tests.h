#pragma once

class Tests
{
public:

	Tests();

	void testAll();
	void TestService_Add_Valid();
	void TestService_Add_Invalid();
	void TestService_Remove_Valid();
	void TestService_Remove_Invalid();
	void TestService_Update_Valid();
	void TestService_Update_Invalid();
};