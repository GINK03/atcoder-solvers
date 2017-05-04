
fun main(args :Array<String>){ 
  val (M, N) = readLine()!!.split(" ").map { x -> x.toInt() } 

  val ms = (1..M).toList().map { x ->
    readLine()!!.toList()
  }
  val ns = (1..N).toList().map { x ->
    readLine()!!.toList()
  }
  val k = (0..M-N).map { x ->
    val a = (0..M-N).map { y ->
      val s = (0..N-1).map { ty ->
        (0..N-1).map { tx -> 
          //println("$ty, $tx")
          ns[ty][tx] == ms[y + ty][x + tx]
        }
      }.flatMap { x -> 
        x 
      }.all { x ->
        x 
      }
      s
    }.any { x ->
      x
    }
    a
  }.any { x ->
    x 
  }
  if( k == true ) {
    println("Yes")
  } else {
    println("No")
  }
}
