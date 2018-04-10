
fun main(args:Array<String>) {
  val n = readLine()!!.toInt()
  val ms = (1..n).map { 
    val (t,x,y) = readLine()!!.split(" ").map(String::toInt)
    Triple(t,x,y)
  }
  var (st,sx,sy) = Triple(0,0,0)
 
  var isPass = true
  ms.map { triple ->
    val (t,x,y) = triple
    val deltaT = t - st
    val measure = Math.abs(x - sx) + Math.abs(y - sy)
    if( deltaT < measure )
      isPass = false
    if( deltaT%2 == 1 && x == sx && y == sy ) 
      isPass = false
    st = t
    sx = x
    sy = y
  }
  if( isPass ) {
    println("Yes")
  } else {
    println("No")
  }

}
