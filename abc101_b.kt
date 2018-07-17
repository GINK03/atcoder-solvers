
fun main(args:Array<String>) {
  val n = readLine()!!
  val b1 = n.toList().map(Char::toString).map(String::toInt).sum()
  val b2 = n.toInt()

  when( b2%b1 ) { 
    0 -> "Yes" 
    else -> "No"
  }.run(::println)
}
