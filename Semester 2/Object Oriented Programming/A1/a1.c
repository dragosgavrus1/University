#include <stdio.h>

int greatest_common_divisor(int number1, int number2)
{
	// Findinng the gcd of two given numbers
	if (number1 == number2)
		return number1;
	if (number1 > number2)
		return greatest_common_divisor(number1 - number2, number2);
	return greatest_common_divisor(number1, number2 - number1);
}

void smaller_relatively_prime_numbers(int number)
{
	// Going trough all smaller numbers than a given number and checking if they are relatively prime (gcd is 1)
	for (int i = 1; i < number; i++)
	{
		int gcd = greatest_common_divisor(i, number);
		if (gcd == 1)
		{
			printf("%d ", i);
		}
	}
}

void all_relatively_prime_numbers_to_a_natural_number()
{
	int number;
	printf("Number n: ");
	scanf("%d", &number);
	smaller_relatively_prime_numbers(number);
	printf("\n");

}

void printElementsOfMaxSumSubsequence(int max_starting_index, int max_ending_index, int vector[20])
{
	// Printing the elements of the maximum sum
	for (int i = max_starting_index; i <= max_ending_index; i++)
	{
		printf("%d ", vector[i]);
	}
	printf("\n");
}

void findingTheIndexesOfLongestSubsequenceWithMaxSum(int number_of_elements, int vector[])
{

	// Finding the longest subsenquence wuth maximum sum of the given array
	int starting_index = 1, sum = 0;
	int max_starting_index = 1, max_ending_index = 1, max_sum = -1000;

	for (int i = 1; i <= number_of_elements; i++)
	{
		sum += vector[i];
		if (sum > max_sum)
		{
			max_sum = sum;
			max_starting_index = starting_index;
			max_ending_index = i;
		}
		if (sum < 0)
		{
			sum = 0;
			starting_index = i + 1;
		}

	}
	printElementsOfMaxSumSubsequence(max_starting_index, max_ending_index, vector);

}


void read_array()
{
	// Reading an array with a given number of elements
	int number_of_elements;
	int vector[20];
	printf("Number of elements: ");
	scanf("%d", &number_of_elements);
	printf("Numbers: ");
	for (int i = 1; i <= number_of_elements; i++)
	{
		scanf("%d", &vector[i]);
	}

	findingTheIndexesOfLongestSubsequenceWithMaxSum(number_of_elements, vector);
}



int main()
{
	int choice = -1;
	printf("1. All smaller numbers relatively prime to n \n");
	printf("2. Longest contiguous subsequence with the maximum sum \n");
	printf("0. Exit\n");
	while (choice != 0)
	{
		printf("Option: ");
		scanf("%d", &choice);
		if (choice == 1)
			all_relatively_prime_numbers_to_a_natural_number();
		else if (choice == 2)
			read_array();
		else
			printf("Wrong input \n");
	}
	
	return 0;

}
