
fun main(args : Array<String>) {
  val (a, b) = readLine()!!.split(" ").map { x -> x.toDouble() }
  println( Math.ceil(b/a).toInt() )
}
