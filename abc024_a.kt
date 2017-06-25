
fun main( args : Array<String> ) { 
  val (a,b,c,d) = readLine()!!.split(" ").map { x -> x.toInt() }
  val (e,f)     = readLine()!!.split(" ").map { x -> x.toInt() }

  val normal    = a*e + b*f
  val deg       = when { 
    e+f - d >= 0 -> (e+f)*c
    else         -> 0
  
  }
  println( normal - deg )
}
