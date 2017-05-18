
// このコードはこれでは計算が間に合わない
fun miss1() {
  val m  = readLine()!!.toInt() - 1
  val ts = readLine()!!.split(" ").map { x -> x.toInt() }
  var c  = 0
  for( i in (0..m) ) {
    var st = ts[i]
    val ns = ts.slice(i+1..m)
    for(n in ns) {
      if(st < n) {
        //println("$st $n")
        st = n
        c += 1
      } else {
        break
      }
    }
  }
  println(c + ts.size )
}

// このコードは、計算は早いが本当にまれに、動かない
fun miss2() {
  readLine()
  val m = readLine()!!.split(" ").map { x -> x.toInt() }
  val a:MutableList<MutableList<Int>> = mutableListOf()
  var buff = -1
  var t: MutableList<Int> = mutableListOf()
  for( a1 in m ) {
    if( buff < a1) {
      t.add(a1)
      buff = a1
    } else {
      buff = a1
      a.add(t)
      t    = mutableListOf(a1)
    }
  }
  a.add(t)
  val r = a.map { xs ->
    val t2 = (1 .. xs.size ).toList().map { x ->
      x
    }.reduce { y,x -> y + x }
    t2
  }.reduce { y,x ->
    y + x
  }
  println(r)
}


fun main(args : Array<String>) {
}
