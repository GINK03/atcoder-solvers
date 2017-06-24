
fun main(args: Array<String>) { 
  val (a1, a2) = readLine()!!.split(" ").map { x -> x.toInt() }
  val n        = readLine()!!.toInt()
  (1..n).map { 
    readLine()!!.toInt()
  }.map { x ->
    when {
      a1 >= x              -> println(a1 - x)
      a1 < x   &&  x <= a2 -> println(0)
      a2 < x               -> println(-1)
    }
  }
}
