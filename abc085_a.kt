
fun main(args:Array<String>) {
  val ns = readLine()!!.split("/")
  
  listOf("2018", ns[1], ns[2]).joinToString("/").let(::println)
}
