
fun main ( args : Array<String> ) {
  val (n, k) = readLine()!!.split(" ").map { x ->
    x.toLong()
  }
  val r = (1..n).mapIndexed {  i,x ->
    if(i == 0) 
      k 
    else
      k-1
  }.reduce { y,x ->
    y*x
  }
  println(r)
}
