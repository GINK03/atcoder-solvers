
fun main(args : Array<String> ) { 
  val (a, b, c)  = readLine()!!.split(" ").map { x -> x.toLong() }
  if( a + b == c ||  a == b + c || b == a + c) {
    println("Yes")
  } else 
    println("No")
}
