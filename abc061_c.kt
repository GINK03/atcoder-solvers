
fun main(args:Array<String>) {
  val (N, K) = readLine()!!.split(" ").map(String::toInt)
  (1..N).map { 
    val (a, b) = readLine()!!.split(" ").map(String::toInt)
    Pair(a,b)
  }.sortedBy { it.first }.let { pairs ->
    var int = 0 
    for( pair in pairs ) {
      val (a,b) = pair
      //println(pair)
      int += b
      if( K <= int ) {
        println(a)
        break
      }
    }
  }
}
