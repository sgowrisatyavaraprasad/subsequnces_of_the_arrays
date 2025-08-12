#include<bits/stdc++.h>
using namespace std;
void subseq(vector<int>&arr , int index , int n , vector<int>&sum){
	if(index == n){
		for(int i = 0; i < sum.size(); i++){
			cout << sum[i] << " ";
		}
		cout << endl;
		return;
	}
	sum.push_back(arr[index]);
	subseq(arr , index+1 , n , sum);
	sum.pop_back();
	
	subseq(arr , index+1 , n , sum);
}
int main(){
	int n; 
	cin >> n;
	vector<int>arr(n);
	for(int i = 0; i < n; i++){
		cin >> arr[i];
	}
	vector<int>sum;
	subseq(arr , 0 , n , sum);
}