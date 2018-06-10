
fun main(args:Array<String>) {
  val (a, b) = readLine()!!.split(" ").map(String::toInt)
  val delta = b - a
  
  val base = (1..delta-1).sum()
  //println(base)
  println(base - a)
}
