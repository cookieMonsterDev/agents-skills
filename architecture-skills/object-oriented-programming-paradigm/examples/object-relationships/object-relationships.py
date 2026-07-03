"""Object relationships in Python.

Three ways one object refers to another: association (uses-a), aggregation
(has-a), and composition (owns-a). The dividing questions are who creates
the part, whether it can be shared, and whether it survives the whole.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Book:
    title: str


@dataclass
class Library:
    """External service — neither professor nor department owns it."""

    books: list[Book] = field(default_factory=list)

    def lookup(self, title: str) -> Book | None:
        for book in self.books:
            if book.title == title:
                return book
        return None


@dataclass
class Professor:
    """Independent object: created elsewhere, may outlive any department."""

    name: str

    # Association: uses the library for one operation; no stored reference.
    def lookup_book(self, library: Library, title: str) -> str:
        book = library.lookup(title)
        if book is None:
            return f"{self.name}: '{title}' not in catalog"
        return f"{self.name} looked up '{book.title}' in the library"


@dataclass
class Course:
    """Meaningful only inside its department — never handed out."""

    title: str


class Department:
    """Whole that aggregates professors and composes courses."""

    def __init__(self, name: str, professors: list[Professor]) -> None:
        self.name = name
        self.professors = list(professors)  # aggregation: borrowed references
        self._courses: list[Course] = []      # composition: sole owner

    def add_course(self, title: str) -> None:
        self._courses.append(Course(title))  # whole creates the part

    def course_titles(self) -> list[str]:
        return [c.title for c in self._courses]

    def professor_names(self) -> list[str]:
        return [p.name for p in self.professors]

    def dissolve(self) -> None:
        """Drop aggregated references; destroy composed courses."""
        self.professors.clear()
        self._courses.clear()


if __name__ == "__main__":
    library = Library(books=[Book("Algorithms"), Book("Calculus")])

    alice = Professor("Dr. Alice")
    bob = Professor("Dr. Bob")

    cs = Department("Computer Science", [alice, bob])
    cs.add_course("Algorithms")
    cs.add_course("Data Structures")

    math = Department("Mathematics", [alice])  # Alice shared across departments
    math.add_course("Calculus")

    print("=== Association (uses-a) ===")
    print(alice.lookup_book(library, "Algorithms"))

    print("\n=== Aggregation (has-a) ===")
    print(f"CS roster: {', '.join(cs.professor_names())}")
    print(f"Math roster: {', '.join(math.professor_names())}")
    cs.dissolve()
    print(f"After dissolving CS — Alice still exists: {alice.name}")
    print(f"Math roster unchanged: {', '.join(math.professor_names())}")

    print("\n=== Composition (owns-a) ===")
    print(f"Math courses: {', '.join(math.course_titles())}")
    math.dissolve()
    print(f"After dissolving Math — courses gone: {math.course_titles() or '(none)'}")
