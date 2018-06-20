
fun main(args:Array<String>) {
  val (M, n) = readLine()!!.split(" ").map(String::toInt)

  (1..n).map { 
    val (a,b) = readLine()!!.split(" ").map(String::toInt) 
    listOf( Pair(a,b), Pair(b,a) )
  }.flatten().let {
    val m = mutableMapOf<Int,MutableList<Int>>()
    it.map { 
      val (key,value) = it
      //lprintln(it)
      if( m[key] == null ) m[key] = mutableListOf()
      m[key]!!.add( value )
    }
    //println(m)
    m.toList().map { it.second }.any { it.contains(1) && it.contains(M) }.let { when(it) { true -> "POSSIBLE"; else -> "IMPOSSIBLE" } }.run(::println) 
  }
}
