
fun main( args : Array<String> ) {
  val t = readLine()!!.toInt()
  val n = readLine()!!.toInt()
  val ts = readLine()!!.split(" ").map { it.toInt() }
  val m = readLine()!!.toInt()
  val cs = readLine()!!.split(" ").map { it.toInt() }

  val mts = ts.toMutableList()
  cs.map { c ->
    val toTrim = mts.mapIndexed{i,x ->
      Pair(i,x) 
    }.filter { 
      c - it.second  >= 0 && c - it.second <= t 
    }.let { 
      when {
        it.size > 0 -> it.first().first
        else        -> null
      }
    }
    if( toTrim != null ) 
      mts.removeAt(toTrim)
    toTrim
  }.all { 
    it != null
  }.let {
    when(it) {
      true -> "yes"
      else -> "no"
    }.let { println(it) }
  }
}
