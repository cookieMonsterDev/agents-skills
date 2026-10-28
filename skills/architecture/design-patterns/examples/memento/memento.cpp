// Memento pattern in C++.
//
// The snapshot's fields are private and only TextEditor (a friend) can
// read them, so the history can store snapshots without being able to
// inspect or corrupt editor state — the classic "opaque memento".

#include <iostream>
#include <string>
#include <vector>

class TextEditor;

class Snapshot {  // memento: opaque outside TextEditor
public:
    Snapshot(std::string text, std::size_t cursor)
        : text_(std::move(text)), cursor_(cursor) {}

private:
    friend class TextEditor;
    std::string text_;
    std::size_t cursor_;
};

class TextEditor {  // originator
public:
    void type(const std::string& insert) {
        text_.insert(cursor_, insert);
        cursor_ += insert.size();
    }

    Snapshot save() const { return Snapshot(text_, cursor_); }

    void restore(const Snapshot& s) {
        text_ = s.text_;
        cursor_ = s.cursor_;
    }

    void print(const std::string& label) const {
        std::cout << label << " '" << text_ << "' (cursor at " << cursor_ << ")\n";
    }

private:
    std::string text_;
    std::size_t cursor_ = 0;
};

class History {  // caretaker: stores but never inspects snapshots
public:
    void push(Snapshot s) { snapshots_.push_back(std::move(s)); }

    bool pop(Snapshot& out) {
        if (snapshots_.empty()) return false;
        out = snapshots_.back();
        snapshots_.pop_back();
        return true;
    }

private:
    std::vector<Snapshot> snapshots_;
};

int main() {
    TextEditor editor;
    History history;

    editor.type("Hello");
    history.push(editor.save());
    editor.type(", world");
    history.push(editor.save());
    editor.type("!!!");
    editor.print("current:");

    Snapshot s("", 0);
    for (int i = 0; i < 2 && history.pop(s); i++) {
        editor.restore(s);
        editor.print("undo:   ");
    }
    return 0;
}
