
fun main( args : Array<String> ) { 
  val ml    = readLine()!!.toMutableList()
  val n     = readLine()!!.toInt()
  (1..n).map { 
    val (s, e)   = readLine()!!.split(" ").map { it.toInt() } 
    ml
      .slice(s-1..e-1)
      .reversed()
      .mapIndexed { i, x ->
        ml[i+s-1] = x
      }
  }
  println( ml.joinToString("") )
}
