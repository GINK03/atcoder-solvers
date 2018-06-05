
fun main(args:Array<String>) {
  val (x,y,z) = readLine()!!.split(" ").map(String::toInt)

  println( (x-z)/(y+z) )
}
