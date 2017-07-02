
fun main( args : Array<String> ) {
  readLine()?.let { 
    val a = (it.toInt() + 1)%12
    when (a) {
      0 -> 12
      else -> a 
    }.let { println(it) }
  }
}
