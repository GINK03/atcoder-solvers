
fun main(args:Array<String>) {
  val list = (1..3).map { 
    readLine()!!.split(" ").map(String::toInt)
  }
  if( list[0][0]+list[1][1] == list[0][1]+list[1][0] &&
    list[0][1]+list[1][2] == list[0][2]+list[1][1] && 
    list[1][0]+list[2][1] == list[2][0]+list[1][1] && 
    list[1][1]+list[2][2] == list[1][2]+list[2][1] )
    println("Yes")
  else
    println("No")
    
}
