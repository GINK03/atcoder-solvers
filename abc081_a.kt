
fun main(args:Array<String>) {
  readLine()!!.toList().mapNotNull {
    if( it == '1') it
    else null
  }.size.let(::println)
}
