PWD=`pwd`/
echo "default user path"
rm a.o
echo $PWD
g++-4.8 -std=c++11 -fPIC -fpermissive \
  build_html.cpp \
  -o a.o 
./a.o
