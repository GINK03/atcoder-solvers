
fun main( args : Array<String> ) {
  val (x, a, b) = readLine()!!.split(" ").map { it.toInt() }
  val expire    = b - a
  when {
    expire > x -> "dangerous"
    expire <= 0 -> "delicious"
    else -> "safe"
  }.let { println( it ) }
}
