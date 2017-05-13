
fun main(args : Array<String> ) {
  val m:MutableMap<Char, MutableList<Char> > = mutableMapOf()
  m['a'] = readLine()!!.toMutableList()
  m['b'] = readLine()!!.toMutableList()
  m['c'] = readLine()!!.toMutableList()
  
  var t = 'a'
  while(true) { 
    val l = m[t]
    //println(l)
    if( l!!.size == 0) {
      println(t.toString().toUpperCase())
      break
    }
    t = l[0]
    l.removeAt(0)
  }
}
