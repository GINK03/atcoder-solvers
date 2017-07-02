
fun main( args : Array<String> ) {
  val n = readLine()!!.toInt()
  (1..n).map {
    readLine()!!.toInt()
  }.toSet()
  .toList()
  .sorted()
  .reversed()[1].let { println(it) }
}
