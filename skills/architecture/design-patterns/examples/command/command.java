// Command pattern in Java.
//
// Text editor with undo: a Command interface with execute/undo, concrete
// commands capturing their own undo state, and a history deque as the
// invoker. For one-shot commands without undo, a Runnable lambda is the
// modern lightweight form.

import java.util.ArrayDeque;
import java.util.Deque;

public class command {

    /** Receiver. */
    static final class Editor {
        StringBuilder text = new StringBuilder();
    }

    interface Command {
        void execute();
        void undo();
    }

    static final class InsertText implements Command {
        private final Editor editor;
        private final String text;

        InsertText(Editor editor, String text) {
            this.editor = editor;
            this.text = text;
        }

        @Override
        public void execute() {
            editor.text.append(text);
        }

        @Override
        public void undo() {
            editor.text.setLength(editor.text.length() - text.length());
        }
    }

    static final class DeleteLast implements Command {
        private final Editor editor;
        private final int count;
        private String deleted; // captured on execute so undo can restore it

        DeleteLast(Editor editor, int count) {
            this.editor = editor;
            this.count = count;
        }

        @Override
        public void execute() {
            int len = editor.text.length();
            deleted = editor.text.substring(len - count);
            editor.text.setLength(len - count);
        }

        @Override
        public void undo() {
            editor.text.append(deleted);
        }
    }

    /** Invoker: runs commands and tracks them for undo. */
    static final class History {
        private final Deque<Command> undoStack = new ArrayDeque<>();

        void execute(Command command) {
            command.execute();
            undoStack.push(command);
        }

        void undo() {
            if (!undoStack.isEmpty()) {
                undoStack.pop().undo();
            }
        }
    }

    public static void main(String[] args) {
        Editor editor = new Editor();
        History history = new History();

        history.execute(new InsertText(editor, "Hello"));
        history.execute(new InsertText(editor, ", world!"));
        history.execute(new DeleteLast(editor, 1));
        System.out.println("after edits: \"" + editor.text + "\"");

        history.undo();
        history.undo();
        System.out.println("after 2 undos: \"" + editor.text + "\"");
    }
}
