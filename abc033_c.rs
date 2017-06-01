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

  let a    = &it.next().unwrap().unwrap();
  let vs   = a.split('+').collect::<Vec<_>>();
  let mut rs:Vec<bool> = Vec::new();
  for v in &vs { 
    let v = &v;
    //println!("{}", v);
    if v.contains("*") {
      let vv = v.split('*').collect::<Vec<_>>();
      if vv.contains(&"0") {
        rs.push(true)
      } else {
        rs.push(false)
      }
    } else {
      if v.to_string() == "0".to_string() {
        rs.push(true)
      } else {
        rs.push(false)
      }
    }
  }
  rs.retain(|&x| x == false);
  println!("{}", rs.len());
}

