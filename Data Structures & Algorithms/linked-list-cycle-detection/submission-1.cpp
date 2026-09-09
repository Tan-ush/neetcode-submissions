/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    bool hasCycle(ListNode* head) {
        unordered_set<ListNode*> mp;
        ListNode* ne = head;
        while (ne){
            if (mp.find(ne) != mp.end()){
                return true;
            }
            mp.insert(ne);
            ne = ne->next;
        }
        return false;
    }
};
