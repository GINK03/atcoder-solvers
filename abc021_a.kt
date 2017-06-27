

fun main( args : Array<String> ) {
  val a = readLine()!!.toInt() 
  a.let {
    if( it % 2 == 0 ) {
      val l = it/2
      println( l )
      (1..l).map { println(2) }
    } else {
      val l = (it-1)/2
      println( l + 1 )
      println(1)
      (1..l).map { println(2) }
    }
  }
}
