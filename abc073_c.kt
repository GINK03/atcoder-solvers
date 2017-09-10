
fun main( args : Array<String> ) {
  val m = mutableMapOf<Int, Int>()
  val n = readLine()!!.toInt()
  (1..n).map {
    val o = readLine()!!.toInt()
    when {
      m[o] == null -> m[o] = o
      else -> m.remove(o)
    }
  }
  println( m.size )
}
