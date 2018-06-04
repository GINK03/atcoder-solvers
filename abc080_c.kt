
fun main(args:Array<String>) {
  val n = readLine()!!.toInt()
  val onehots = (1..n).map {
    readLine()!!.split(" ").map(String::toInt)
  }
  val gains = (1..n).map { 
    readLine()!!.split(" ").map(String::toInt)
  }

  val result = mutableListOf<Int>()
  (0..1).map { a1 -> (0..1).map { a2 -> (0..1).map { a3 -> (0..1).map { a4 -> (0..1).map { a5 -> (0..1).map { a6 -> (0..1).map { a7 -> (0..1).map { a8 -> (0..1).map { a9 -> (0..1).map { a10 -> 
    val b = listOf(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)
    if( b.sum() != 0 ) {  
      val gain = onehots.mapIndexed { index, onehot ->
        val query = b.zip( onehot ).toList<Pair<Int, Int>>().map { it ->
          val (a, hot) = it
          a*hot 
        }.sum()

        val gain = gains[index][query]

        gain
      }.sum()

      result.add( gain )
      //println(b)
    }
  } } } } } } } } } }

  println( result.sorted().last() )
} 
