
fun main(args : Array<String>) {
  val i = readLine()!!.toDouble()
  val b = Math.pow(i, 0.5)
  val a = (b.toInt()..i.toInt()).toList().map { x ->
    Triple(x, i.toInt()/x - x, i.toInt()%x)
  }.map { xyz -> 
    val (x, y, z) = xyz
    Math.abs(y) + z
  }.min()
  println(a)
}
