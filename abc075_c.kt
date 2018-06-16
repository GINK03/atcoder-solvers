import java.math.BigDecimal as BD 
fun gcd(a: BD, b: BD): BD = if (b == 0.toBigDecimal() ) a else gcd(b, a % b)
fun lcm(a: BD, b: BD) = a * b / gcd(a, b)
fun main(args:Array<String>) {
  val n = readLine()!!.toInt()
  val ms = (1..n).map { readLine()!!.toBigDecimal() }
  var ini = ms[0]
  (1..ms.size-1).map { 
    ini = lcm(ini, ms[it])
    //println(ini)
  }
  println(ini)
}
