// Iterator pattern in Java.
//
// A binary search tree traversed in sorted order. Java builds the
// pattern in as Iterable<T>/Iterator<T>: implementing them plugs a
// custom collection into for-each. Java has no generators, so the
// iterator replaces the recursive walk with an explicit stack.

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Iterator;

public class iterator {

    static final class SortedTree implements Iterable<Integer> {

        private static final class Node {
            final int value;
            Node left, right;
            Node(int value) { this.value = value; }
        }

        private Node root;

        void add(int value) {
            if (root == null) {
                root = new Node(value);
                return;
            }
            Node node = root;
            while (true) {
                if (value < node.value) {
                    if (node.left == null) { node.left = new Node(value); return; }
                    node = node.left;
                } else {
                    if (node.right == null) { node.right = new Node(value); return; }
                    node = node.right;
                }
            }
        }

        @Override
        public Iterator<Integer> iterator() {
            return new Iterator<>() {
                // Stack of nodes whose left subtrees are already done.
                private final Deque<Node> stack = new ArrayDeque<>();
                { pushLeftSpine(root); }

                private void pushLeftSpine(Node node) {
                    for (; node != null; node = node.left) {
                        stack.push(node);
                    }
                }

                @Override
                public boolean hasNext() {
                    return !stack.isEmpty();
                }

                @Override
                public Integer next() {
                    Node node = stack.pop();
                    pushLeftSpine(node.right);
                    return node.value;
                }
            };
        }
    }

    public static void main(String[] args) {
        SortedTree tree = new SortedTree();
        for (int value : new int[] {5, 3, 8, 1, 4, 9, 7}) {
            tree.add(value);
        }

        StringBuilder inOrder = new StringBuilder("in order:");
        int sum = 0;
        for (int value : tree) {
            inOrder.append(' ').append(value);
            sum += value;
        }
        System.out.println(inOrder);
        System.out.println("sum: " + sum);
    }
}
