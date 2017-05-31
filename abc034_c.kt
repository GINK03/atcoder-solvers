
fun main(args : Array<String>) { 
  val (a, b) = readLine()!!.split(" ").map { x -> x.toLong() }
  (1..a+b-2).toList().reduce { y, x ->
    (y %1000000007L) * (x % 1000000007L)
  }
}
