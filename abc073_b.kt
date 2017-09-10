
fun main( args : Array<String> ) {
  val n = readLine()!!.toInt()
  (1..n).map {
    val (a, b) = readLine()!!.split(" ").map { it.toInt() }
    b - a + 1
  }.sum().let { println(it) }
}
