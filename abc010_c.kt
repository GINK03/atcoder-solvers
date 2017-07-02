import java.lang.Math
fun main( args : Array<String> ) {
  val dim = readLine()!!.split(" ").map { it.toDouble() } 
  val (t01, t02, t11, t12) = dim.slice(0..3)
  val t = dim[4]
  val v = dim[5]
  val n = readLine()!!.toInt()
  (1..n).map { 
    val (a, b) = readLine()!!.split(" ").map { it.toDouble() }
    val delta1 = Math.pow( Math.pow(t01 - a, 2.0) + Math.pow(t02 - b, 2.0), 0.5 )
    val delta2 = Math.pow( Math.pow(t11 - a, 2.0) + Math.pow(t12 - b, 2.0), 0.5 )
    delta1+delta2
  }.any {
    t >= it/v
  }.let {
    when(it) {
      true -> "YES"
      else -> "NO"
    }.let { 
      println(it)
    }
  }
}
