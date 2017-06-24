
fun main( args : Array<String> ) { 
  val m = mutableMapOf<String, Int>()
  readLine()!!.split(" ").map { x ->
    if( m.get(x) == null ) 
      m[x] = 0
    m[x] = m[x]!! + 1
  }
  val n = m.toList().map { xy ->
    val (x,y) = xy
    Pair(y,x)
  }.toMap()
  if( n.get(1) != null )
    println( n[1]!! )
  else
    println( n[3]!! )
}
