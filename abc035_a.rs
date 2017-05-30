use std::io;
use std::io::prelude::*;

fn main(){
  let stdin = io::stdin();
  for line in stdin.lock().lines() { 
    let a = &line.unwrap();
    let v: Vec<&str> = a.split(' ').collect();
    let bs = v.iter().map( |&x|  {
      //println!("{}", x);
      let x = x.parse::<f64>().unwrap();
      return x;
    }).collect::<Vec<_>>();
    let a = bs[0]/bs[1];
    if( a == 4.0/3.0 ) { 
      println!("4:3")
    } else if( a == 16.0/9.0 ) {
      println!("16:9")
    }
    break;
  }
}
