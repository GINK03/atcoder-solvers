

fun main(args:Array<String>) { 
  val list = readLine()!!.split(" ").map(String::toInt)

  val min = list.min()!!


  // 最小値を引き、基底をつくる

  val list2 = list.map { it - min }
  
  var cost:Int

  // 残り２つが同じ大きさの時
  if( list2.filter { it != 0 }.size == 1 ) {
    cost = list2.max()!! // <- 最大値の数だけコストがかかる
    println(cost)
    return 
  }

  // 大、中、小で構成されている時
  val max2 = list2.max()!!
  val min2 = list2.min()!!
  val mid2 = list2.filter { it != max2 && it != min2 }.first()

  // max2 - mid2が1を繰り返す回数
  val onetimes = max2 - mid2 

  // 1を繰り返した結果、残りが偶数であれば、2で割った数
  val nokori = max2 - ( min2 + onetimes )

  if( nokori%2 == 0 )  {
    cost = nokori/2 + onetimes
  } else {
    cost = nokori/2+1+1+onetimes
  }
  println(cost)
}
