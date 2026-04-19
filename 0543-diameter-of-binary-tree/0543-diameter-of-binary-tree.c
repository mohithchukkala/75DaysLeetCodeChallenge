/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int max(int maxi,int out){
    if(maxi>out){
        return maxi;
    }
    return out;
}
int helperh(struct TreeNode* root,int * maxi)
{
    if(root==NULL){
        return 0;
    }
    int lh=helperh(root->left,maxi);
    int rh=helperh(root->right,maxi);

    int ans=max(*maxi,lh+rh);
    *maxi=ans;
    if(lh>rh){
        return 1+lh;
    }
    return 1+rh;

    return *maxi;
}
int diameterOfBinaryTree(struct TreeNode* root) {
    int maxi=0;
    helperh(root,&maxi);
    return maxi;
}