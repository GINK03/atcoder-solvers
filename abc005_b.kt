
fun main( args : Array<String> ){
  val n = readLine()!!.toInt()
  (1..n).map { readLine()!!.toInt() }
    .toSet()
    .sorted()
    .first()
    .let { println(it) }
}


