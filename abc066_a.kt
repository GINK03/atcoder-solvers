
fun main( args : Array<String> ) {
  readLine()!!.split(" ")
    .map { it.toInt() }
    .sorted()
    .let { 
      val (a, b, c) = it
      println( a + b )
    }

}
