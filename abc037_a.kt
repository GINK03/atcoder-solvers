
fun main(args:Array<String>) { 
  val (a, b, c) = readLine()!!.split(" ").map { x -> x.toInt() }
  val r = listOf(c/a, c/b).max()
  println(r)
}
