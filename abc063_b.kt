
fun main( args : Array<String> ) {
  val xs = readLine()!!.toList()
  when {
    xs.size == xs.toSet().size -> "yes"
    else -> "no"
  }.let { println(it) }
}
