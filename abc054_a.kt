
fun main(args : Array<String> ) { 
  val (a, b) = readLine()!!.split(" ").map { x ->
    val t = x.toInt()
    if( t == 1 ) { 
      t + 13
    } else { 
      t 
    }
  }
  if ( a > b ) { 
    println("Alice")
  } else if ( a == b ) {
    println("Draw")
  } else if ( a < b ) {
    println("Bob")
  }
}
