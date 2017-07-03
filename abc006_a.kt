
fun main( args : Array<String> ) {
  readLine()!!.toInt().let { 
    when {
      it%3 == 0 -> "YES"
      else -> "NO"
    }.let { println(it) }
  }
}
