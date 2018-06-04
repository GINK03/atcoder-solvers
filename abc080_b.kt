
fun main(args:Array<String>) {
  val input = readLine()!!

  val x = input.toInt()
  
  val fx = input.toList().map(Char::toString).map(String::toInt).sum()
  
  when {
    x % fx == 0 -> "Yes"
    else -> "No"
  }.let(::println)

}
