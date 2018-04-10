
fun main(args:Array<String>) {
  ( readLine()!!.split(" ").map(String::toInt).reduce { y,x -> y*x } % 2 ).let { 
    when {
      it == 0 -> "Even"
      else -> "Odd"
    }.let(::println)
  }
}
