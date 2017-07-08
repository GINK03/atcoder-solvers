
fun main( args : Array<String> ) {
  val (a,b,c) = readLine()!!.split(" ").map { it.toInt() }
  when {
    a <= c && c <= b -> "Yes"
    else -> "No"
  }.let { println(it) }
}
