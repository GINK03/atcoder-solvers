
fun main(args:Array<String>) {
  var (n, m) = readLine()!!.split(" ").map(String::toInt)

  // n is S
  var snum = when { 
              m >= 2*n -> { 
                val ret = n
                m -= 2*n
                n = 0
                ret
              }
              else -> { 
                n = n - m/2
                val ret = m/2
                m = 0
                ret 
              }
            }
  //println("$snum $n $m")
  val sofm = m / 4 
  
  snum += sofm
  println(snum)
}
