import java.lang.Math


fun main(args:Array<String>) {
  val (n,m) = readLine()!!.split(" ").map { it.toDouble() }
  var buff = n
  var count = 0L
  while(true) {
    buff = 2*buff 
    count += 1
    if(buff > m)  break
    if( buff == m) { 
      count+=1 
      break
    }
  }
  println(count)
}
