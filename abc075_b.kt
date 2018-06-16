
fun main(args:Array<String>) {
  val (h, w) = readLine()!!.split(" ").map(String::toInt)
  // y, x style composer
  val bs = (1..h).map { 
    readLine()!!.toList().map(Char::toString).toMutableList()
  }
  for( y in (0..h-1) ) {
    for( x in (0..w-1) ) {
      // 周辺をスキャン
      if( bs[y][x] != "#" ) {
        var count = 0
        if( y -1 >= 0 && x-1 >= 0 &&  bs[y-1][x-1] == "#" ) count += 1
        if( y -1 >= 0 && bs[y-1][x+0] == "#" ) count += 1
        if( y -1 >= 0 && x+1 <= w-1 && bs[y-1][x+1] == "#" ) count += 1

        if( x-1 >= 0 && bs[y+0][x-1] == "#" ) count += 1
        if( x+1 <= w-1 && bs[y+0][x+1] == "#" ) count += 1

        if( y+1 <= h-1 && x-1 >= 0 && bs[y+1][x-1] == "#" ) count += 1
        if( y+1 <= h-1 && bs[y+1][x+0] == "#" ) count += 1
        if( y+1 <= h-1 && x+1 <= w-1 && bs[y+1][x+1] == "#" ) count += 1
        
        bs[y][x] = count.toString()
      }
    }
  }
  bs.map { b ->
    b.joinToString("").run(::println)
  }
}
