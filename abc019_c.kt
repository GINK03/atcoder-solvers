
fun main(a:Array<String>){
  val n  = readLine()!!.toInt()
  val ms = readLine()!!.split(" ").map { it.toInt() }.sorted()
  
  var bs = ms.toMutableList()
 
  var cnt = 0
  for(i in (0..ms.size-1)) {
    if( bs == mutableListOf<Int>() ) break
    val t = bs[0]
    bs = bs.filter { x ->
      !( x/t % 2 == 0 && 
          (x/t).toDouble() == x/t.toDouble() || t == x )
    }.toMutableList()
    cnt += 1
  }
  println(cnt)
}
