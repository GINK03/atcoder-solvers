
fun main(args:Array<String>) {
  val (a, b, x) = readLine()!!.split(" ").map(String::toInt)
  when {
    a <= x && x <= a+b -> "YES"
    else -> "NO"
  }.let(::println)
}
