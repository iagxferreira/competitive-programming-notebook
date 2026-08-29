import java.util.*;

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        var dummy = new ListNode(0);
        var tail = dummy;
        var carry = 0;

        while(l1 != null|| l2 != null || carry != 0){
            int d1 = (l1 != null) ? l1.val : 0;
            int d2 = (l2 != null) ? l2.val : 0;

            int sum = d1 + d2 + carry;
            int digit = sum % 10;
            carry = sum / 10;

            var node = new ListNode(digit);
            tail.next = node;
            tail = tail.next;

            l1 = (l1 != null) ? l1.next : null;
            l2 = (l2 != null) ? l2.next : null;
        }

        var result = dummy.next;
        dummy.next = null;
        return result;
    }
}

// LeetCode provides this. Kept here so the file compiles locally.
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
