
fun main( args : Array<String> )  {
  val ba = (1..4).map { readLine()!!.split(" ").toMutableList() }
  val ta = (1..4).map { (1..4).map { "I" }.toMutableList() }
  (0..ba.size-1).map { y ->
    val swapY = ba.size-1 - y
    (0..ba[0].size-1).map { x ->
      val swapX = ba[0].size-1-x
      ta[swapY][swapX] = ba[y][x]
    }
  }
  ta.map { it.joinToString(" ") }.map { println(it) }
}
