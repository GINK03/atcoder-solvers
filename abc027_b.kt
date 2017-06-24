
data class A(var x:Int, var chaineLeft:Boolean, var chaineRight:Boolean)
fun main( args : Array<String> ) { 
  val n  = readLine()!!.toInt()
  val bs = readLine()!!.split(" ").map { x ->
    A(x.toInt(), false, false)
  }
  val mean =  bs.map { x -> x.x }.reduce { x,y -> x+y } / n
  when {
    bs.map { x -> x.x }.reduce { x,y -> x+y } % n != 0 -> println(-1)
    bs.all { x -> x.x == mean } -> println(0)
    else ->  {
      for(i in (0..bs.size -1)) { 
        if( bs[i].x == mean ) 
          continue
        if( bs[i].chaineLeft == true || bs[i].chaineRight == true ) 
          continue
        //println( bs[i] )
        for( j in (i+1..bs.size -1) ) {
          val slice  = bs.slice(i..j)
          val weight = slice.map { x -> x.x }.reduce { x,y -> x+y } / slice.size
          if( weight == mean ) {
            slice.map { x -> 
              x.chaineLeft = true
              x.chaineRight = true
            }
            slice[0].chaineLeft = false
            slice[slice.size-1].chaineRight = false
            break
          }
        }
      }
      //println( bs )
      val c = bs.map { x -> 
        listOf(x.chaineLeft, x.chaineRight)
      }.flatMap { x -> 
        x 
      }.count { x -> 
        x == true 
      }
      println( c/2 )
    }
  }


}
