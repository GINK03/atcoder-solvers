
fun main(args:Array<String>) { 
  val (n,k) = readLine()!!.split(" ").map(String::toInt)

  val xs = readLine()!!.split(" ").map(String::toInt).sorted().slice(n-k..n-1)

  var eff = 0.0
  xs.map { eff = (eff+it).toDouble()/2 }
  println(eff)
}
