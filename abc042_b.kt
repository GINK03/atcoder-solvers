
fun main(args : Array<String> )  { 
  val (n, l) = readLine()!!.split(" ").map { x -> x.toInt() }
  val r = (1..n).toList().map { x ->
    readLine()!!
  }.sortedBy { x ->
    x 
  }.joinToString("")
  println(r)
}
