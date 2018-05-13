
fun main(args:Array<String>) {
  val ba = readLine()!!.split(" ").map(String::toInt).toMutableList()
  val m = readLine()!!.toInt()
  val max = ba.max()!!
  val index = ba.mapIndexed { i,x ->
    if ( max == x )
      i
    else
      null
  }.filter { it != null }[0]!!
  val fold = (1..m).fold(max) { y, x -> 
    y * 2
  }
  ba[ index ] = fold
  ba.sum().let(::println)
}
