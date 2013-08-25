PWD=`pwd`/
echo "default user path"
echo $PWD
g++-4.8 -std=c++11 -fPIC -fpermissive \
  build_html.cpp \
  -o a.o 
