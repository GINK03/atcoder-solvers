
fun main(args : Array<String>) { 
  val r = readLine()!!.split(" ").map { x -> x.toInt() }.sortedBy { x -> x*-1 } 
  if(r == listOf(7,5,5) )
    println("YES")
  else 
    println("NO")
}
