// Object relationships in JavaScript.
//
// Every reference looks alike; signal composition by creating parts inside
// the class and keeping the field private (#courses). Aggregation accepts
// objects from outside. Association passes collaborators as method parameters.

class Book {
  constructor(title) {
    this.title = title;
  }
}

class Library {
  constructor(books = []) {
    this.books = books;
  }

  lookup(title) {
    return this.books.find((b) => b.title === title) ?? null;
  }
}

class Professor {
  constructor(name) {
    this.name = name;
  }

  // Association: library is a parameter — no stored reference.
  lookupBook(library, title) {
    const book = library.lookup(title);
    if (!book) {
      return `${this.name}: '${title}' not in catalog`;
    }
    return `${this.name} looked up '${book.title}' in the library`;
  }
}

class Course {
  constructor(title) {
    this.title = title;
  }
}

class Department {
  #courses = []; // composition: private, created and owned here

  constructor(name, professors) {
    this.name = name;
    this.professors = [...professors]; // aggregation: references from outside
  }

  addCourse(title) {
    this.#courses.push(new Course(title));
  }

  courseTitles() {
    return this.#courses.map((c) => c.title);
  }

  professorNames() {
    return this.professors.map((p) => p.name);
  }

  dissolve() {
    this.professors = []; // drop references — never destroy professors
    this.#courses = [];   // composed parts die with the whole
  }

  printRoster() {
    console.log(`${this.name} roster: ${this.professorNames().join(", ")}`);
  }

  printCourses() {
    const titles = this.courseTitles();
    console.log(
      titles.length === 0
        ? `${this.name} courses: (none)`
        : `${this.name} courses: ${titles.join(", ")}`
    );
  }
}

const library = new Library([new Book("Algorithms"), new Book("Calculus")]);

const alice = new Professor("Dr. Alice");
const bob = new Professor("Dr. Bob");

const cs = new Department("Computer Science", [alice, bob]);
cs.addCourse("Algorithms");
cs.addCourse("Data Structures");

const math = new Department("Mathematics", [alice]);
math.addCourse("Calculus");

console.log("=== Association (uses-a) ===");
console.log(alice.lookupBook(library, "Algorithms"));

console.log("\n=== Aggregation (has-a) ===");
cs.printRoster();
math.printRoster();
cs.dissolve();
console.log(`After dissolving CS — Alice still exists: ${alice.name}`);
math.printRoster();

console.log("\n=== Composition (owns-a) ===");
math.printCourses();
math.dissolve();
math.printCourses();
