
fun main(args:Array<String>) {
  val a = readLine()!!.replace(" ", "").toInt()
  
  val sqrt = Math.pow(a.toDouble(), 0.5)
  if( sqrt == sqrt.toInt().toDouble() )
    println("Yes")
  else
    println("No")
}
