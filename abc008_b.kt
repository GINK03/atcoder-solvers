
fun main( args : Array<String> ) {
  val n = readLine()!!.toInt()
  val a = (1..n).map {
    readLine()!!
  }.groupBy( 
    {it}, {1}
  ).map { kv ->
    val (k,v) = kv
    Pair(k, v.size)
  }.sortedBy { 
    it.second
  }
  println(a.last().first)
}
