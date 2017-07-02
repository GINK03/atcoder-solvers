
fun main( args : Array<String> ) {
  readLine()?.let {
    val i = it.toInt()
    when (i%2  == 0){
      true -> i/2
      else -> i/2+1
    }.let { println(it) }
  }
}
