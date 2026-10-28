// Interface Segregation Principle in Swift.
//
// A fat OfficeMachine protocol forces SimplePrinter to stub scanDocument
// and faxDocument with errors. The fix splits Printer and Scanner so
// each client depends only on the methods it calls.

import Foundation

enum OfficeError: Error, CustomStringConvertible {
    case notSupported(String)

    var description: String { "not supported" }
}

// --- Violation: one fat protocol every device must implement ---

protocol OfficeMachine {
    func printDocument(_ path: String)
    func scanDocument(_ path: String) throws
    func faxDocument(_ path: String) throws
}

final class SimplePrinter: OfficeMachine {
    func printDocument(_ path: String) {
        print("print \(path)")
    }

    func scanDocument(_ path: String) throws {
        throw OfficeError.notSupported("scan")
    }

    func faxDocument(_ path: String) throws {
        throw OfficeError.notSupported("fax")
    }
}

func runOfficeJob(_ machine: OfficeMachine, path: String) {
    machine.printDocument(path)
    for (action, fn) in [
        ("scan", { try machine.scanDocument(path) }),
        ("fax", { try machine.faxDocument(path) }),
    ] {
        do {
            try fn()
        } catch is OfficeError {
            print("\(action) attempt: NotSupported")
        } catch {
            fatalError("\(error)")
        }
    }
}

// --- Fix: small client-specific protocols ---

protocol Printer {
    func printDocument(_ path: String)
}

protocol Scanner {
    func scanDocument(_ path: String)
}

final class BasicPrinter: Printer {
    func printDocument(_ path: String) { print("print \(path)") }
}

final class FlatbedScanner: Scanner {
    func scanDocument(_ path: String) { print("scan \(path)") }
}

final class MultiFunctionDevice: Printer, Scanner {
    func printDocument(_ path: String) { print("print \(path)") }
    func scanDocument(_ path: String) { print("scan \(path)") }
}

func printJob(_ printer: Printer, path: String) {
    printer.printDocument(path)
}

func scanJob(_ scanner: Scanner, path: String) {
    scanner.scanDocument(path)
}

print("-- Violation: SimplePrinter forced to stub scan/fax --")
runOfficeJob(SimplePrinter(), path: "document.pdf")

print("\n-- Fix: clients depend only on what they need --")
printJob(BasicPrinter(), path: "document.pdf")
scanJob(FlatbedScanner(), path: "page.tif")
printJob(MultiFunctionDevice(), path: "report.pdf")
