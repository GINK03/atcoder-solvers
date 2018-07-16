
fun main(args:Array<String>) {
  val n = readLine()
  val xs = readLine()!!.split(" ").map(String::toInt)
  (xs.max()!! - xs.min()!!).run(::println)
}
