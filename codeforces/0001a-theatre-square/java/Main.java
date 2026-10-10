// Solution.
//
// Scanner is far too slow for competitive input and is the most common
// cause of a Java TLE on a solution that is algorithmically correct.
// This uses BufferedReader + StringTokenizer, which is fast enough for
// anything you will meet and robust about mixed token/line input.

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        // Deep recursion overflows the default ~512KB stack somewhere
        // around depth 10^4. Run the real work on a thread with a big one.
        new Thread(null, Main::run, "main", 1 << 28).start();
    }

    static void run() {
        try (FastReader in = new FastReader()) {
            StringBuilder sb = new StringBuilder();

            int t = 1;
            // t = in.nextInt();            // uncomment for multi-test problems
            while (t-- > 0) solve(in, sb);

            System.out.print(sb);
        } catch (IOException e) {
            throw new UncheckedIOException(e);
        }
    }

    static void solve(FastReader in, StringBuilder sb) throws IOException {
        // ...
    }

    /** One reader over System.in. Never open a second one: they each
     *  buffer, and the two will silently eat each other's input. */
    static final class FastReader implements Closeable {
        private final BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in), 1 << 16);
        private StringTokenizer st = new StringTokenizer("");

        String next() throws IOException {
            while (!st.hasMoreTokens()) {
                String line = br.readLine();
                if (line == null) return null;
                st = new StringTokenizer(line);
            }
            return st.nextToken();
        }

        int nextInt() throws IOException { return Integer.parseInt(next()); }
        long nextLong() throws IOException { return Long.parseLong(next()); }
        double nextDouble() throws IOException { return Double.parseDouble(next()); }

        /** Reads the rest of the CURRENT line if tokens remain, otherwise
         *  the next one. Mixing this with next() is where line-based input
         *  usually goes wrong. */
        String nextLine() throws IOException {
            if (st.hasMoreTokens()) return st.nextToken("\n");
            return br.readLine();
        }

        int[] nextIntArray(int n) throws IOException {
            int[] a = new int[n];
            for (int i = 0; i < n; i++) a[i] = nextInt();
            return a;
        }

        @Override public void close() throws IOException { br.close(); }
    }

    /** Arrays.sort(int[]) is dual-pivot quicksort, with adversarial
     *  O(n^2) inputs that get hacked on Codeforces. Shuffle first.
     *  (Arrays.sort on a boxed Integer[] uses TimSort and is safe, but
     *  boxing costs far more than this shuffle.) */
    static void sort(int[] a) {
        Random r = new Random();
        for (int i = a.length - 1; i > 0; i--) {
            int j = r.nextInt(i + 1);
            int tmp = a[i]; a[i] = a[j]; a[j] = tmp;
        }
        Arrays.sort(a);
    }
}
