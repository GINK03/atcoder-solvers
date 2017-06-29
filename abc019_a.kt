
fun main( a : Array<String> ) { 
  readLine()!!.split(" ").map { it.toInt() }.sorted()[1].let { println(it) }
}
