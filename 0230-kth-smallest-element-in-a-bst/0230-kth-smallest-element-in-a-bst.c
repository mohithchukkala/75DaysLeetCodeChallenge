int kthSmallest(struct TreeNode* root, int k) {
    struct TreeNode* stack[2000];
    int top = -1;
    struct TreeNode* curr = root;
    while (curr || top >= 0) {
        while (curr) {
            stack[++top] = curr;
            curr = curr->left;
        }
        curr = stack[top--];
        if (--k == 0) return curr->val;
        curr = curr->right;
    }
    return -1;
}
