/**
 * Definition for singly-linked list.
 * struct ListNode {
    int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
}

class Solution {
   public
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        set<ListNode *> ht;

        while (headA != nullptr) {
            ht.insert(headA);
            headA = headA->next;
        }

        while (headB != nullptr) {
            if (ht.find(headB) != ht.end()) {
                return headB;
            }
            headB = headB->next;
        }
        return nullptr;
    }
};
