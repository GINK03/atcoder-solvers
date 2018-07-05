
fun main(args:Array<String>) {
  val (a, b) = readLine()!!.split(" ").map(String::toInt)
  when { 
    a <= 8 && b <= 8 && a + b <= 16 -> "Yay!"
    else -> ":("
  }.run(::println)
}
