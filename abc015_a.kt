
fun main( args : Array<String> ) { 
  (1..2).map { 
    readLine()!!
  }.sortedBy {
    it.length
  }.last().let {
    println(it)
  }
}
