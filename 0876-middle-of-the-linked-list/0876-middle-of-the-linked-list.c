/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    struct ListNode* temp;
    temp=head;
    int len=0,i=0;
    while(temp!=NULL){
        len++;
        temp=temp->next;
    }
    temp=head;
    while(i<(len/2)){
        temp=temp->next;
        i++;
    }
    return temp;

}