
fun main(args:Array<String>) {
  val n = readLine()!!.toInt()
  val aas = readLine()!!.split(" ").map { it.toInt() }.toMutableList()
  aas.add(0, 0)
  aas.add(n+1, 0)
  
  var sum = 0
  (0..n).map { 
    sum += Math.abs(aas[it+1] - aas[it])
  }
  (1..n).map {
    println( sum - Math.abs(aas[it-1] -  aas[it]) - Math.abs(aas[it] - aas[it+1]) + Math.abs(aas[it-1] - aas[it+1]) ) 
  }
}
