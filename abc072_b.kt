
fun main( args : Array<String> ) {
  readLine()!!.toList()
  .mapIndexed { i, x ->
    Pair(i,x.toString())
  }.filter {
    it.first%2 == 0
  }.map {
    it.second
  }.joinToString("")
  .let { println(it) }
}
