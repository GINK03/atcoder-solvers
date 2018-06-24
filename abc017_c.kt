
fun main(args:Array<String>) {
  val (n, m) = readLine()!!.split(" ").map(String::toInt)

  val ms = mutableSetOf<Int>()
  val xs = (1..n).map { 
    val (l,r,s) = readLine()!!.split(" ").map(String::toInt)
    Triple(l,r,s)
  }.sortedBy { it.third*-1 }

  var sc = 0
  for( it in xs ) { 
    val (l,r,s) = it
    val mscopy = ms.toMutableSet()
    (l..r).map { mscopy.add(it) }
    if( mscopy.size == m )  continue
    sc += s
    (l..r).map { ms.add(it) }
  }
  println(sc)
}
