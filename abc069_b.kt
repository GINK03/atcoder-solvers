
fun main(args:Array<String>) {
  val s = readLine()!!
  val head = s.first()
  val last = s.last()
  val len = s.length-2
  println( "$head$len$last" )
}
