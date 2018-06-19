
fun main(args:Array<String>) {
  val n = readLine()!!
  val xs = readLine()!!.split(" ").map(String::toInt)

  val max = xs.max()!!

  val m = mutableMapOf<Int,Int>()
  
  xs.map { x -> 
    if( m[x] == null ) m[x] = 0
    m[x] = m[x]!! + 1
  }
  //println( m )

  (max downTo 0 step 2).map { 
    //println( m ) 
    //println( it )
    //println( m[it] )
    when { 
      it >= 1 && m[it] == 2 -> true 
      it < 1  && m[it] == 1 -> true
      else -> false
    }
  }.all { it }.let { result ->
    if( result == false ) { 0 }
    else {
      (1..(max+1)/2).map {2}.reduce { y,x -> y*x }
    }
  }.run(::println)
  
}
