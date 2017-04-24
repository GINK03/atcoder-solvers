fun main(args: Array<String>) { 
  val a = readLine()!!.toList()
  val b = readLine()!!.toMutableList()
  b.add("__DUMMY__")
  val c = a.zip(b).map { x -> x.toList() }.flatMap { x -> x }.joinToString("")
  println(c)
}
