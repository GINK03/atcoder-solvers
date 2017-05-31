
use std::io::{self, Read};
use std::io::prelude::*;
use std::collections::BTreeSet;
use std::collections::HashSet;
use std::collections::HashMap;

fn main(){
  let stdin  = std::io::stdin();
  let mut it = stdin.lock().lines();
  let mut s:HashSet<char> = HashSet::new();
  let mut m:HashMap<String,f64> = HashMap::new();

  let a      = &it.next().unwrap().unwrap();
  let a      = a.parse::<i32>();
  for i in 0..a.unwrap() {
    //println!("{}", i);
    let a  = &it.next().unwrap().unwrap();
    let bs = a.split(' ').collect::<Vec<_>>();
    let cn = String::from(bs[0]);
    let pn = bs[1].parse::<f64>().unwrap();
    m.insert(cn, pn);
  }
  let mut acc:f64 = 0.0;
  for (cn, pn) in &m {
    //println!("{}", cn);
    acc += pn.clone();
  }
  let mut r:Option<String> = None;
  for (cn, pn) in &m {
    if pn/acc > 0.5 {
      r = Some(cn.clone());
    }
  }
  match r {
    Some(x) => println!("{}", x),
    None    => println!("atcoder"),
  }
}


