
fun main(args:Array<String>) {
  val a = readLine()!!.split(" ").map { x ->
    x.toInt()
  }.reduce { x, y ->
    x+y
  } % 24
  println(a)
}
