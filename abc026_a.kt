
fun main( args : Array<String> ) { 
  val n   = readLine()!!.toInt()
  val ans = (1..n/2+1).map { x ->
    x * (n - x)
  }.sortedBy { x ->
    x*-1
  }.first()
  println( ans )
}
