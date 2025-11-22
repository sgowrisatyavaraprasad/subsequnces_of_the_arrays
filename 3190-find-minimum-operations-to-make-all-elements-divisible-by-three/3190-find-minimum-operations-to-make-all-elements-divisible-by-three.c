int minimumOperations(int* nums, int numsSize) {
    int c = 0;
    for(int i = 0; i < numsSize; i++){
        if(nums[i] == 1){
            if((nums[i] - 1) % 3 == 0){
                c++;
            }
        }
        else{
            if(nums[i] % 3 != 0){
                if((nums[i] - 1) % 3 == 0){
                    c++;
                }
                else if((nums[i] + 1) % 3 == 0){
                    c++;
                }
            }
        }
    }
    return c;
}