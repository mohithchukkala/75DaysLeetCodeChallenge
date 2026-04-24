#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define ALPHABET_SIZE 26

typedef struct TrieNode {
    struct TrieNode* children[ALPHABET_SIZE];
    bool isEndOfWord;
} TrieNode;

typedef struct {
    TrieNode* root;
} Trie;

TrieNode* createNode() {
    TrieNode* node = (TrieNode*)malloc(sizeof(TrieNode));
    for (int i = 0; i < ALPHABET_SIZE; i++) {
        node->children[i] = NULL;
    }
    node->isEndOfWord = false;
    return node;
}

Trie* trieCreate() {
    Trie* trie = (Trie*)malloc(sizeof(Trie));
    trie->root = createNode();
    return trie;
}

void trieInsert(Trie* obj, char* word) {
    TrieNode* curr = obj->root;
    for (int i = 0; word[i]; i++) {
        int index = word[i] - 'a';
        if (!curr->children[index]) {
            curr->children[index] = createNode();
        }
        curr = curr->children[index];
    }
    curr->isEndOfWord = true;
}

bool trieSearch(Trie* obj, char* word) {
    TrieNode* curr = obj->root;
    for (int i = 0; word[i]; i++) {
        int index = word[i] - 'a';
        if (!curr->children[index]) return false;
        curr = curr->children[index];
    }
    return curr->isEndOfWord;
}

bool trieStartsWith(Trie* obj, char* prefix) {
    TrieNode* curr = obj->root;
    for (int i = 0; prefix[i]; i++) {
        int index = prefix[i] - 'a';
        if (!curr->children[index]) return false;
        curr = curr->children[index];
    }
    return true;
}

void freeNode(TrieNode* node) {
    if (!node) return;
    for (int i = 0; i < ALPHABET_SIZE; i++) {
        freeNode(node->children[i]);
    }
    free(node);
}

void trieFree(Trie* obj) {
    freeNode(obj->root);
    free(obj);
}
