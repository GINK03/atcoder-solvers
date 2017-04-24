
fun main(args:Array<String>) { 
  val (M, N) = readLine()!!.split(" ").map { x -> x.toLong() }
  val man = (1..M).map { 
    readLine()!!.split(" ").map { x -> x.toLong() }
  }
  val checkpoints = (1..N).map { 
    readLine()!!.split(" ").map { x -> x.toLong() }
  }
  val ans = man.map { x ->
    checkpoints.mapIndexed { i, cp ->
      val m = x.zip(cp).map { x2 ->
        val (x3, x4) = x2
        Math.abs(x3 - x4)
      }.reduce { x, y ->
        x + y 
      }
      Pair(i+1, m)
    }.minBy { x ->
      val (i, m) = x
      m
    }
  }
  ans.map { a ->
   println(a!!.first)
  }
}
