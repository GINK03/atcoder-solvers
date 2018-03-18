
fun main(args:Array<String>) {
  val (a, b, c) = readLine()!!.split(" ").map { it.toInt() }
  when { 
    a + b >= c -> "Yes"
    else -> "No"
  }.let { println(it) }
}
