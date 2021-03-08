/**
 * Definition for singly-linked list.
 * 
 */

struct ListNode
{
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(nullptr) {}
};

class Solution
{
public:
  bool hasCycle(ListNode *head)
  {
    auto fast = head;
    auto slow = head;
    while (fast)
    {
      if (!fast->next)
        return false;
      fast = fast->next->next;
      slow = slow->next;
      if (fast == slow)
        return true;
    }

    return false;
  }
};
