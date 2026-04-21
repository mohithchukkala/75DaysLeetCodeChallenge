#include <stdio.h>
#include <stdlib.h>

struct QueueNode {
    struct TreeNode *node;
    int level;
};

int** levelOrder(struct TreeNode* root, int* returnSize, int** returnColumnSizes) {
    if (!root) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }

    struct QueueNode queue[2000];
    int front = 0, rear = 0;
    queue[rear++] = (struct QueueNode){root, 0};

    int** result = (int**)malloc(sizeof(int*) * 2000);
    *returnColumnSizes = (int*)malloc(sizeof(int) * 2000);
    int counts[2000] = {0};
    *returnSize = 0;

    while (front < rear) {
        struct QueueNode qn = queue[front++];
        struct TreeNode* node = qn.node;
        int level = qn.level;

        if (counts[level] == 0) {
            result[level] = (int*)malloc(sizeof(int) * 2000);
            (*returnColumnSizes)[level] = 0;
            (*returnSize)++;
        }

        result[level][counts[level]++] = node->val;
        (*returnColumnSizes)[level]++;

        if (node->left) queue[rear++] = (struct QueueNode){node->left, level + 1};
        if (node->right) queue[rear++] = (struct QueueNode){node->right, level + 1};
    }

    return result;
}
