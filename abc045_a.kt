
fun main( args :Array<String> ) {
  val (a,b,c) = (1..3).map { readLine()!!.toDouble() } 
  println( ((a+b)/2*c).toInt() )
}
