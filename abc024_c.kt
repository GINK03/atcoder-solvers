
fun main( args : Array<String> ) {
  val (a,b) = readLine()!!.split(" ").map { x -> x.toInt() }
  val cs    = readLine()!!.toList().map { x -> x.toString() }

  var ret   = "NO"
  search@ for( i in (0..cs.size-b) ) { 
    val d = cs.slice(i..i+b-1).toSet()
    // search next
    for( k in (i+b..cs.size-b) ) {
      val e = cs.slice(k..k+b-1).toSet()

      if( d == e ) {
        ret = "YES"
        break@search 
      }
    }
  }
  println( ret )
}
