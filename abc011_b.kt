
fun main( args : Array<String> ) {
  readLine()?.let {
    it.toLowerCase()
      .capitalize()
      .let { println(it) } 
  }
}
