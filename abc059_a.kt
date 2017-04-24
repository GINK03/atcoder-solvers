

fun main(args: Array<String>) { 
  val result = readLine()!!.split(" ").map { x ->
   x.toList().first()
  }.joinToString("").toUpperCase()
  println(result)
}
