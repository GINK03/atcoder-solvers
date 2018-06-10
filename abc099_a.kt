
fun main(args:Array<String>) { 
  val n = readLine()!!.toInt()
  when {
    n >= 1000 -> "ABD"
    else -> "ABC"
  }.run(::println)
}
