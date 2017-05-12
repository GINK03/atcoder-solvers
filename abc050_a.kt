
fun main(args: Array<String>) {
  val raw = readLine()!!
  val r = Regex(""" (\+|\-) """).split(raw).map { x ->
    x.toInt()
  }
  if( raw.contains("+") )
    println( r.reduce { x, y -> x + y } )
  else 
    println( r.reduce { x, y -> x - y } )
}
