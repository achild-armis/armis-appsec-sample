import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class SamplePathTraversal {
    public static String readFile(String filename) throws IOException {
        Path baseDir = Paths.get("documents");

        // Vulnerable: user-controlled path is resolved without validation
        Path target = baseDir.resolve(filename);

        return Files.readString(target);
    }

    public static void main(String[] args) throws Exception {
        String filename = args.length > 0 ? args[0] : "readme.txt";
        System.out.println(readFile(filename));
    }
}
