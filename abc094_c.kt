
fun main(args:Array<String>) {
  val n = readLine()!!.toInt()

  val ns = readLine()!!.split(" ").map(String::toInt).sorted()
  //println(ns)
  val ln = ns.size

  (0..ln-1).map { l -> 
    val N = ln/2 - 1
    if( N > l ) {
      println(ns[n/2])
    } else {
      println(ns[n/2-1])
    }
  }
}
