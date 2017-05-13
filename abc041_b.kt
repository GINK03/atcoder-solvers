
fun main(args : Array<String>) { 
  val ps = readLine()!!.split(" ").map { x -> x.toLong()%1000000007L }
  println( (ps[0]*ps[1]%1000000007L)*ps[2]%1000000007L )
}
