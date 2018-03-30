
fun main(args:Array<String>) {
  val train = (1..2).map { readLine()!!.toInt() }.min()!!
  val bas   = (1..2).map { readLine()!!.toInt() }.min()!!
  println( train + bas )
}
