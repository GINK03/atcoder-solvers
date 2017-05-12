
fun main(args : Array<String> ) { 
  val (s,e,st) = readLine()!!.split(" ").map { x -> x.toLong() }
  if ( s%st == 0L) 
    println( e/st - s/st + 1 )
  else
    println( e/st - s/st  )
    
}
