
fun main(args:Array<String>){
  val (a,b,c,d) = readLine()!!.split(" ").map { it.toInt() }

  when { 
    a+b > c+d -> "Left"
    a+b == c+d -> "Balanced"
    a+b < c+d -> "Right"
    else -> null
  }.let { println(it) }
}
