
fun main(args:Array<String>) {
  val t = readLine()!!.toLong()

  val num = t/11L
  val delta = when { t%11L > 6 -> 2; t%11L > 0 -> 1; else -> 0 }

  println(num*2 + delta )
}
