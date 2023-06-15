#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define LIST_SIZE 10

typedef struct {
    void *object;
} ListEntry;

typedef struct {
    ListEntry *entries;
    int size;
    int capacity;
} List;

void initializeList(List *list, int initialCapacity) {
    list->entries = malloc(initialCapacity * sizeof(ListEntry));
    list->size = 0;
    list->capacity = initialCapacity;
}

void destroyList(List *list) {
    free(list->entries);
    list->size = 0;
    list->capacity = 0;
}

bool append(ListEntry entry, List *list) {
    if (list->size >= list->capacity) {
        int newCapacity = list->capacity * 2;
        ListEntry *newEntries = realloc(list->entries, newCapacity * sizeof(ListEntry));
        if (newEntries == NULL) {
            return false;  
        }
        list->entries = newEntries;
        list->capacity = newCapacity;
    }
    
    list->entries[list->size] = entry;
    list->size++;
    
    return true;
}

int main() {
    List my_list;
    initializeList(&my_list, LIST_SIZE);
    
    int intData = 42;
    ListEntry intEntry = { .object = &intData };
    append(intEntry, &my_list);
    
    return 0;