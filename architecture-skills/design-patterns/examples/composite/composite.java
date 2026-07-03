// Composite pattern in Java.
//
// Files and directories implement one Node interface, so callers can
// total sizes or print trees without distinguishing leaf from branch —
// the same shape as Swing containers or the XML DOM.
//
// The public class is lowercase so the filename matches the pattern name.

import java.util.ArrayList;
import java.util.List;

public class composite {

    interface Node {
        long size();
        void print(int indent);
    }

    static class File implements Node {
        private final String name;
        private final long size;

        File(String name, long size) {
            this.name = name;
            this.size = size;
        }

        public long size() {
            return size;
        }

        public void print(int indent) {
            System.out.printf("%s%s (%d B)%n", " ".repeat(indent), name, size);
        }
    }

    static class Directory implements Node {
        private final String name;
        private final List<Node> children = new ArrayList<>();

        Directory(String name) {
            this.name = name;
        }

        Directory add(Node child) {
            children.add(child);
            return this;
        }

        public long size() {
            return children.stream().mapToLong(Node::size).sum();
        }

        public void print(int indent) {
            System.out.printf("%s%s/ (%d B)%n", " ".repeat(indent), name, size());
            for (Node child : children) {
                child.print(indent + 2);
            }
        }
    }

    public static void main(String[] args) {
        Directory project = new Directory("project")
            .add(new Directory("src")
                .add(new File("main.py", 1200))
                .add(new File("util.py", 450)))
            .add(new Directory("docs")
                .add(new File("readme.md", 800)))
            .add(new File(".gitignore", 20));
        project.print(0);
    }
}
