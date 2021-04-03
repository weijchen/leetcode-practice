/**
 * Remove Kth Node from End - Medium
 * 利用 two pointers, 將 first node pointer 調整到欲刪除的 node 的位置
 */

class Program {
  // O(N) time | O(1) space
  public static void removeKthNodeFromEnd(LinkedList head, int k) {
    // Write your code here.
    int counter = 1;
    LinkedList first = head;
    LinkedList second = head;
    while (counter <= k) {
      second = second.next;
      counter++;
    }
    if (second == null) {
      head.value = head.next.value;
      head.next = head.next.next;
      return;
    }
    while (second.next != null) {
      second = second.next;
      first = first.next;
    }
    first.next = first.next.next;
  }

  static class LinkedList {
    int value;
    LinkedList next = null;

    public LinkedList(int value) {
      this.value = value;
    }
  }
}
