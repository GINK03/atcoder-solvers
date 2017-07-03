
fun main( args : Array<String> ) {
   val tri = mutableListOf(0L,0L,1L)
   val n = readLine()!!.toInt()
   (3..n-1).map { i ->
     val next = ( tri[i-1] + tri[i-2] + tri[i-3] )
     tri.add( next%10007L )
   }
   println(tri[n-1])
}
