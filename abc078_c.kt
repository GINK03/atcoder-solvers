
fun main(args:Array<String>) {
  val (n, m) = readLine()!!.split(" ").map(String::toInt)
  val a1 = (1..m).map { 2 }.reduce { y, x -> y*x } 
  val a2 = (n - m)*100
  println((1900*m + a2)*a1)
  //println(a1)
}
