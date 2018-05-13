
fun main(args:Array<String>) {
  val (a,b,c,d) = readLine()!!.split(" ").map(String::toInt)
  
  when {
    Math.abs( a - c ) <= d || ( Math.abs( a - b ) <= d && Math.abs( b - c ) <= d ) -> "Yes"
    else -> "No"
  }.let(::println)
}
