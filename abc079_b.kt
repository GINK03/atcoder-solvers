
fun main(args:Array<String>) {
  val m = listOf(2L, 1L).toMutableList()
  val n = readLine()!!.toInt()
  (2..n).map { 
    m.add( m[it-1] + m[it-2] )
  }
  println( m.last() )
}
