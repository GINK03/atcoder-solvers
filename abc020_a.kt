
fun main( a : Array<String> ) {
  val b = readLine()!!.toInt()
  when (b) {
    1    -> "ABC"
    2    -> "chokudai"
    else -> null
  }.let { println(it) }
}
