
fun main(args : Array<String>) {
  val a = readLine()!!.toList()
  var b:MutableList<MutableList<Int>> = mutableListOf(mutableListOf(0, 0))
  a.map { x ->
    when(x) {
      'U' -> { 
        b.map { b2 ->
          b2[1] = b2[1] + 1 
        }
      }
      'D' -> { 
        b.map { b2 ->
          b2[1] = b2[1] - 1 
        }
      }
      'L' -> { 
        b.map { b2 ->
          b2[0] = b2[0] - 1
        }
      }
      'R' -> { 
        b.map { b2 ->
          b2[0] = b2[0] + 1
        }
      }
      '?' -> { 
        val t = b.map { b2 ->
          val b3 = mutableListOf(b2[0], b2[1])
          b3[0] = b3[0] - 1
          val b4 = mutableListOf(b2[0], b2[1])
          b4[0] = b4[0] + 1
          val b5 = mutableListOf(b2[0], b2[1])
          b5[1] = b5[1] + 1
          val b6 = mutableListOf(b2[0], b2[1])
          b6[1] = b6[1] - 1
          listOf(b3, b4, b5, b6)
        }
        b = mutableListOf()
        t.map { t2 -> 
          t2.map { t ->
            b.add(t)
          }
        }
      }
      else -> ""
    }
  }
  val mode = readLine()!!.toInt()
  //println(b)
  val comp = b.map { z ->
    z.map { y -> Math.abs(y)}.reduce { y,x -> y+x }
  }
  when(mode) { 
    1 -> println(comp.max())
    2 -> println(comp.min())
  }
}
