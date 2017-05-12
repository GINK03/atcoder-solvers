
fun main(args : Array<String> )  {
  val (h, w) = readLine()!!.split(" ").map { x -> x.toInt() }
  val strs = (1..h).map { 
    val s = readLine()!!
    s
  }
  strs.zip(strs).map{ x -> 
    x.toList() 
  }.flatten()
  .map{ x ->
    println(x)
  }
}
