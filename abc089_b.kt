
fun main(args:Array<String>) {
  val base = setOf("P", "W", "G", "Y")
  readLine()
  val target = readLine()!!.split(" ").toSet()

  val size = base.intersect( target ).size
  when { 
    size == 4 -> "Four"
    size == 3 -> "Three"
    else -> null
  }.let { println(it) }
}
