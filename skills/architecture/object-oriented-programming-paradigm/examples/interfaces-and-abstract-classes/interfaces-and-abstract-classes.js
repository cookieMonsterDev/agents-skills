/** Interfaces & abstract classes in JavaScript.
 *
 * JavaScript has no interface keyword: a class with only method stubs
 * (throwing) or duck typing plays the contract role. TabularExporter
 * implements exportAll once; JsonExporter satisfies the contract directly.
 */

class Metric {
  constructor(name, value) {
    this.name = name;
    this.value = value;
  }
}

class Exporter {
  get contentType() {
    throw new Error('not implemented');
  }

  exportAll(metrics) {
    throw new Error('not implemented');
  }

  fileName() {
    return 'report.' + this.contentType.split('/').pop();
  }
}

class TabularExporter extends Exporter {
  exportAll(metrics) {
    const lines = [this.header(), ...metrics.map((m) => this.row(m))];
    lines.push(`# ${metrics.length} records`);
    return lines.join('\n');
  }

  header() {
    throw new Error('not implemented');
  }

  row(metric) {
    throw new Error('not implemented');
  }
}

class CsvExporter extends TabularExporter {
  get contentType() { return 'text/csv'; }
  header() { return 'name,value'; }
  row(m) { return `${m.name},${m.value.toFixed(2)}`; }
}

class JsonExporter extends Exporter {
  get contentType() { return 'application/json'; }

  exportAll(metrics) {
    const entries = metrics.map(
      (m) => `{"name": "${m.name}", "value": ${m.value.toFixed(2)}}`
    );
    return `[${entries.join(', ')}]`;
  }
}

function deliver(exporter, metrics) {
  console.log(`--- ${exporter.contentType} -> ${exporter.fileName()} ---`);
  console.log(exporter.exportAll(metrics));
  console.log();
}

const metrics = [
  new Metric('cpu', 0.93),
  new Metric('memory', 0.67),
  new Metric('disk', 0.41),
];

deliver(new CsvExporter(), metrics);
deliver(new JsonExporter(), metrics);
