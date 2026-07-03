// Composite pattern in JavaScript.
//
// Files and directories expose the same size()/print() shape; duck
// typing removes the need for a formal interface. The DOM is the
// best-known composite in JavaScript.

class File {
  constructor(name, bytes) {
    this.name = name;
    this.bytes = bytes;
  }
  size() {
    return this.bytes;
  }
  print(indent = 0) {
    console.log(`${" ".repeat(indent)}${this.name} (${this.bytes} B)`);
  }
}

class Directory {
  constructor(name) {
    this.name = name;
    this.children = [];
  }
  add(child) {
    this.children.push(child);
    return this;
  }
  size() {
    return this.children.reduce((total, child) => total + child.size(), 0);
  }
  print(indent = 0) {
    console.log(`${" ".repeat(indent)}${this.name}/ (${this.size()} B)`);
    for (const child of this.children) {
      child.print(indent + 2);
    }
  }
}

const project = new Directory("project")
  .add(new Directory("src").add(new File("main.py", 1200)).add(new File("util.py", 450)))
  .add(new Directory("docs").add(new File("readme.md", 800)))
  .add(new File(".gitignore", 20));

project.print();
