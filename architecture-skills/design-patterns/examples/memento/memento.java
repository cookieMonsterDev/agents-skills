// Memento pattern in Java.
//
// A private nested record gives real opacity: only TextEditor can read
// the snapshot's fields, so History stores state it cannot inspect.

import java.util.ArrayDeque;
import java.util.Deque;

public class memento {

    static final class TextEditor {
        private StringBuilder text = new StringBuilder();
        private int cursor = 0;

        /** Memento: fields visible only to the enclosing originator. */
        record Snapshot(String text, int cursor) {}

        void type(String insert) {
            text.insert(cursor, insert);
            cursor += insert.length();
        }

        Snapshot save() {
            return new Snapshot(text.toString(), cursor);
        }

        void restore(Snapshot s) {
            text = new StringBuilder(s.text());
            cursor = s.cursor();
        }

        @Override
        public String toString() {
            return "'" + text + "' (cursor at " + cursor + ")";
        }
    }

    /** Caretaker: stores snapshots but never inspects them. */
    static final class History {
        private final Deque<TextEditor.Snapshot> snapshots = new ArrayDeque<>();

        void push(TextEditor.Snapshot s) {
            snapshots.push(s);
        }

        TextEditor.Snapshot pop() {
            return snapshots.isEmpty() ? null : snapshots.pop();
        }
    }

    public static void main(String[] args) {
        TextEditor editor = new TextEditor();
        History history = new History();

        editor.type("Hello");
        history.push(editor.save());
        editor.type(", world");
        history.push(editor.save());
        editor.type("!!!");
        System.out.println("current: " + editor);

        for (int i = 0; i < 2; i++) {
            TextEditor.Snapshot s = history.pop();
            if (s != null) {
                editor.restore(s);
                System.out.println("undo:    " + editor);
            }
        }
    }
}
