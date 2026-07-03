// Interface Segregation Principle in C++.
//
// A fat OfficeMachine interface forces SimplePrinter to stub scan()
// and fax() with std::runtime_error. The fix splits Printer and Scanner
// so each client depends only on the methods it calls.

#include <iostream>
#include <stdexcept>
#include <string>

// --- Violation: one fat interface every device must implement ---

class OfficeMachine {
public:
    virtual ~OfficeMachine() = default;
    virtual void printDocument(const std::string& path) = 0;
    virtual void scanDocument(const std::string& path) = 0;
    virtual void faxDocument(const std::string& path) = 0;
};

class SimplePrinter : public OfficeMachine {
public:
    void printDocument(const std::string& path) override {
        std::cout << "print " << path << "\n";
    }

    void scanDocument(const std::string& path) override {
        (void)path;
        throw std::runtime_error("scan");
    }

    void faxDocument(const std::string& path) override {
        (void)path;
        throw std::runtime_error("fax");
    }
};

void runOfficeJob(OfficeMachine& machine, const std::string& path) {
    machine.printDocument(path);
    try {
        machine.scanDocument(path);
    } catch (const std::runtime_error&) {
        std::cout << "scan attempt: NotSupported\n";
    }
    try {
        machine.faxDocument(path);
    } catch (const std::runtime_error&) {
        std::cout << "fax attempt: NotSupported\n";
    }
}

// --- Fix: small client-specific interfaces ---

class Printer {
public:
    virtual ~Printer() = default;
    virtual void printDocument(const std::string& path) = 0;
};

class Scanner {
public:
    virtual ~Scanner() = default;
    virtual void scanDocument(const std::string& path) = 0;
};

class BasicPrinter : public Printer {
public:
    void printDocument(const std::string& path) override {
        std::cout << "print " << path << "\n";
    }
};

class FlatbedScanner : public Scanner {
public:
    void scanDocument(const std::string& path) override {
        std::cout << "scan " << path << "\n";
    }
};

class MultiFunctionDevice : public Printer, public Scanner {
public:
    void printDocument(const std::string& path) override {
        std::cout << "print " << path << "\n";
    }

    void scanDocument(const std::string& path) override {
        std::cout << "scan " << path << "\n";
    }
};

void printJob(Printer& printer, const std::string& path) {
    printer.printDocument(path);
}

void scanJob(Scanner& scanner, const std::string& path) {
    scanner.scanDocument(path);
}

int main() {
    std::cout << "-- Violation: SimplePrinter forced to stub scan/fax --\n";
    SimplePrinter simple;
    runOfficeJob(simple, "document.pdf");

    std::cout << "\n-- Fix: clients depend only on what they need --\n";
    BasicPrinter basic;
    FlatbedScanner flatbed;
    MultiFunctionDevice mfd;
    printJob(basic, "document.pdf");
    scanJob(flatbed, "page.tif");
    printJob(mfd, "report.pdf");
    return 0;
}
