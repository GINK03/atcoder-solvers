import java.lang.Math
fun main( args : Array<String> ) { 
  val n = readLine()!!.toInt()
  var bs = (1..n).map { 
    readLine()!!.toInt()
  }.sortedBy { x ->
   x*-1
  }.mapIndexed { i,x ->
    val ret = when { 
      i%2 == 0 -> x*x
      else     -> -1*x*x
    }
    ret
  }
  val a = bs.reduce { x,y ->
    x+y
  }
  println( a*Math.PI )

}
