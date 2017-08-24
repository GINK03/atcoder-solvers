
fun main( args : Array<String> ) {
  readLine()
  val bs = readLine()!!.split(" ").map {
    it.toInt()
  }.groupBy {
    it
  }.toList().map {
    val (k,vs) = it
    Pair(k,vs.size)
  }.filter {
    it.second >= 2
  }
  when {
    bs.size >= 2 -> { 
      val (a,b) = bs.sortedBy { 
        it.first * -1
      }.slice(0..1)
      .map {
        it.first
      }
      a*b
    }
    else -> 0
  }.let { 
    println(it)
  }
}
