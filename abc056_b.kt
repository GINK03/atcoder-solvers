fun main(args:Array<String>) {
  val (w, a, b) = readLine()!!.split(" ").map { x -> x.toInt() }
  val (a1, a2) = Pair(a - w, a + w)
  if( a1 <= b && b <+ a2 ) { 
    println(0)
  }else {
    println( listOf(a1, a2).map { x ->
      b - x
    }.map { x -> 
      Math.abs(x)
    }.min() )
  }
}
