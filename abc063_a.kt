
fun main( args : Array<String> ) {
  val (a, b) = readLine()!!.split(" ").map { it.toInt() }
  when {
    a + b >= 10 -> "error"
    else -> a + b
  }.let { println(it) }
}
