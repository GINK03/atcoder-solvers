
fun main( args : Array<String> ) {
  readLine()?.let { 
    val (a, b) = it.split(" ").map { it.toInt() }
    println(b - a + 1)
  }
}
