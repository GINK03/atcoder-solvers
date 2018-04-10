
fun main(args:Array<String>) {
  val (a, b) = readLine()!!.split(" ").map(String::toInt)

  (a..b).map { 
    val str = it.toString().toList()
    val size = str.size
    (0..size/2).map {
      str[it] == str[size-1-it] 
    }.all{ it == true }
  }.filter { it == true }.size.let(::println)
}
