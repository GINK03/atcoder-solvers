
fun main(args:Array<String>) {
  val n = readLine()!!.toInt()

  val a = readLine()!!.toInt()

  val amari = n%500
  if( amari <= a ) 
    println("Yes")
  else
    println("No")
}
