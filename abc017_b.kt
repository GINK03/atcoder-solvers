
fun main( args : Array<String> ) { 
  readLine()!!.let { 
    val a = it.replace("o", "X")
              .replace("k", "X")
              .replace("u", "X")
              .replace("ch", "X")
              .replace("X", "")
    if ( a == "" )
      println("YES")
    else 
      println("NO")

  }
}
