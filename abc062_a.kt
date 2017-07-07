
fun main( args : Array<String> ) {
  val bs = readLine()!!.split(" ").map { it.toInt() }
 
  bs.map { a ->
    when {
      listOf(1,3,5,7,8,10,12).contains(a) -> 0
      listOf(4,6,9,11).contains(a) -> 1
      listOf(2).contains(a) -> 2
      else -> null
    }
  }.let { 
    val (a, b) = it
    when {
      a == b -> "Yes"
      else   -> "No"
    }.let { 
      println( it )
    }
  }

}
