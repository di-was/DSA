#include <stdio.h>
#include <string.h>


void get_address_of_indexes(int * pArray, int total_elements) {
    for (int i=0; i < total_elements; i++) {
        int * memory_address = pArray + sizeof(*pArray) * i;
        printf("The address of index %d is %p  \n", i, memory_address);
    }
}

int main() {
    int array[10] = {1 , 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int total_elements = sizeof(array)/sizeof(*array);

    get_address_of_indexes(array, total_elements);
    return 0;
}