
fun main(args : Array<String> ) { 
  val n = readLine()!!.toInt() - 1

  val b = (0..n).map { 
    readLine()!!.toList()
  }.toList()

  val a:MutableList<MutableList<Char>> = (0..n).map { 
    val b:MutableList<Char> = (0..n).map { 'D'}.toMutableList()
    b
  }.toMutableList()

  (0 .. n).map { y ->
    (0 .. n).map { x ->
      a[x][Math.abs((y-n)%(n+1))] = b[y][x]
    }
  }
  a.map { x-> 
    println(x.joinToString(""))
  }
}
