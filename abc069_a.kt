
fun main(args:Array<String>) {
  readLine()!!.split(" ").map(String::toInt).map { it-1 }.fold(1) { y,x -> y*x }.run(::println)
}
