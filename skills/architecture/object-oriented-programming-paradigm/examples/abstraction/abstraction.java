// Abstraction in Java.
//
// The abstraction is an interface: callers see save/load and nothing
// else, while each implementation hides its operational detail (a
// HashMap vs a file). The client method takes NoteStore and runs
// unchanged when the implementation behind it swaps.

import java.io.IOException;
import java.io.UncheckedIOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

public class abstraction {

    /** The abstraction: the only surface callers may rely on. */
    interface NoteStore {
        void save(String key, String text);
        Optional<String> load(String key);
    }

    /** Operational detail: a HashMap. Callers never see it. */
    static final class MemoryStore implements NoteStore {
        private final Map<String, String> notes = new HashMap<>();

        public void save(String key, String text) {
            notes.put(key, text);
        }

        public Optional<String> load(String key) {
            return Optional.ofNullable(notes.get(key));
        }
    }

    /** Operational detail: append-only lines in a file, last write wins. */
    static final class FileStore implements NoteStore {
        private final Path path;

        FileStore(Path path) {
            this.path = path;
        }

        public void save(String key, String text) {
            try {
                Files.writeString(path, key + "\t" + text + "\n",
                        StandardOpenOption.CREATE, StandardOpenOption.APPEND);
            } catch (IOException e) {
                throw new UncheckedIOException(e);
            }
        }

        public Optional<String> load(String key) {
            if (!Files.exists(path)) return Optional.empty();
            try {
                String found = null;
                for (String line : Files.readAllLines(path)) {
                    String[] parts = line.split("\t", 2);
                    if (parts.length == 2 && parts[0].equals(key)) {
                        found = parts[1]; // keep scanning: last write wins
                    }
                }
                return Optional.ofNullable(found);
            } catch (IOException e) {
                throw new UncheckedIOException(e);
            }
        }
    }

    /** Client: written once against the abstraction, never edited when
     *  the implementation behind it swaps. */
    static void runSession(NoteStore store) {
        store.save("groceries", "eggs, flour");
        store.save("groceries", "eggs, flour, milk"); // overwrite
        store.save("idea", "hide the how, expose the what");
        System.out.println("  groceries: " + store.load("groceries").orElse("(missing)"));
        System.out.println("  idea:      " + store.load("idea").orElse("(missing)"));
        System.out.println("  missing:   " + store.load("missing").orElse("(missing)"));
    }

    public static void main(String[] args) throws IOException {
        System.out.println("memory-backed store:");
        runSession(new MemoryStore());

        Path path = Path.of("abstraction_demo.txt");
        System.out.println("file-backed store:");
        runSession(new FileStore(path));
        Files.deleteIfExists(path);
    }
}
