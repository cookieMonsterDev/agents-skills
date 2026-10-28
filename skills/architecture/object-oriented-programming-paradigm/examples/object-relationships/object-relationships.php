<?php
// Object relationships in PHP.
//
// Every field is a reference; the relationships survive as conventions.
// Constructor promotion with private composed parts vs. injected aggregated
// collaborators makes the split readable at the constructor signature.

declare(strict_types=1);

final readonly class Book
{
    public function __construct(public string $title) {}
}

final class Library
{
    /** @var list<Book> */
    private array $books;

  /** @param list<Book> $books */
    public function __construct(array $books)
    {
        $this->books = $books;
    }

    public function lookup(string $title): ?Book
    {
        foreach ($this->books as $book) {
            if ($book->title === $title) {
                return $book;
            }
        }
        return null;
    }
}

final class Professor
{
    public function __construct(public string $name) {}

    // Association: library is a parameter — no stored reference.
    public function lookupBook(Library $library, string $title): string
    {
        $book = $library->lookup($title);
        if ($book === null) {
            return "{$this->name}: '{$title}' not in catalog";
        }
        return "{$this->name} looked up '{$book->title}' in the library";
    }
}

final readonly class Course
{
    public function __construct(public string $title) {}
}

final class Department
{
    /** @var list<Professor> aggregation: injected references */
    private array $professors;

    /** @var list<Course> composition: created and owned here */
    private array $courses = [];

    /** @param list<Professor> $professors */
    public function __construct(
        private string $name,
        array $professors,
    ) {
        $this->professors = $professors;
    }

    public function addCourse(string $title): void
    {
        $this->courses[] = new Course($title);
    }

    public function dissolve(): void
    {
        $this->professors = []; // drop references — never destroy professors
        $this->courses = [];    // composed parts die with the whole
    }

    public function printRoster(): void
    {
        $names = array_map(static fn (Professor $p): string => $p->name, $this->professors);
        echo "{$this->name} roster: " . implode(', ', $names) . PHP_EOL;
    }

    public function printCourses(): void
    {
        if ($this->courses === []) {
            echo "{$this->name} courses: (none)" . PHP_EOL;
            return;
        }
        $titles = array_map(static fn (Course $c): string => $c->title, $this->courses);
        echo "{$this->name} courses: " . implode(', ', $titles) . PHP_EOL;
    }
}

$library = new Library([
    new Book('Algorithms'),
    new Book('Calculus'),
]);

$alice = new Professor('Dr. Alice');
$bob = new Professor('Dr. Bob');

$cs = new Department('Computer Science', [$alice, $bob]);
$cs->addCourse('Algorithms');
$cs->addCourse('Data Structures');

$math = new Department('Mathematics', [$alice]);
$math->addCourse('Calculus');

echo "=== Association (uses-a) ===" . PHP_EOL;
echo $alice->lookupBook($library, 'Algorithms') . PHP_EOL;

echo PHP_EOL . "=== Aggregation (has-a) ===" . PHP_EOL;
$cs->printRoster();
$math->printRoster();
$cs->dissolve();
echo "After dissolving CS — Alice still exists: {$alice->name}" . PHP_EOL;
$math->printRoster();

echo PHP_EOL . "=== Composition (owns-a) ===" . PHP_EOL;
$math->printCourses();
$math->dissolve();
$math->printCourses();
