// Interface Segregation Principle in Java.
//
// A fat OfficeMachine interface forces SimplePrinter to stub scan()
// and fax() with UnsupportedOperationException. The fix splits Printer
// and Scanner so each client depends only on the methods it calls.
//
// Java identifiers cannot contain hyphens; a package-private class keeps
// the single-file source launcher (`java interface-segregation.java`) working.

class InterfaceSegregation {

    // --- Violation: one fat interface every device must implement ---

    interface OfficeMachine {
        void printDocument(String path);
        void scanDocument(String path);
        void faxDocument(String path);
    }

    static final class SimplePrinter implements OfficeMachine {
        public void printDocument(String path) {
            System.out.println("print " + path);
        }

        public void scanDocument(String path) {
            throw new UnsupportedOperationException("scan");
        }

        public void faxDocument(String path) {
            throw new UnsupportedOperationException("fax");
        }
    }

    static void runOfficeJob(OfficeMachine machine, String path) {
        machine.printDocument(path);
        try {
            machine.scanDocument(path);
        } catch (UnsupportedOperationException e) {
            System.out.println("scan attempt: NotSupported");
        }
        try {
            machine.faxDocument(path);
        } catch (UnsupportedOperationException e) {
            System.out.println("fax attempt: NotSupported");
        }
    }

    // --- Fix: small client-specific interfaces ---

    interface Printer {
        void printDocument(String path);
    }

    interface Scanner {
        void scanDocument(String path);
    }

    static final class BasicPrinter implements Printer {
        public void printDocument(String path) {
            System.out.println("print " + path);
        }
    }

    static final class FlatbedScanner implements Scanner {
        public void scanDocument(String path) {
            System.out.println("scan " + path);
        }
    }

    static final class MultiFunctionDevice implements Printer, Scanner {
        public void printDocument(String path) {
            System.out.println("print " + path);
        }

        public void scanDocument(String path) {
            System.out.println("scan " + path);
        }
    }

    static void printJob(Printer printer, String path) {
        printer.printDocument(path);
    }

    static void scanJob(Scanner scanner, String path) {
        scanner.scanDocument(path);
    }

    public static void main(String[] args) {
        System.out.println("-- Violation: SimplePrinter forced to stub scan/fax --");
        runOfficeJob(new SimplePrinter(), "document.pdf");

        System.out.println("\n-- Fix: clients depend only on what they need --");
        printJob(new BasicPrinter(), "document.pdf");
        scanJob(new FlatbedScanner(), "page.tif");
        printJob(new MultiFunctionDevice(), "report.pdf");
    }
}
