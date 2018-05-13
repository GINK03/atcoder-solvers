
fun main(args:Array<String>) {
  var (a, b, c, x, y) = readLine()!!.split(" ").map(String::toInt)
  a = a/2
  b = b/2
  c = c/2 
  val bi:List<()->Int> = listOf({  
      val max = listOf(x, y).max()!!
      val cost = max*c*2*2
      cost
    }, 
    {
      val cost = b*y*2 + a*x*2
      cost
    },
    {
      var cost = x*c*2*2
      val y2 = y - x
      if( y2 > 0 ) {
        cost += b*y2*2
      }
      cost
    },
    {
      var cost = y*c*2*2
      val x2 = x - y
      if( x2 > 0 ) {
        cost += a*x2*2
      }
      cost
    })
  println( bi.map { it() }.min() ) 
}
