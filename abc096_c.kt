
fun main(args:Array<String>) {
  val (h, w) = readLine()!!.split(" ").map(String::toInt)
  val X = (1..h).map {
    readLine()!!.toList().map { it.toString() }
  }
  val sc = (0..h-1).map { y ->
    (0..w-1).map { x ->
      val st = X[y][x]
      if( st == "#" ) {
        val sst = mutableListOf<String>()
        // up
        if( y != 0 ) sst.add( X[y-1][x] ) 
        // down
        if( y != h-1) sst.add( X[y+1][x] )
        // left
        if( x != 0) sst.add( X[y][x-1] )
        // right
        if( x != w-1) sst.add( X[y][x+1] )
        sst.filter { it == "#" }.size >= 1
      } else {
        null
      }
    }
  }.flatten().mapNotNull { it }.all { it == true }
  when(sc) {
    true -> "Yes"
    else -> "No"
  }.let(::println)
} 
