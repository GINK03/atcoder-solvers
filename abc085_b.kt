
fun main(args:Array<String>){ 
  val n = readLine()!!.toInt()
  (1..n).map { readLine() }.toSet().size.let(::println)
}
