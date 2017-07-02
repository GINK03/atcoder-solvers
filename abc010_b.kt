
fun main( args : Array<String> ) {
  val n = readLine()!!.toInt()
  readLine()!!
    .split(" ")
    .map { it.toInt() }
    .map {
      (1..it).map { x ->
        when {
          x%2 == 0 || x%3 == 2 -> false
          else                 -> true
        }
      }.reversed()
      .takeWhile { it == false }
      .size
      //.let { println(it) }
    }.reduce { y,x ->
      y+x
    }.let { 
      println(it)
    }
}
