
fun main(args:Array<String>) {
  val m = mutableMapOf<Int,Int>() 
  readLine()!!.split(" ").map(String::toInt).map { 
    if( m[it] == null ) m[it] = 0
    m[it] = m[it]!! + 1
  }
  m.toList().mapNotNull { 
    if( it.second == 1 ) it.first
    else null
  }.first().run(::println)
}
