
fun main(args:Array<String>) {
  val xs = readLine()!!.split(" ").map(String::toInt)
  val (x1,y1) = xs.slice(0..1)
  val (x2,y2) = xs.slice(2..3)
  val (x3,y3) = xs.slice(4..5)

  val xa2 = x2 - x1
  val ya2 = y2 - y1
  val xa3 = x3 - x1
  val ya3 = y3 - y1
  
  (Math.abs( xa2*ya3 - xa3*ya2 ).toDouble()/2).run(::println)
}
