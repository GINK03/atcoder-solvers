
fun main(args:Array<String>) {
  val n = readLine()!!.toDouble() 
  

  var no = n 
  var c = 0
  while(true) {
    if( no < 6.0 ) break
    
    val a1 = ( Math.log(no) / Math.log(9.0) ).toInt()
      
    val a2 = ( Math.log(no)/ Math.log(6.0) ).toInt()
    
    val nextA1 = no - Math.pow(9.0, a1.toDouble())
    val nextA2 = no - Math.pow(6.0, a2.toDouble())
    
    if( nextA1 < nextA2 ) { 
      no = nextA1
    } else {
      no = nextA2 
    }
    c += 1
    //println("a1 $a1 a2 $a2 no $no")
  }
  //println(no)
  println((no+c).toInt())
}
