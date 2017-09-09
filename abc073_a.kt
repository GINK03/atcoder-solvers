
fun main( args : Array<String> ) {
  when { 
    readLine()!!.contains("9") -> "Yes"
    else -> "No"
  }.let { println(it) }
}
