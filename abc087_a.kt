
fun main(args:Array<String>) {
  val (x,a,b) = (1..3).map { readLine()!!.toInt() }
  println( (x - a)%b )
}
