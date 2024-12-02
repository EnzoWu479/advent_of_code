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
	
	sort(numbers1.begin(), numbers1.end());
	sort(numbers2.begin(), numbers2.end());
	
	int sum = 0;
	
	for(int i = 0; i < numbers1.size(); i++)
	{
		int value = numbers1[i] - numbers2[i];
		if(value < 0)
			value *= -1;
		sum += value;
	}
	
	cout << sum << endl;
	
}