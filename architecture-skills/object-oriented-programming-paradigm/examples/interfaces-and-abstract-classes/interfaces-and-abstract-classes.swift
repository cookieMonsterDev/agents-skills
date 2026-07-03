// Interfaces & abstract classes in Swift.
//
// A protocol is the pure contract; a protocol extension with default
// implementations plays the abstract-class role. TabularExporter is a
// helper protocol; JsonExporter conforms to Exporter directly.

import Foundation

struct Metric {
    let name: String
    let value: Double
}

protocol Exporter {
    var contentType: String { get }
    func exportAll(metrics: [Metric]) -> String

    func fileName() -> String {
        "report." + contentType.split(separator: "/").last!
    }
}

protocol TabularExporter: Exporter {
    func header() -> String
    func row(metric: Metric) -> String
}

extension TabularExporter {
    func exportAll(metrics: [Metric]) -> String {
        var lines = [header()]
        lines += metrics.map { row(metric: $0) }
        lines.append("# \(metrics.count) records")
        return lines.joined(separator: "\n")
    }
}

struct CsvExporter: TabularExporter {
    var contentType: String { "text/csv" }
    func header() -> String { "name,value" }
    func row(metric: Metric) -> String {
        String(format: "%@,%.2f", metric.name, metric.value)
    }
}

struct JsonExporter: Exporter {
    var contentType: String { "application/json" }

    func exportAll(metrics: [Metric]) -> String {
        let entries = metrics.map {
            String(format: #"{"name": "%@", "value": %.2f}"#, $0.name, $0.value)
        }
        return "[\(entries.joined(separator: ", "))]"
    }
}

func deliver(exporter: Exporter, metrics: [Metric]) {
    print("--- \(exporter.contentType) -> \(exporter.fileName()) ---")
    print(exporter.exportAll(metrics: metrics))
    print()
}

let metrics = [
    Metric(name: "cpu", value: 0.93),
    Metric(name: "memory", value: 0.67),
    Metric(name: "disk", value: 0.41),
]

deliver(exporter: CsvExporter(), metrics: metrics)
deliver(exporter: JsonExporter(), metrics: metrics)
