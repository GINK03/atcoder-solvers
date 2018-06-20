
fun main(args:Array<String>) {
  val (n, k) = readLine()!!.split(" ").map(String::toInt)
 	if(k==0) println(n*n)
	else
	{
    var ans = 0L
		for(i in (k+1..n))
		{
			ans+=((n/i)*(i-k));
			if((n%i)>=k)ans+=((n%i)-k+1);
		}
		println(ans)
	}
}
