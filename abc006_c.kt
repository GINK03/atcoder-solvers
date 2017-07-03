
fun main( args : Array<String> ) {
  val (n, m) = readLine()!!.split(" ").map { it.toInt() }
  var res: String = "-1 -1 -1"
  for( c in (0..m-2*n) ) { 
    val b = m - 2*n  -2*c
    if ( b < 0 ) break 
    val a = n - b -c
    if ( a < 0 ) continue
    res = "$a $b $c"
    break
  }
  println(res)
}
