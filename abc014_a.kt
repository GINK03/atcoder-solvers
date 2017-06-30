
fun main( args : Array<String> ) {
  val (a, b) = (1..2).map { readLine()!!.toInt() }
  println((b - a%b)%b)
}
