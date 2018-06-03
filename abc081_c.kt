
fun main(args:Array<String>) {
  val (n, k) = readLine()!!.split(" ").map(String::toInt)

  val bs = mutableMapOf<Int,Int>()
  readLine()!!.split(" ").map(String::toInt).map {
    if( bs.get(it) == null ) bs[it] = 0
    
    bs[it] = bs[it]!! + 1
  }
  val cs = bs.toList().sortedBy { it.second }.slice( 0..(bs.size - k - 1) )
  println(cs.map { it.second }.sum() )
}
