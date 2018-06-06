
data class Data(val c:Int, val s:Int, val f:Int)
fun main(args:Array<String>) {
  val n = readLine()!!.toInt()
  
  val datasBase = (1..n-1).map { 
    val sp = readLine()!!.split(" ").map(String::toInt)
    val data = Data(sp[0], sp[1], sp[2])
    data
  }

  for( slicer in (0..datasBase.size-1) ) {
    val datas = datasBase.slice(slicer..datasBase.size-1)
    var time = 0
    for( loop in (0..100000) ) {
      if( datas.size-1 < loop ) break
      if( loop == 0 ) {
        time = datas[0].s
        time += datas[0].c
      } else { 
        if( time < datas[loop].s ) {
          // 未発射
          time += (datas[loop].s - time)
          time += datas[loop].c
        } else {
          // 発射済み
          if(  (time - datas[loop].s)%datas[loop].f  != 0 ){ 
            val wait = datas[loop].f - (time - datas[loop].s)%datas[loop].f 
            time += wait 
          }
          time += datas[loop].c
        }
      }
    }
    println(time)
  }
  println(0)
}
