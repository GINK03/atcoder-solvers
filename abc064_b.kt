
fun main( args : Array<String> ) {
  val n = readLine()
  readLine()!!.split(" ").map { it.toInt() }.sorted().let { println(it.last() - it.first()) }
}
