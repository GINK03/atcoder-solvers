
fun main(args:Array<String>) { 
  val input = readLine()!!
  if( input.toList().sorted().joinToString("") == "abc" ) 
    println("Yes")
  else
    println("No")
}
