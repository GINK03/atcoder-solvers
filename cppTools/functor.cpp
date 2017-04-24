#include<algorithm>
#include<vector>
#include<functional>
#include<iostream>
int ordrcnt = 0;
std::vector<std::function<void()>> v;
template<class FUNC>
int sub(FUNC f){
  auto func = std::bind(f);
  v.push_back(func);
  return 0;
};
sub([&](){std::cout << "多分これはいける" << std::endl; return 3;});
std::for_each(std::begin(v), std::end(v), [](std::function<void()> f){f();});
