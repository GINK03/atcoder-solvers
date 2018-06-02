
fun main(args:Array<String>) {
  val n = readLine()!!.toInt()

  val reds = (1..n).map { 
    val (a,b) = readLine()!!.split(" ").map(String::toInt)
    Pair(a,b)
  }
  val blues = (1..n).map { 
    val (a,b) = readLine()!!.split(" ").map(String::toInt)
    Pair(a,b)
  }

  val mm:MutableMap<Pair<Int, Int>, MutableList<Pair<Int,Int>>> = mutableMapOf() 

  blues.map { blue -> 
    val vals = reds.filter  { it ->
      val (ra,rb) = it
      val (ba,bb) = blue
      if ( ba > ra && bb > rb ) true
      else false
    }
    mm[ blue ] = vals.toMutableList()
  }
  //println(mm)

  val al = mutableSetOf<Pair<Int,Int>>()
  val jk = mm.toList().sortedBy { it -> 
   val (a, b) = it 
   -1*a.first*a.second
  }.mapNotNull {
    val (k,v) = it
    
    val chv = v.filter { pair ->
      if( ! al.contains(pair) ) true
      else false
    }.sortedBy { pair ->
      (k.first - pair.first) * (k.second - pair.second ) 
    }
    //println("$k ${chv}")
    if( chv.size >= 1 ) {
      al.add( chv.first() )
      chv.first()
    } else {
      null 
    }
  }
  println(jk.size)
}
