/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {

    struct ListNode* list3=NULL,*tail;

    if(list1==NULL)
    {
        return list2;
    }
    if(list2==NULL)
    {
        return list1;
    }
    if(list1->val < list2->val)
    {
        list3=list1;
        tail=list1;
        list1=list1->next;
    }
    else
    {
        list3=list2;
        tail=list2;
        list2=list2->next;
    }

    while(list1!=NULL && list2 !=NULL)
    {
        if(list1->val<list2->val)
        {
            tail->next=list1;
            tail=tail->next;
            list1=list1->next;
        }
        else
        {
            tail->next=list2;
            tail=tail->next;
            list2=list2->next;
        }
    }
    if(list1==NULL)
    {
        tail->next=list2;
    }
    else
    {
        tail->next=list1;
    }

    return list3;



    
    
}