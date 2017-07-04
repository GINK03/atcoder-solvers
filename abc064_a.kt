


fun main( args : Array<String> ) {
  when { 
    readLine()!!.split(" ").joinToString("").toLong() % 4  == 0L -> "YES"
    else -> "NO"
  }.let { println(it) }
}
