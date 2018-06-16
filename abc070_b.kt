
fun main(args:Array<String>) {
  val (a,b,c,d) = readLine()!!.split(" ").map(String::toInt)
  ( listOf(b,d).min()!! - listOf(a, c).max()!! ).let { listOf(0, it).max()!! }.run(::println)
}
