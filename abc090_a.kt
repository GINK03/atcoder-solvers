
fun main(args:Array<String>) {
  (0..2).map { 
    readLine()!!.toList()[it]
  }.joinToString("").let(::println)
}
