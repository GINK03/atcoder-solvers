
fun main( args : Array<String> ) {
  val n = readLine()!!.toInt()
  println( ( (1..n).map { it*10000 }
              .reduce { y,x -> y+x}.toDouble() / n ).toInt() )
}
