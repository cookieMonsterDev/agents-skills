// Abstraction in C++.
//
// The abstraction is an abstract base class with pure virtual methods
// and a virtual destructor; each implementation hides its operational
// detail (a std::map vs a file). The client takes NoteStore& and runs
// unchanged whichever concrete type is behind the reference.

#include <cstdio>
#include <fstream>
#include <iostream>
#include <map>
#include <optional>
#include <string>

// The abstraction: the only surface callers may rely on.
class NoteStore {
public:
    virtual ~NoteStore() = default;
    virtual void save(const std::string& key, const std::string& text) = 0;
    virtual std::optional<std::string> load(const std::string& key) const = 0;
};

// Operational detail: a std::map. Callers never see it.
class MemoryStore : public NoteStore {
public:
    void save(const std::string& key, const std::string& text) override {
        notes_[key] = text;
    }

    std::optional<std::string> load(const std::string& key) const override {
        auto it = notes_.find(key);
        if (it == notes_.end()) return std::nullopt;
        return it->second;
    }

private:
    std::map<std::string, std::string> notes_;
};

// Operational detail: append-only lines in a file, last write wins.
class FileStore : public NoteStore {
public:
    explicit FileStore(std::string path) : path_(std::move(path)) {}

    void save(const std::string& key, const std::string& text) override {
        std::ofstream(path_, std::ios::app) << key << '\t' << text << '\n';
    }

    std::optional<std::string> load(const std::string& key) const override {
        std::ifstream in(path_);
        std::optional<std::string> found;
        std::string line;
        while (std::getline(in, line)) {
            auto tab = line.find('\t');
            if (tab != std::string::npos && line.substr(0, tab) == key)
                found = line.substr(tab + 1);  // keep scanning: last write wins
        }
        return found;
    }

private:
    std::string path_;
};

// Client: written once against the abstraction, never edited when the
// implementation behind it swaps.
void run_session(NoteStore& store) {
    store.save("groceries", "eggs, flour");
    store.save("groceries", "eggs, flour, milk");  // overwrite
    store.save("idea", "hide the how, expose the what");
    std::cout << "  groceries: " << store.load("groceries").value_or("(missing)") << '\n'
              << "  idea:      " << store.load("idea").value_or("(missing)") << '\n'
              << "  missing:   " << store.load("missing").value_or("(missing)") << '\n';
}

int main() {
    MemoryStore memory;
    std::cout << "memory-backed store:\n";
    run_session(memory);

    const std::string path = "abstraction_demo.txt";
    FileStore file(path);
    std::cout << "file-backed store:\n";
    run_session(file);
    std::remove(path.c_str());
}
