
fun main(args : Array<String> ) { 
  readLine()
  readLine()!!.split(" ").mapIndexed { i,x ->
    Pair( i+1, x.toInt() )
  }.sortedBy { xy ->
    val (x, y) = xy
    y*-1
  }.map { xy ->
    val (x, y) = xy
    println(x)
  }
}
