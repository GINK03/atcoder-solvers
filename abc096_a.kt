
fun main(args:Array<String>) {
  val (a, b) = readLine()!!.split(" ").map(String::toInt)
  when {
    a <= b -> println(a)
    else -> println(a-1)
  }
}
