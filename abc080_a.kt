
fun main(args:Array<String>) {
  val (a,b,c) = readLine()!!.split(" ").map(String::toInt) 
  listOf(a*b, c).min().let(::println)
}
