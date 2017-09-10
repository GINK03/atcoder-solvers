
fun main( args : Array<String> ) {
  val (x, t) = readLine()!!.split(" ").map { it.toInt() }
  when {
    x - t >= 0 -> x - t
    else -> 0
  }.let {
    println(it)
  }
}
