
fun main( args : Array<String> ) {
  val (a, b) = readLine()!!.split(" ").map { it.toInt() }

  val cs = readLine()!!
    .split(" ")
    .map { it.toInt() } 
    .mapIndexed { i,x ->
      Pair(i,x)
    }.toMap()
  
  Integer.toBinaryString(b)
    .toList()
    .reversed()
    .mapIndexed { i, x ->
      x.toString().toInt() * cs[i]!!.toInt()
    }.reduce { y,x ->
      y+x
    }.let { 
      println( it )
    }
}
