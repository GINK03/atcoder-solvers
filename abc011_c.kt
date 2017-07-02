
data class A(val i: Int, var f: Boolean)
fun main( args : Array<String> ) {
   val s = readLine()!!.toInt()
   (1..3).map { 
    readLine()!!.toInt()
   }.sorted()
   .let {
     val xs = it
     (0..s).map { i ->
       when ( xs.contains(i) ) {
         true -> A(i, true)
         else -> A(i, false)
       }
     }.reversed()
     .let {
       val ds = it.filter { a ->
         a.f == true 
       }
       
       when {
         ds.size == 3 && ds[0]!!.i + 2 == ds[1]!!.i + 1 && ds[1]!!.i + 1 == ds[2]!!.i + 0 -> "NO"
         300 <= s -> "NO"
         299 <= s && (ds[0]!!.i + 2 == ds[1]!!.i + 1 || ds[1]!!.i + 1 == ds[0]!!.i + 0 ) -> "NO"
         else -> "YES"
       }.let { println(it) }
     }
   }
}
