
fun main( args : Array<String> ) {
  val n  = readLine()!!.toInt()
  val ss = readLine()!!.split(" ").map { it.toString() }
  var bu = mutableListOf<String>()
  for(i in (0..n-1) ) {
    if( i%2 == 0 )
      bu.add( ss[i] )
    else
      bu.add( 0, ss[i] )
  }
  if( n%2 == 0 )
    println(bu.joinToString(" "))
  else
    println(bu.reversed().joinToString(" ") )
}
