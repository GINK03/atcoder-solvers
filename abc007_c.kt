
data class B(val type:String, val y:Int, val x:Int, var score:Int)
fun main( args : Array<String> ) {
  val (R,C)    = readLine()!!.split(" ").map { it.toInt() }
  val (sy, sx) = readLine()!!.split(" ").map { it.toInt()-1 }
  val (ey, ex) = readLine()!!.split(" ").map { it.toInt()-1 }
  val ds       = (0..R-1).map { y ->
    readLine()!!
      .toList()
      .mapIndexed { x, c ->
        B(c.toString(), y, x, -1)
    }
  }
  // array type (y,x)
  ds[sy][sx].score = 0
  while(true) { 
    //get maxs 
    val maxScore = ds.flatMap { it }.sortedBy { it.score }.last().score
    val maxx     = ds.flatMap { it }.filter { it.score == maxScore }
    // search 4
    maxx.map { max ->
      val y = max.y
      val x = max.x
      val nowScore = max.score
      for(rule in listOf( listOf(-1, 0), listOf(+1, 0), listOf(0, -1), listOf(0,+1) ) ){
        val dy = y + rule[0]
        val dx = x + rule[1]
        if( dy < 0 || dy > ds.size-1 ) continue
        if( dx < 0 || dx > ds[0].size-1 ) continue  
        if( ds[dy][dx].type == "#") continue
        if( ds[dy][dx].score >= 0 && ds[dy][dx].score < nowScore + 1 ) continue
        ds[dy][dx].score = nowScore + 1
      }
    }
    if( ds.flatMap { it }.filter { it.type == "." }.filter { it.score == -1 }.size == 0 ) { 
      /* ds.map { dx ->
        println( dx.map { it.score }  )
      }
      println(ey)
      println(ex) */
      println(ds[ey][ex].score)
      break
    }
  }
}
