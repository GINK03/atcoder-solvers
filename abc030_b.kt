import java.lang.Math
fun main(args: Array<String>) { 
  val (a1, a2) = readLine()!!.split(" ").map { x -> x.toInt() }
  val b2  = (a2*6)%360
  val b1  = (a1%12)*30.0 + (b2/12.0)
  val ans = Math.abs(b2 - b1)
  when { 
    ans > 180 -> println(360 - ans)
    else      -> println(ans)
  }
}
