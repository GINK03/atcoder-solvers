#include<string>
#include<iostream>
#include<stdint.h>
#include<memory>
#include<map>
#include<functional>
#include<vector>
#include<tuple>
//#include<boost/mpl/string.hpp>
namespace BuildsUtil{
  //boost::mpl::string<'age'> age;
  std::string __str = "";
  template<class...> 
  static std::string begin();
  template<char x, char... xs> 
  std::string begin(){
    __str += x;
    return begin<xs...>();
  };
  template<>
  std::string begin<>(){
    std::string res = __str;
    __str == "";
    return res;
  };
  static std::string begin(const std::string& in){
    return std::string("<").append(in).append(">");
  };
  static std::string end(const std::string& in){
    return "</" + in + ">\n";
  };
  static std::string wrapp(const std::string& in, const std::string& ac){
    return begin(ac) + in + end(ac);
  };
};

class BuildHTML{
  private:
  constexpr static auto head = "head";
  std::string _data;
  int64_t     _cur;
  //do not allow create free instance
  BuildHTML()
  :_data("")
  {};
  ~BuildHTML(){};
  public:
  struct BR{};
  struct BODY{};
  struct END{};
  struct HEADIN{
    std::string in;
    HEADIN(const std::string& in)
    :in(in){};
  };
  struct HEAD{
    HEADIN hin; std::string in;
    HEAD(const HEADIN& hin, const std::string& in)
    :hin(hin), in(in){};
  };
  struct DOCTYPE{
    std::string in;
    DOCTYPE(const std::string& in):in(in){};
    DOCTYPE():in("<!DOCTYPE html>\n"){};
  };
  struct LANG{
    std::string in;
    LANG(const std::string& in):in("<html lang=\""+in+"\">\n"){};
    LANG():in("<html lang=\"ja\">\n"){};
  };
  static BuildHTML& COUT(){
    static auto cout = BuildHTML(); 
    return cout;
  };
  template<class FUNC>
  BuildHTML& operator <<(FUNC func){
    std::vector<std::string> v = func();
    _data.insert(_cur, BuildsUtil::wrapp(v[1], v[0]).c_str());
    _cur  += BuildsUtil::wrapp(v[1], v[0]).length();
    return *this;
  };
  BuildHTML& operator <<(const DOCTYPE& doctype){
    _data.insert(_cur, doctype.in);
    _cur   += doctype.in.length();
    return *this;
  };
  BuildHTML& operator <<(const LANG& lang){
    _data.insert(_cur, lang.in);
    _cur   += lang.in.length();
    return *this;
  };
  BuildHTML& operator <<(const HEAD& head){
    _data += BuildsUtil::wrapp(
        BuildsUtil::wrapp(head.hin.in, "title"),
        "head");
    _cur  += BuildsUtil::wrapp(
        BuildsUtil::wrapp(head.hin.in, "title"),
        "head").length();
    return *this;
  };
  BuildHTML& operator <<(const BR& br){
    _data.insert(_cur, BuildsUtil::end("br"));
    _cur  += BuildsUtil::end("br").length();
    return *this;
  };
  BuildHTML& operator <<(const BODY& body){
    _data += BuildsUtil::begin<'<','b','o','d','y','>'>();
    _cur  += BuildsUtil::begin("body").length();
    _data += BuildsUtil::end("body");
    return *this;
  };
  BuildHTML& operator <<(const char* in){
    _data.insert(_cur, BuildsUtil::wrapp(in, "p"));
    _cur  += BuildsUtil::wrapp(in, "p").length();
    return *this;
  };
  struct P{
    std::string in;
    P(const std::string& in):in(in){};
  };
  BuildHTML& operator <<(const P& p){
    _data.insert(_cur, BuildsUtil::wrapp(p.in, "p"));
    _cur  += BuildsUtil::wrapp(p.in, "p").length();
    return *this;
  };
  void operator <<(const END& end){
    // output only
    std::cout << _data << std::endl; 
  };
};
int main(){
  //auto COUT = *std::shared_ptr<BuildHTML>(new BuildHTML()); 
  BuildHTML::COUT()
       << BuildHTML::DOCTYPE()
       << BuildHTML::LANG("ja")
       << BuildHTML::HEAD(BuildHTML::HEADIN("眠たいページ"), "kusonemi")
       << BuildHTML::BODY()
          << BuildHTML::P("mogeo")
          << "hage"   << "mage"   << BuildHTML::BR()
          << "mogzya" << "touch"  << BuildHTML::BR()
          << [&](){std::vector<std::string> v = {"h1","眠くて無理だ"}; return v;}
       << BuildHTML::END();
  return 0;
};
