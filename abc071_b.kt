
fun main( args : Array<String> ) {
  val s = "abcdefghijklmnopqrstuvwxyz".toSet()
  val t = readLine()!!.toSet()
  (s - t).toList().sorted().let {
    when {
      it.size > 0 -> it.first().toString() 
      else -> "None"
    }.let { println(it) }
  }
}
