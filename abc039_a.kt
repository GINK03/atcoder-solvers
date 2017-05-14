
fun main(args : Array<String>) {
  val (a,b,c) = readLine()!!.split(" ").map { x -> x.toInt() }
  println( (a*b+b*c+c*a)*2 )
}
