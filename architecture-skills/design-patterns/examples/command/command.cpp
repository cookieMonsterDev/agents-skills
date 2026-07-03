// Command pattern in C++.
//
// Text editor with undo: a virtual Command interface with execute/undo,
// concrete commands capturing their own undo state, and a history stack
// of unique_ptrs as the invoker. For one-shot commands without undo,
// std::function<void()> is the lighter modern idiom.

#include <iostream>
#include <memory>
#include <string>
#include <vector>

struct Editor {
    std::string text; // receiver
};

class Command {
public:
    virtual ~Command() = default;
    virtual void execute() = 0;
    virtual void undo() = 0;
};

class InsertText : public Command {
public:
    InsertText(Editor& editor, std::string text)
        : editor_(editor), text_(std::move(text)) {}

    void execute() override { editor_.text += text_; }
    void undo() override { editor_.text.erase(editor_.text.size() - text_.size()); }

private:
    Editor& editor_;
    std::string text_;
};

class DeleteLast : public Command {
public:
    DeleteLast(Editor& editor, std::size_t count) : editor_(editor), count_(count) {}

    void execute() override {
        deleted_ = editor_.text.substr(editor_.text.size() - count_);
        editor_.text.erase(editor_.text.size() - count_);
    }
    void undo() override { editor_.text += deleted_; }

private:
    Editor& editor_;
    std::size_t count_;
    std::string deleted_; // captured on execute so undo can restore it
};

class History {
public:
    void execute(std::unique_ptr<Command> command) {
        command->execute();
        undoStack_.push_back(std::move(command));
    }

    void undo() {
        if (!undoStack_.empty()) {
            undoStack_.back()->undo();
            undoStack_.pop_back();
        }
    }

private:
    std::vector<std::unique_ptr<Command>> undoStack_;
};

int main() {
    Editor editor;
    History history;

    history.execute(std::make_unique<InsertText>(editor, "Hello"));
    history.execute(std::make_unique<InsertText>(editor, ", world!"));
    history.execute(std::make_unique<DeleteLast>(editor, 1));
    std::cout << "after edits: \"" << editor.text << "\"\n";

    history.undo();
    history.undo();
    std::cout << "after 2 undos: \"" << editor.text << "\"\n";
    return 0;
}
