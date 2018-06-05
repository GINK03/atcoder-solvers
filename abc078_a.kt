
fun main(args:Array<String>) {
  val (a, b) = readLine()!!.split(" ")
  when {
    a > b -> ">"
    a < b -> "<"
    else -> "="
  }.let(::println)
}
