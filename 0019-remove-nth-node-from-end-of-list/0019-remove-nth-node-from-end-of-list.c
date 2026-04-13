/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode* temp=head;
    struct ListNode* prev=NULL;
    if(head==NULL){
        return head;
    }
    if(head->next==NULL && n==1){
        return NULL;
    }
    int count=0;
    while(temp!=NULL){
        count++;
        temp=temp->next;
    }
    temp=head;
    if(n==count && temp->next!=NULL){
        struct ListNode* temp1=head;
        head=head->next;
        free(temp1);
        return head;
    }
    int i=0;
    temp=head;
    while(i<count-n && temp!=NULL){
        prev=temp;
        temp=temp->next;
        i++;
    }
    if(temp==NULL || temp->next==NULL){
       prev->next=NULL;
    }
    else{
        prev->next=temp->next;
        free(temp);
    }
    return head;
}