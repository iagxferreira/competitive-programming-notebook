import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        FastScanner in = new FastScanner();
        StringBuilder out = new StringBuilder();
        solve(in, out);
        System.out.print(out);
    }

    private static void solve(FastScanner in, StringBuilder out) throws IOException {
        // TODO: solve the problem
    }

    private static final class FastScanner {
        private final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        private StringTokenizer tokens;

        String next() throws IOException {
            while (tokens == null || !tokens.hasMoreTokens()) {
                String line = reader.readLine();
                if (line == null) return null;
                tokens = new StringTokenizer(line);
            }
            return tokens.nextToken();
        }

        int nextInt() throws IOException { return Integer.parseInt(next()); }
        long nextLong() throws IOException { return Long.parseLong(next()); }
    }
}
