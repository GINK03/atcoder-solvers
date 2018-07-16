
fun main(args:Array<String>) {
  val n = readLine()!!.toInt()
  when { n%2 == 0 -> n; else -> n*2 }.run(::println)
}
