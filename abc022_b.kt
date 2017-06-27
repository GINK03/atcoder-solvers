
fun main( args : Array<String> ) { 
  val n      = readLine()!!.toInt()
  val stores = mutableSetOf<Int>()
  val ss = (1..n).map { 
    val type = readLine()!!.toInt() 
    if( !stores.contains( type ) ) {
      stores.add( type ) 
      false
    } else {
      true
    }
  } 
  println( ss.count { it == true } )
}
