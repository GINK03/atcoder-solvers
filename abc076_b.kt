
fun main(args:Array<String>) {
  val (n, k) = (1..2).map { readLine()!!.toInt() }
  val add = fun(i:Int):Int { return i * 2 } 
  val bys = fun(i:Int):Int { return i + k } 

  val funs = (0..n-1).map { slice ->
    (0..n-1).map { 
      when { 
       it <= slice -> add
       else -> bys
      }
    } 
  }
  funs.map { funlist -> 
    var s1 = 1
    funlist.map { s1 = it(s1) }
    var s2 = 1
    funlist.reversed().map { s2 = it(s2) }
    listOf(s1, s2)
  }.flatten().min().run(::println)
}
