
fun main( args : Array<String> ) {
  val n = readLine()!!.toInt()
  val m = mutableMapOf<Int, Int>()
  (1..n).map { 
    val (a, b) = readLine()!!.split(" ").map { it.toInt() }
    (a..b).map { i ->
      if (m[i] == null) m[i] = 0
      m[i] = m[i]!! + 1
    }
  }
  println(m.values.max())

}

