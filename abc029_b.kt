
fun main(args : Array<String>) { 
  val a = (1..12).map { 
    when { 
      readLine()!!.contains("r")  -> true
      else                        -> false
    }
  }.count { x -> x == true } 
  println( a )
}
