
fun main(args : Array<String>) {
  val a = readLine()!!.toInt()
  val m = (1..a).map {
    val b = readLine()!!.split(" ")
    val n  = b[0]
    val na = b[1].toDouble()
    Pair(n, na)
  }.toMap()
  val to:Double = m.map { xy ->
    val (x, y) = xy
    y
  }.reduce { y,x -> 
    y + x
  }
  val n = m.map { xy ->
    val (x, y) = xy
    Pair(x, y/to > 0.5)
  }.filter { xy ->
    val (x, y) = xy
    y
  }
  when {
    n != listOf<Pair<String,Boolean>>() -> println(n[0].first)
    else -> println("atcoder")
  }
}
