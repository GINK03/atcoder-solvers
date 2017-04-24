fun main(args: Array<String>) {
  val (a,b,c) = readLine()!!.split(" ").map {x -> x.toInt()}
  if(b - a == c - b) {
    println("YES")
  } else {
    println("NO")
  }
}
