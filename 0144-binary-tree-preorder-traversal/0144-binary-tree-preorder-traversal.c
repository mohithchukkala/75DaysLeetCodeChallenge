/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void helper(struct TreeNode* root,int *arr,int* index)
{
    if(root==NULL){
        return;
    }
    arr[(*index)++]=root->val;
    helper(root->left,arr,index);
    helper(root->right,arr,index);
}
int* preorderTraversal(struct TreeNode* root, int* returnSize) {
    int *arr=(int*)malloc(100*sizeof(int));
    int index=0;
    helper(root,arr,&index);
    *returnSize=index;
    return arr;
}