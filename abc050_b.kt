
fun main( args : Array<String> ) {
  val N  = readLine()!!.toInt()
  val Ts = readLine()!!.split(" ").map { x -> x.toInt() }
  val M  = readLine()!!.toInt()
  val px = (1..M).map { x -> 
    val (m, x) = readLine()!!.split(" ").map { x -> x.toInt() }
    Pair(m, x)
  }.toList().map { xy -> 
    val (x, y) = xy
    val ts     = Ts.toMutableList()
    ts[x-1] = y
    println( ts.sum() )
  }
   
}
