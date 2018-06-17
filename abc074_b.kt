
fun main(args:Array<String>) {
  val n = readLine()!!.toInt()
  val k = readLine()!!.toInt()
  val xs = readLine()!!.split(" ").map(String::toInt)

  xs.map { listOf( Math.abs(k - it), it ).min()!!*2 }.sum().run(::println)
}
