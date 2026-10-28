// Object relationships in C++.
//
// Ownership is spelled in the member type: unique_ptr or by-value member is
// composition (destructor cascades), shared_ptr is aggregation, raw pointer
// or reference is association (non-owning by convention).

#include <iostream>
#include <memory>
#include <string>
#include <vector>

struct Book {
    std::string title;
};

struct Library {
    std::vector<Book> books;

    const Book *lookup(const std::string &title) const {
        for (const Book &book : books) {
            if (book.title == title) {
                return &book;
            }
        }
        return nullptr;
    }
};

struct Professor {
    std::string name;

    // Association: library is a non-owning parameter.
    std::string lookupBook(const Library &library, const std::string &title) const {
        const Book *book = library.lookup(title);
        if (!book) {
            return name + ": '" + title + "' not in catalog";
        }
        return name + " looked up '" + book->title + "' in the library";
    }
};

struct Course {
    std::string title;
};

class Department {
public:
    Department(std::string name, std::vector<Professor *> professors)
        : name_(std::move(name)), professors_(std::move(professors)) {}

    void addCourse(std::string title) {
        courses_.push_back(std::make_unique<Course>(Course{std::move(title)}));
    }

    std::vector<std::string> professorNames() const {
        std::vector<std::string> names;
        for (const Professor *p : professors_) {
            names.push_back(p->name);
        }
        return names;
    }

    std::vector<std::string> courseTitles() const {
        std::vector<std::string> titles;
        for (const auto &c : courses_) {
            titles.push_back(c->title);
        }
        return titles;
    }

    void dissolve() {
        professors_.clear();  // aggregation: never delete professors
        courses_.clear();     // composition: unique_ptrs destroyed here
    }

    void printRoster() const {
        std::cout << name_ << " roster:";
        for (const Professor *p : professors_) {
            std::cout << " " << p->name;
        }
        std::cout << "\n";
    }

    void printCourses() const {
        if (courses_.empty()) {
            std::cout << name_ << " courses: (none)\n";
            return;
        }
        std::cout << name_ << " courses:";
        for (const auto &c : courses_) {
            std::cout << " " << c->title;
        }
        std::cout << "\n";
    }

private:
    std::string name_;
    std::vector<Professor *> professors_;              // aggregation: raw ptr
    std::vector<std::unique_ptr<Course>> courses_;     // composition: sole owner
};

int main() {
    Library library{{{"Algorithms"}, {"Calculus"}}};

    Professor alice{"Dr. Alice"};
    Professor bob{"Dr. Bob"};

    Department cs("Computer Science", {&alice, &bob});
    cs.addCourse("Algorithms");
    cs.addCourse("Data Structures");

    Department math("Mathematics", {&alice});
    math.addCourse("Calculus");

    std::cout << "=== Association (uses-a) ===\n";
    std::cout << alice.lookupBook(library, "Algorithms") << "\n";

    std::cout << "\n=== Aggregation (has-a) ===\n";
    cs.printRoster();
    math.printRoster();
    cs.dissolve();
    std::cout << "After dissolving CS — Alice still exists: " << alice.name << "\n";
    math.printRoster();

    std::cout << "\n=== Composition (owns-a) ===\n";
    math.printCourses();
    math.dissolve();
    math.printCourses();

    return 0;
}
