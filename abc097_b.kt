
fun main(args:Array<String>) {
  val b = readLine()!!.toDouble()
  val c = (2..999).map {
    val ba = it.toDouble()
    val bb = Math.pow(b, 1/ba).toInt().toDouble()
    Math.pow(bb.toDouble(), ba).toInt()
  }.toList().max()!!
  println( c )
}
