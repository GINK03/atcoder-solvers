
fun main(args:Array<String>) { 
  val r = readLine()!!.split(" ").map { it.toDouble() }.sum() / 2.0
  println(Math.round(r))
}
