
fun main(args:Array<String>) {
  val (a,b,c) = readLine()!!.split(" ")

  var h = a.toInt()
  var m = b.toInt()
  val delta = c.replace("UTC", "").toDouble() - 9

  h += delta.toInt() 
  h = h % 24
  
  m += Math.round((delta - delta.toInt().toDouble())*60).toInt()

  when( m > 0 ) { true -> null; else -> { m += 60; h-=1 } } 
  when( h > 0 ) { true -> null; else -> { h += 24 } }

  h += m/60 
  m = m%60

  h = h%24
  println("%02d:%02d".format(h, m))
}
