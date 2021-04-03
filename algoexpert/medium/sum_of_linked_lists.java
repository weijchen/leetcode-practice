package algoexpert.medium;

// O(max(n, m)) time | O(max(n, m)) space - where n is the lendth of the first linked list and m is the length of the second linked list
public class sum_of_linked_lists {
  class Program {
    // This is an input class. Do not edit.
    public class LinkedList {
      public int value;
      public LinkedList next;

      public LinkedList(int value) {
        this.value = value;
        this.next = null;
      }
    }

    public LinkedList sumOfLinkedLists(LinkedList linkedListOne, LinkedList linkedListTwo) {
      // Write your code here.
      int carry = 0;
      LinkedList p1 = linkedListOne;
      LinkedList p2 = linkedListTwo;
      LinkedList curNode = new LinkedList(0);
      LinkedList retNode = curNode;

      while (p1 != null || p2 != null) {
        int val1 = p1 == null ? 0 : p1.value;
        int val2 = p2 == null ? 0 : p2.value;
        int tmpSum = val1 + val2 + carry;
        carry = (tmpSum) >= 10 ? 1 : 0;

        int curValue = tmpSum % 10;
        p1 = p1 == null ? null : p1.next;
        p2 = p2 == null ? null : p2.next;
        curNode.next = new LinkedList(curValue);
        curNode = curNode.next;
      }
      if (carry == 1) {
        curNode.next = new LinkedList(1);
      }
      return retNode.next;
    }
  }

}
