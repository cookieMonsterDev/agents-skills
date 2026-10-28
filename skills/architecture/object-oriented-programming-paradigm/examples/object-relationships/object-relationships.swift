// Object relationships in Swift.
//
// ARC makes the distinction semi-visible: a let reference held only by its
// whole behaves as composition (deinit fires when the whole goes), strong
// references shared across objects are aggregation, and passing a collaborator
// as a parameter is association because it adds no lifetime coupling.

import Foundation

struct Book {
    let title: String
}

final class Library {
    private let books: [Book]

    init(books: [Book]) {
        self.books = books
    }

    func lookup(_ title: String) -> Book? {
        books.first { $0.title == title }
    }
}

final class Professor {
    let name: String

    init(name: String) {
        self.name = name
    }

    // Association: library is a parameter — no stored reference.
    func lookupBook(_ library: Library, title: String) -> String {
        guard let book = library.lookup(title) else {
            return "\(name): '\(title)' not in catalog"
        }
        return "\(name) looked up '\(book.title)' in the library"
    }
}

struct Course {
    let title: String
}

final class Department {
    let name: String
    private var professors: [Professor] // aggregation: strong refs, shared
    private var courses: [Course] = []  // composition: owned exclusively here

    init(name: String, professors: [Professor]) {
        self.name = name
        self.professors = professors
    }

    func addCourse(_ title: String) {
        courses.append(Course(title: title))
    }

    func dissolve() {
        professors.removeAll() // drop strong refs — professors survive if held elsewhere
        courses.removeAll()    // composed parts released when whole clears them
    }

    func printRoster() {
        let names = professors.map(\.name).joined(separator: ", ")
        print("\(name) roster: \(names)")
    }

    func printCourses() {
        if courses.isEmpty {
            print("\(name) courses: (none)")
            return
        }
        let titles = courses.map(\.title).joined(separator: ", ")
        print("\(name) courses: \(titles)")
    }
}

let library = Library(books: [
    Book(title: "Algorithms"),
    Book(title: "Calculus"),
])

let alice = Professor(name: "Dr. Alice")
let bob = Professor(name: "Dr. Bob")

let cs = Department(name: "Computer Science", professors: [alice, bob])
cs.addCourse("Algorithms")
cs.addCourse("Data Structures")

let math = Department(name: "Mathematics", professors: [alice])
math.addCourse("Calculus")

print("=== Association (uses-a) ===")
print(alice.lookupBook(library, title: "Algorithms"))

print("\n=== Aggregation (has-a) ===")
cs.printRoster()
math.printRoster()
cs.dissolve()
print("After dissolving CS — Alice still exists: \(alice.name)")
math.printRoster()

print("\n=== Composition (owns-a) ===")
math.printCourses()
math.dissolve()
math.printCourses()
