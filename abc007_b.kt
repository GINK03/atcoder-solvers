
fun main( args : Array<String> ) {
  readLine()?.let {
    when(it) {
      "a" -> -1
      else -> 'a'
    }.let { println(it) }
  }
}
