#include<string>
#include<iostream>
#include<stdint.h>
#include<memory>
#include<map>
#include<functional>
#include<vector>
#include<tuple>
namespace BuildsUtil{
  static std::string begin(const std::string& in){
    return "<" + in + ">";
  };
  static std::string end(const std::string& in){
    return "</" + in + ">\n";
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
  };
  ~BuildHTML(){};
  template<class FUNC>
  BuildHTML operator <<(FUNC func){
    std::vector<std::string> v = func();
    _data.insert(_cur, BuildsUtil::wrapp(v[1], v[0]).c_str());
    _cur  += BuildsUtil::wrapp(v[1], v[0]).length();
    return *this;
  };
  BuildHTML operator <<(HEAD head){
    _data += BuildsUtil::wrapp(head.in, "head");
    _cur  += _data.length();
    return *this;
  };
  BuildHTML operator <<(BR br){
    _data.insert(_cur, BuildsUtil::end("br").c_str());
    _cur  += BuildsUtil::end("br").length();
    return *this;
  };
  BuildHTML operator <<(BODY body){
    _data += BuildsUtil::begin("body");
    _cur  += BuildsUtil::begin("body").length();
    _data += BuildsUtil::end("body");
    return *this;
  };
  BuildHTML operator <<(const char* in){
    _data.insert(_cur, BuildsUtil::wrapp(in, "a").c_str());
    _cur  += BuildsUtil::wrapp(in, "a").length();
    return *this;
  };
  void operator <<(END end){
    // output only
    std::cout << _data << std::endl; 
  };
};
int main(){
  auto COUT = *std::shared_ptr<BuildHTML>(new BuildHTML()); 
  COUT << BuildHTML::HEAD("kusonemi")
       << BuildHTML::BODY()
          << "hage"   << "mage"   << BuildHTML::BR()
          << "mogzya" << "touch"  << BuildHTML::BR()
          << [&](){std::vector<std::string> v = {"h1","眠くて無理だ"}; return v;}
       << BuildHTML::END();
  return 0;
};
