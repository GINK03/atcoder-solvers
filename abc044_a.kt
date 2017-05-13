
fun main(args : Array<String>) {
  val(n, k, x, y) = (1..4).map { readLine()!!.toInt() } 
  
  if( n > k )
    println( k*x + y*(n - k) )
  else
    println( n*x )
}
