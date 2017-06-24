
fun main( args : Array<String> ) { 
  val s = readLine()!!.toList().map { x -> x.toString() }
  val k = readLine()!!.toInt()
  val n = mutableSetOf<String>()
  s.map { x ->
    s.map { y ->
      n.add( x + y )
    }
  }
  val m = n.toList()
    .sortedBy { x ->
      x
    }.mapIndexed { i, x ->
      Pair(i+1,x)
    }.toMap()
  println( m[k] )
}
