import java.lang.Math
fun main(args : Array<String>){
  val (x,a,b) = readLine()!!.split(" ").map { it.toInt() }
  when {
    Math.abs(x-a) < Math.abs(x-b) -> "A"
    else -> "B"
  }.let {
    println(it)
  }
}
