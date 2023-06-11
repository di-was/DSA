#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define TABLE_SIZE 10

typedef struct {
    char * key;
    int value;
} Entry;

typedef struct {
    Entry * entries;
} HashTable;


void initilize_hash(HashTable * array) {
    for (int i=0; i< TABLE_SIZE; i++) {
        array[i].entries = NULL;
    }
}

unsigned int  hash_value(const char * key) {
    unsigned int hash =0;
    unsigned int len = strlen(key);
    for (unsigned int i = 0; i < len; i++) {
        hash = hash * 31 + key[i];
    }
    return hash %  TABLE_SIZE;
}

bool insert_entry(HashTable * array, char key[],  int value) {
    Entry decoy;
    decoy.key = key;
    decoy.value = value;

    unsigned int hash = hash_value(key);
    array[hash].entries = &decoy;
}

bool delete_entry(HashTable * array, const char * key) {
    array[hash_value(key)].entries = NULL;
}

int printHashTable(HashTable * array) {
    for (int i=0; i < TABLE_SIZE; i++) {
        if (array[i].entries == NULL) {
            printf("%d =  %c \n", i, '_');
        } else {
            printf("%d = %s \n", i, (*array[i].entries).key);
        }
    }
    return 0;
} 

int main() {
    HashTable array[TABLE_SIZE];
    initilize_hash(array);
    
    
    return 0;
}
