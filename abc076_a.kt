
fun main(args:Array<String>) {
  val (a,b) = (1..2).map { readLine()!!.toInt() }
  (2*b - a).run(::println)
}
