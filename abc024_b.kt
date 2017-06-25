
fun main( args : Array<String> ) { 
  val (a, b) = readLine()!!.split(" ").map { x -> x.toInt() }
  val cs = (1..a).map { 
    readLine()!!.toInt()
  }
  var buff = 0
  for( i in (0..cs.size-2) ) {
    val down = cs[i]
    val up   = cs[i+1]
    if( up - down <= b )
      buff += up - down
    else
      buff += b
  }
  println( buff + b )
}
