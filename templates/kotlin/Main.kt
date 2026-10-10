import java.io.BufferedInputStream

fun main() {
    val input = FastScanner()
    val output = StringBuilder()
    solve(input, output)
    print(output)
}

private fun solve(input: FastScanner, output: StringBuilder) {
    // TODO: solve the problem
}

private class FastScanner {
    private val input = BufferedInputStream(System.`in`)
    private val buffer = ByteArray(1 shl 16)
    private var length = 0
    private var position = 0

    private fun readByte(): Int {
        if (position >= length) {
            length = input.read(buffer)
            position = 0
            if (length <= 0) return -1
        }
        return buffer[position++].toInt()
    }

    fun next(): String? {
        val token = StringBuilder()
        var byte = readByte()
        while (byte >= 0 && byte <= 32) byte = readByte()
        while (byte > 32) {
            token.append(byte.toChar())
            byte = readByte()
        }
        return token.toString().ifEmpty { null }
    }
}
