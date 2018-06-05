
fun main(args:Array<String>) {
  val s = readLine()!!.toList().sorted().joinToString("")
  val t = readLine()!!.toList().sorted().reversed().joinToString("")
  
  when {
    s < t -> "Yes"
    else -> "No"
  }.let(::println)
}
