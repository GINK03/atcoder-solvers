
fun main(args:Array<String>) {
  val a = readLine()!!
  val mp = ('0'..'9').toList().map { it.toString().repeat(3) }.any { a.contains(it) }
  when { 
    mp == true -> "Yes"
    else -> "No"
  }.let(::println)
}
