
fun main( args : Array<String> ) {
  val (n, depth) = readLine()!!.split(" ").map { it.toInt() }
  val inits      = readLine()!!.toList().map { it.toString() }
  val max        = Integer.parseInt("1".repeat(inits.size), 2)
  val ms         = mutableSetOf<String>()
  (0..max).map { x ->
    val mmm   = "%0${inits.size}d".format(Integer.toBinaryString( x ).toLong())
    val count = mmm.toList().count { '1' == it }
    if( count <= depth ) {
      mmm
        .toList()
        .zip( inits )
        .mapIndexed { i, fc ->
          val (f, c) = fc
          Triple(i, f, c)
        }.filter { triple ->
          triple.second == '1'
        }.sortedBy { triple ->
          triple.third
        }.let {
          val nextInits = inits.toMutableList()
          val targets   = it.map { it.first }.sorted()
          targets.zip(it).map { target_triple ->
            val (target, triple) = target_triple
            nextInits[target] = triple.third
          }
          ms.add( nextInits.joinToString("") )
        }
    }
  }
  println(ms.sorted().first())
}



