

fun main(args :Array<String>) { 
  val n    = readLine()!!.toLong()
  val base = 1000000007L
  val r    = (1..n).reduce ( { x,y ->
    x*y%base
  })
  println(r)
}
