#include <bits/stdc++.h>
using namespace std;

int main()
{
	vector<int> numbers1;
	vector<int> numbers2;
	int num1, num2;
	while(cin >> num1 >> num2)
	{
		numbers1.push_back(num1);
		numbers2.push_back(num2);
	}
	
	int sum = 0;
	
	for(int i = 0; i < numbers1.size(); i++)
	{
		for(int j = 0; j < numbers2.size(); j++)
			if(numbers1[i] == numbers2[j])
				sum += numbers1[i];
	}
	
	cout << sum << endl;
	
}