
fun main(args : Array<String>) { 
  val a = readLine()!!.toList().toSet().size
  when (a) {
    1 -> println("SAME")
    else -> println("DIFFERENT")
  }
}
