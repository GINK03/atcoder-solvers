
fun main(args:Array<String>) {
  val map = mutableMapOf<String, Int>()
  val m = readLine()!!.toInt()
  (1..m).map { 
    val e = readLine()!!
    if( map.get(e) == null ) 
      map[e] = 0
    map[e] = map[e]!! + 1 
  }
  val n = readLine()!!.toInt()
  (1..n).map { 
    val e = readLine()!!
    if( map.get(e) == null ) 
      map[e] = 0
    map[e] = map[e]!! - 1 
  }

  val max = map.toList().sortedBy { 
    it.second 
  }.last()

  val maxnum = max.second
  when {
    maxnum <= 0 -> 0
    else -> maxnum
  }.let(::println)
}
