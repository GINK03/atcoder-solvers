
fun main(args : Array<String>) { 
  val (n, m) = readLine()!!.split(" ").map { x -> x.toInt() }
  val b:MutableList<Long> = readLine()!!.split(" ").map { x -> x.toLong() }.toMutableList()
  (0 .. m - 2).map { x ->
    b[x] = (x+1) * b[x]
  }
  (m-1 .. b.size - m).map { x ->
    b[x] = m * b[x]
  }
  var f = m - 1
  (b.size -m + 1 .. b.size - 1).map { x ->
    b[x] = f * b[x]
    f--
  }
  //println( b )
  println( b.sum() )

}
