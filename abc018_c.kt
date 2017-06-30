
fun main( args : Array<String> ) {
  val (R, C, K) = readLine()!!.split(" ").map { it.toInt() }
  (1..R).map {
    readLine()!!.toMutableList()
  }.toMutableList().let { println(it) }
}
