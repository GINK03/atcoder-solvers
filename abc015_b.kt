import java.lang.Math
fun main( args : Array<String> ) {
  readLine()
  readLine()?.let {
    it
      .split(" ")
      .map  { it.toInt() }
      .filter { it != 0 }
      .let {
        println(Math.ceil(it.sum()/it.size.toDouble()).toInt())
      }
  }
}
