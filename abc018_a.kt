

fun main( a : Array<String> ) {
  val bs = (1..3).map { 
    readLine()!!.toInt()
  }
  bs.sortedBy { x ->
    x*-1
  }
  .mapIndexed { i,x ->
    Pair(x, i+1)
  }.toMap()
  .let { 
    bs.map { x -> 
      println( "${it[x]}" )
    }
  }
}
