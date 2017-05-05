
fun main(args : Array<String>) { 
  val (K, S) = readLine()!!.split(" ").map { x -> x.toInt() } 
  val r = (0..K).map { x ->
    (0..K).map { y ->
      val z = S - x - y
      if(0 <= z && z <= K) {
        //println("$x, $y, $z")
        1
      } else { 
        0
      }
    }
  }.flatMap { x ->
    x
  }.reduce { x,y ->
    x+y
  }
  println(r)
}
