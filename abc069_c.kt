
fun main(args:Array<String>) {
  val n = readLine()!!
  var xs = readLine()!!.split(" ").map(String::toInt)

  val quads = xs.filter { it%4 == 0 }.size
  xs = xs.filter { it%4 != 0 } 

  val twices = xs.filter { it%2 == 0 }.size
  xs = xs.filter { it%2 != 0 } 

  val noks = xs.size

  when { 
    (noks - quads) <= 1 && twices == 0  -> "Yes"
    noks <= quads && twices > 0  -> "Yes"
    else -> "No"
  }.run(::println)

  //println( noks -  quads )
}
