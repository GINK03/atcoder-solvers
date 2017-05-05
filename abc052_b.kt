
fun main(args : Array<String>) { 
  var c = 0
  val state:MutableList<Int> = mutableListOf(0)
  readLine()
  readLine()!!.toList().map { x ->
    when(x) { 
      'D' -> c--
      'I' -> c++
    }
    state.add(c)
  }
  println(state.max())
}
