
fun main( args : Array<String> ) {
  val n = readLine()
  readLine()!!.split(" ")
  .map {
    val x = it.toInt()
    listOf(x-1, x, x+1)
  }.flatten()
  .groupBy {
    it
  }.toList()
  .map {
    it.second.size
  }.max()
  .let {
    println(it)
  }
}
