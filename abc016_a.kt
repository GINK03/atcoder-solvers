
fun main( args : Array<String> ) {
  readLine()!!
    .split(" ")
    .map { it.toInt() }
    .let { xy ->
      val (x, y) = xy
      when { 
        x%y == 0 -> "YES"
        else     -> "NO"
      }.let { 
        println(it) 
      }
    }
}
