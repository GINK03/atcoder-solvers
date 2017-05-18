
fun main(args : Array<String>) { 
  val a = readLine()!!.split(" ").map { x -> x.toInt() }
  val b = readLine()!!.split(" ").map { x -> x.toInt() }
  val r = a.any { x -> b.contains(x) }
  when(r) {
    true -> println("YES")
    else -> println("NO")
  }
}
