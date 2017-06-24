
fun main( args : Array<String> ) { 
  val bs = readLine()!!.split(" ").map { x -> x.toInt() }.reversed()
  val ans = mutableSetOf<Int>()
  for( i in (0..bs.size-1) ) {
    for( j in (i+1..bs.size-1) ) {
      for( k in (j+1..bs.size-1) ) {
        ans.add( bs[i] + bs[j] + bs[k] )
      }
    }
  }
  val sort =  ans
            .toList()
            .sortedBy { x ->
              x
            }
  println( sort[sort.size - 3] ) 
}
