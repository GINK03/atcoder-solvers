
fun main(args:Array<String>) {
  val n = readLine()!!.toDouble() 
  
  var res = n;
  for( i in (0..n.toInt()-1) ) {
    var cc = 0
    var t = i
    while(t>0) { cc+=t%6; t/=6 }
    t=(n-i).toInt()
    while(t>0) { cc+=t%9; t/=9 }
    if(res>cc) res=cc.toDouble()
  }
  println( res.toInt() )
}
