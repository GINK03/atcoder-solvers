
fun main( args : Array<String> ) { 
  val (y,m,d) = (1..3).map { readLine()!!.toInt() }
  var (m2,y2) = when { 
                  m == 1 || m == 2 -> { 
                    Pair( m + 12, y - 1 )
                  }
                  else -> Pair( m, y )
                }
  println("$y $m2 $d")

  val a = 735369 - (365*y2 + y2/4 - y2/100 + y2/400 + 306*(m2+1)/10 + d - 429)
  println( a )
}
