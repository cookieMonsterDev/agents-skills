// Object relationships in Java.
//
// The GC erases the memory-level distinction — every field is a reference.
// Composition means the whole constructs the part and cancels it in close();
// aggregation means the part arrives via constructor and is left alone at
// teardown. Java identifiers cannot contain hyphens, so the launcher class
// is named after the concept instead of the file.

import java.util.ArrayList;
import java.util.List;

class ObjectRelationshipsDemo {

    record Book(String title) {}

    static final class Library {
        private final List<Book> books = new ArrayList<>();

        Library(List<Book> initial) {
            books.addAll(initial);
        }

        Book lookup(String title) {
            return books.stream()
                    .filter(b -> b.title().equals(title))
                    .findFirst()
                    .orElse(null);
        }
    }

    static final class Professor {
        private final String name;

        Professor(String name) {
            this.name = name;
        }

        String name() {
            return name;
        }

        // Association: library is a method parameter, not a stored field.
        String lookupBook(Library library, String title) {
            Book book = library.lookup(title);
            if (book == null) {
                return name + ": '" + title + "' not in catalog";
            }
            return name + " looked up '" + book.title() + "' in the library";
        }
    }

    record Course(String title) {}

    static final class Department {
        private final String name;
        private final List<Professor> professors; // aggregation: injected
        private final List<Course> courses = new ArrayList<>(); // composition

        Department(String name, List<Professor> professors) {
            this.name = name;
            this.professors = new ArrayList<>(professors);
        }

        void addCourse(String title) {
            courses.add(new Course(title)); // whole creates the part
        }

        List<String> professorNames() {
            return professors.stream().map(Professor::name).toList();
        }

        List<String> courseTitles() {
            return courses.stream().map(Course::title).toList();
        }

        void dissolve() {
            professors.clear(); // drop references — never destroy professors
            courses.clear();    // composed parts cancelled with the whole
        }

        void printRoster() {
            System.out.print(name + " roster:");
            for (Professor p : professors) {
                System.out.print(" " + p.name());
            }
            System.out.println();
        }

        void printCourses() {
            if (courses.isEmpty()) {
                System.out.println(name + " courses: (none)");
                return;
            }
            System.out.print(name + " courses:");
            for (Course c : courses) {
                System.out.print(" " + c.title());
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Library library = new Library(List.of(
                new Book("Algorithms"),
                new Book("Calculus")
        ));

        Professor alice = new Professor("Dr. Alice");
        Professor bob = new Professor("Dr. Bob");

        Department cs = new Department("Computer Science", List.of(alice, bob));
        cs.addCourse("Algorithms");
        cs.addCourse("Data Structures");

        Department math = new Department("Mathematics", List.of(alice));
        math.addCourse("Calculus");

        System.out.println("=== Association (uses-a) ===");
        System.out.println(alice.lookupBook(library, "Algorithms"));

        System.out.println("\n=== Aggregation (has-a) ===");
        cs.printRoster();
        math.printRoster();
        cs.dissolve();
        System.out.println("After dissolving CS — Alice still exists: " + alice.name());
        math.printRoster();

        System.out.println("\n=== Composition (owns-a) ===");
        math.printCourses();
        math.dissolve();
        math.printCourses();
    }
}
