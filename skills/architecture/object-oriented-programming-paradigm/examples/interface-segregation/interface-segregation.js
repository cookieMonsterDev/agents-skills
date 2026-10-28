// Interface Segregation Principle in JavaScript.
//
// A fat officeMachine duck type forces SimplePrinter to stub scanDocument
// and faxDocument with errors. The fix splits printer and scanner shapes
// so each client depends only on the methods it calls.

class NotSupportedError extends Error {
  constructor(feature) {
    super(feature);
    this.name = 'NotSupported';
  }
}

// --- Violation: one fat shape every device must implement ---

class SimplePrinter {
  printDocument(path) {
    console.log(`print ${path}`);
  }

  scanDocument(path) {
    throw new NotSupportedError('scan');
  }

  faxDocument(path) {
    throw new NotSupportedError('fax');
  }
}

function runOfficeJob(machine, path) {
  machine.printDocument(path);
  for (const [action, fn] of [
    ['scan', () => machine.scanDocument(path)],
    ['fax', () => machine.faxDocument(path)],
  ]) {
    try {
      fn();
    } catch (e) {
      if (e instanceof NotSupportedError) {
        console.log(`${action} attempt: NotSupported`);
      } else {
        throw e;
      }
    }
  }
}

// --- Fix: small client-specific shapes ---

class BasicPrinter {
  printDocument(path) {
    console.log(`print ${path}`);
  }
}

class FlatbedScanner {
  scanDocument(path) {
    console.log(`scan ${path}`);
  }
}

class MultiFunctionDevice {
  printDocument(path) {
    console.log(`print ${path}`);
  }

  scanDocument(path) {
    console.log(`scan ${path}`);
  }
}

function printJob(printer, path) {
  printer.printDocument(path);
}

function scanJob(scanner, path) {
  scanner.scanDocument(path);
}

function main() {
  console.log('-- Violation: SimplePrinter forced to stub scan/fax --');
  runOfficeJob(new SimplePrinter(), 'document.pdf');

  console.log('\n-- Fix: clients depend only on what they need --');
  printJob(new BasicPrinter(), 'document.pdf');
  scanJob(new FlatbedScanner(), 'page.tif');
  printJob(new MultiFunctionDevice(), 'report.pdf');
}

main();
