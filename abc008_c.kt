
// this model would be TLE...
// another way is to use mathematical way
val side:MutableList<MutableList<Int>> = mutableListOf(  )
fun perm(depth: Int, input: List<Int>, buff: MutableList<Int> ) {
  if( depth == 0) 
    side.add( buff ) 
  for(i in (0..input.size-1)) {
    when { 
      buff.contains(i) == false -> { 
        val nextBuff = buff.toMutableList()
        nextBuff.add(i)
        perm(depth-1, input, nextBuff)
      }
      else -> null
    }
  }
}

data class ST(val param: Int, var st: Boolean)
fun main( args : Array<String> ) {
  val n = readLine()!!.toInt()
  val inputs = (1..n).map { 
    readLine()!!.toInt()
  }
  perm(inputs.size, inputs, mutableListOf<Int>() )
  //println(side)
  side.map { sd ->
    val qu = sd.map { i -> ST(inputs[i], true) }
      .toMutableList()
      .let { x ->
        (0..x.size-2).map { i ->
          (i+1..x.size-1).map { k ->
            when { 
              x[k].param%x[i].param == 0 && x[k].st == true  -> x[k].st = false
              x[k].param%x[i].param == 0 && x[k].st == false -> x[k].st = true
              else -> null
            }
          }
        }
        //println(x)
        x
      } 
    qu
  }.let { 
    ( it.flatMap { it }.count { it.st == true }.toDouble() / it.size ).let { println(it) } 
  }
}
