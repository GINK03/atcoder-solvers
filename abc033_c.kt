
fun main(args : Array<String>) {
  val rs = readLine()!!.split("+").map { x -> 
    val st = when {
      x.contains("*") -> { 
          x.split("*").any { x -> x == "0"}
        }
      x == "0"        -> true
      else            -> false
    }
    st
  }
  println(rs.count { x -> x == false})
}
