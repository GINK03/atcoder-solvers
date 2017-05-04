
fun main(args : Array<String>) { 
  val s = readLine()!!
  val a = s.toList().dropWhile { x -> 
    x != 'A' 
  }.reversed().dropWhile { x ->
    x != 'Z'
  }.reversed().joinToString("")
  println(a.length)
}
