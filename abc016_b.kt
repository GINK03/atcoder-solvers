
fun main( args : Array<String> ) {
  readLine()!!
    .split(" ")
    .map { it.toInt() }
    .let { 
      val (a, b, c) = it
      when {
        a - b == c && a + b == c -> "?"
        a - b == c          -> "-"
        a + b == c          -> "+"
        else                -> "!"
      }.let {
        println(it)
      }
    }
}
