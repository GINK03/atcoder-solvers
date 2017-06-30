
fun main( args : Array<String> ) { 
  (1..3).map { 
    val (n, m) = readLine()!!.split(" ").map { it.toInt() }
    (n*m*0.1).toInt()
  }.reduce { y,x -> y+x }
  .let { println(it) } 
}
