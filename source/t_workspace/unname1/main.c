/***Generate by EveIDE_LIGHT at 2022-05-13 13:49:35***/
/****************V0.0.3******************/
#define N 6
int partition(int arr[], int low, int high){
    int key;
    key = arr[low];
    while(low<high){
        while(low <high && arr[high]>= key )
            high--;
        if(low<high)
            arr[low++] = arr[high];
        while( low<high && arr[low]<=key )
            low++;
        if(low<high)
            arr[high--] = arr[low];
    }
    arr[low] = key;
    return low;
}
void quick_sort(int arr[], int start, int end){
    int pos;
    if (start<end){
        pos = partition(arr, start, end);
        quick_sort(arr,start,pos-1);
        quick_sort(arr,pos+1,end);
    }
    return;
}
int main(void){
    int i;
    int arr[N]={32,12,7, 78, 23,45};

    quick_sort(arr,0,N-1);

    return 0;
}