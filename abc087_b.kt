
fun main(args:Array<String>) {
  val (c500s, c100s, c50s, N) = (0..3).map{ readLine()!!.toInt() }
  var count = 0
  for( c500 in (0..c500s) ) {
    for( c100 in (0..c100s) ) {
      for( c50 in (0..c50s) ) {
        if( c500*500 + c100*100 + c50*50 == N )
          count++
      }
    }
  }
  println(count)
}

