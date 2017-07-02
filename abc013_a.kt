
fun main( args : Array<String> ) { 
  readLine()?.let {
    "ABCDE"
      .toList()
      .mapIndexed { i,x -> 
        Pair(x.toString(), i+1) 
      }
      .toMap()
      .get(it)
      .let { 
        println(it) 
      }
  }

}
