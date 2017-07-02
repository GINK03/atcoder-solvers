
fun main( args : Array<String> ) {
  val n = readLine()!!.toInt()
  (1..9).map { i ->
    (1..9).map { k ->
      Pair(i*k, "${i} x ${k}")
    }
  }.flatMap { it }
  .groupBy({it.first}, {it.second})
  .let { 
    it[2025 - n]?.let {
      it.map { println(it) }
    }
  }
}
