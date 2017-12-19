
fun main(args : Array<String>) {
  val m = readLine()!!.toDouble()
  val k = m/1000
  val vv:Double = when {
    k < 0.1 -> 0.0
    k <= 5.0 -> k*10 
    6 <= k && k <= 30 -> k + 50
    35 <= k && k <= 70 -> (k - 30)/5 + 80
    70 < k -> 89.0
    else -> k
  }

  val s = vv.toInt().toString()
  if( s.length == 1 ) {
    println("0${s}")
  } else {
    println("${s}")
  }
}
