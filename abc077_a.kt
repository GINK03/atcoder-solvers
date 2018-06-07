
fun main(args:Array<String>) {
  val a1 = readLine()!!.toList().reversed()
  val a2 = readLine()!!.toList()
  a1.zip(a2).map { 
    val (c1, c2) = it
    c1 == c2 
  }.all { it }.let { 
    when (it)  {
      true -> "YES" 
      else -> "NO"
    }
  }.run(::println)
}
