
fun main(args : Array<String>) {
  val (a, b) = readLine()!!.split(" ").map { x -> x.toInt() }
  println( listOf( b - 1 , a - b).min() )
}
