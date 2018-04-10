
fun main(args:Array<String>) {
  val n = readLine()
  val ms = readLine()!!.split(" ").map(String::toInt).sorted().reversed()

  var (A, B) = Pair(0, 0)
  ms.mapIndexed { index, it -> 
    if( index%2 == 0 )
      A+=it
    else
      B+=it
  }
  println(A-B)
}
