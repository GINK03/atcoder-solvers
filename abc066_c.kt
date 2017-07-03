
fun main( args : Array<String> ) {
  val n  = readLine()!!.toInt()
  val ba = readLine()!!.split(" ").map { it.toInt() }

  var ta = mutableListOf<Int>()
  ba.map { x ->
    ta.add( x )
    ta = ta.reversed().toMutableList()
  }
  println( ta.joinToString(" ") )
}
