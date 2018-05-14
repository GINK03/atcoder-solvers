
fun main(args:Array<String>) {
  val (a,b) = readLine()!!.split(" ").map(String::toInt)
  val aa = readLine()!!
  val h = """\d""".repeat(a)
  val t = """\d""".repeat(b)
  when((h+"-"+t).toRegex().matchEntire(aa)){
     null -> "No"
     else -> "Yes"
  }.let(::println)

}
