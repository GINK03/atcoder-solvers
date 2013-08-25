#include<string>
#include<iostream>
#include<stdint.h>
#include<memory>
#include<map>
#include<functional>
#include<vector>
namespace BuildsUtil{
  static std::string begin(const std::string& in){
    return "<" + in + ">";
  };
  static std::string end(const std::string& in){
    return "</" + in + ">";
  };
  std::string wrapp(const std::string& in, const std::string& ac){
    return begin(ac) + in + end(ac);
  };
};

class BuildHTML{
  private:
  constexpr static auto head = "head";
  std::string _data;
  int64_t     _cur;
  public:
  struct BR{};
  struct BODY{};
  struct END{};
  struct HEAD{std::string in;HEAD(const std::string& in):in(in){};};
  BuildHTML()
  :_data("")
  {
    //if(COUT != nullptr)     BuildHTML::COUT = std::shared_ptr<BuildHTML>(new BuildHTML());
  };
  ~BuildHTML(){};
  template<class SFIX>
  BuildHTML operator <<(SFIX in){
    _data.insert(_cur, BuildsUtil::begin("br").c_str());
    _cur  = BuildsUtil::begin("br").length();
    return *this;
  };
  BuildHTML operator <<(HEAD head){
    _data += BuildsUtil::wrapp(head.in, "head");
    _cur  += _data.length();
    return *this;
  };
  BuildHTML operator <<(BODY body){
    _data += BuildsUtil::begin("body");
    _cur  += BuildsUtil::begin("body").length();
    _data += BuildsUtil::end("body");
    return *this;
  };
  BuildHTML operator <<(END end){
    std::cout << _data << std::endl; 
    return *this;
  };
  BuildHTML operator <<(const char* in){
    _data.insert(_cur, BuildsUtil::wrapp(in, "a").c_str());
    _cur  += BuildsUtil::wrapp(in, "a").length();
    return *this;
  };
};

int ordrcnt = 0;
std::vector<std::function<void()>> v;

template<class FUNC>
int sub(FUNC f){
  auto func = std::bind(f);
  v.push_back(func);
  return 0;
};
#include <algorithm>
int main(){
  auto COUT = *std::shared_ptr<BuildHTML>(new BuildHTML()); 
  COUT << BuildHTML::HEAD("kusonemi")
       << BuildHTML::BODY()
          << "hage"   << "mage"   << BuildHTML::BR()
          << "mogzya" << "touch"  << BuildHTML::BR()
       << BuildHTML::END();
  sub([&](){std::cout << "nemui" << std::endl; return 1;});
  sub([&](){std::cout << "眠くて無理だ" << std::endl; return 2;});
  sub([&](){std::cout << "多分これはいける" << std::endl; return 3;});
  std::for_each(std::begin(v), std::end(v), [](std::function<void()> f){f();});
};
