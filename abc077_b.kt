
fun main(args:Array<String>) {
  val d = readLine()!!.toDouble()
  val sqrt = Math.sqrt(d)
  sqrt.run{ toLong() }.let { it*it }.run(::println)
}
