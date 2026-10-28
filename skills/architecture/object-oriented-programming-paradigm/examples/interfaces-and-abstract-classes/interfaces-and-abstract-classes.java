// Interfaces & abstract classes in Java.
//
// An interface is a pure contract; an abstract class mixes implemented
// and abstract members. TabularExporter captures shared line-assembly
// logic once; JsonExporter satisfies the contract directly.
//
// Java identifiers cannot contain hyphens, so a package-private class
// keeps the single-file launcher working: `java interfaces-and-abstract-classes.java`

import java.util.List;

class InterfacesAndAbstractClasses {

    record Metric(String name, double value) {}

    interface Exporter {
        String contentType();
        String exportAll(List<Metric> metrics);

        default String fileName() {
            String ct = contentType();
            return "report." + ct.substring(ct.indexOf('/') + 1);
        }
    }

    abstract static class TabularExporter implements Exporter {
        @Override
        public String exportAll(List<Metric> metrics) {
            StringBuilder out = new StringBuilder(header());
            for (Metric m : metrics) {
                out.append('\n').append(row(m));
            }
            return out.append("\n# ").append(metrics.size()).append(" records").toString();
        }

        protected abstract String header();
        protected abstract String row(Metric metric);
    }

    static final class CsvExporter extends TabularExporter {
        public String contentType() { return "text/csv"; }
        protected String header() { return "name,value"; }
        protected String row(Metric m) {
            return "%s,%.2f".formatted(m.name(), m.value());
        }
    }

    static final class JsonExporter implements Exporter {
        public String contentType() { return "application/json"; }
        public String exportAll(List<Metric> metrics) {
            StringBuilder out = new StringBuilder("[");
            for (int i = 0; i < metrics.size(); i++) {
                if (i > 0) out.append(", ");
                Metric m = metrics.get(i);
                out.append("{\"name\": \"").append(m.name())
                   .append("\", \"value\": ").append(m.value()).append('}');
            }
            return out.append(']').toString();
        }
    }

    static void deliver(Exporter exporter, List<Metric> metrics) {
        System.out.printf("--- %s -> %s ---%n",
                exporter.contentType(), exporter.fileName());
        System.out.println(exporter.exportAll(metrics));
        System.out.println();
    }

    public static void main(String[] args) {
        List<Metric> metrics = List.of(
                new Metric("cpu", 0.93),
                new Metric("memory", 0.67),
                new Metric("disk", 0.41)
        );
        deliver(new CsvExporter(), metrics);
        deliver(new JsonExporter(), metrics);
    }
}
