
fun main(args : Array<String> ){ 
  val cs:MutableList<Char> = mutableListOf()
  readLine()!!.toList().map { x -> 
    when(x) { 
      '0' -> cs.add(x)
      '1' -> cs.add(x)
      else -> { 
        if(cs.size != 0)
          cs.removeAt(cs.size - 1)
        else 
          null
      }
    }
  }
  println( cs.joinToString("") )
}
