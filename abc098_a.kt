
fun main(args:Array<String>) { 
  val (a,b) = readLine()!!.split(" ").map(String::toInt)
  listOf(a-b, a+b, a*b).max()!!.let(::println)
}
