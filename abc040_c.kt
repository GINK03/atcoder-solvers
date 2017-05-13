
fun main(args : Array<String> ) {
  readLine()
  val r = readLine()!!.split(" ").map { x ->
    x.toInt()
  }.reversed().toMutableList()
  var buff = 0
  for(i in (0..100) ) {
    if( r.size > 2 ) {
      val (c1, c2) = Pair( Math.abs(r[1] - r[0]), Math.abs(r[2] - r[0]) )
      if( c1 < c2 ) {
        println(c1)
        r.removeAt(0)
        buff += c1
      } else {
        println(c2)
        r.removeAt(0)
        r.removeAt(0)
        buff += c2
      }
      if( r.size == 0)
        break
    } else {
      val c1 = Math.abs(r[1] - r[0])
      println(c1)
      buff += c1
      break
    }
  }
  println(buff)

}
