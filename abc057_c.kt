fun main(args:Array<String>) {
  val t = readLine()!!.toLong()
  val a = (1..Math.pow(t.toDouble(), 0.5).toInt()).map { x ->
    if( t%x == 0L ) { 
      Pair(t/x, x)
    } else { 
      null
    }
  }.filter { x ->
    x != null
  }.map { x ->
    val m = x!!.toList().map { x -> x.toString().length }.max() 
    m!!.toInt()
  }.toList()
  println(a.min())
}
