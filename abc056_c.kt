

fun main(args:Array<String>) { 
  val m = readLine()!!.toInt()
  var a = 0
  var c = 0
  for(x in (1..m) ) { 
    c += x
    if(m <= c) {
      a = x
      break
    }
    //println("$x $c")
  }
  println(a)
}
