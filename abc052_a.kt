
fun main(args : Array<String>) { 
  val (a, b, c, d) = readLine()!!.split(" ").map { x -> x.toInt() }
  println(listOf(a*b, c*d).max())
}
