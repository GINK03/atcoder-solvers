
fun main(args:Array<String>) {
  val (n,x) = readLine()!!.split(" ").map(String::toInt)
  val cs = (1..n).map {
    readLine()!!.toInt()
  }
  val sum = cs.sum()
  println( (x - sum)/cs.min()!! + cs.size)
}
