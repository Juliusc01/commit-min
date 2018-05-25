To run this basic example of delta, execute the following line:
../delta -test=hello.test -quiet -suffix=.java -name=HelloWorld -cp_minimal=min.java < HelloWorld.java

NOTE:
Can remove quiet if you want to see output
Suffix default is .c, probably could make .java to avoid this flag
Name is a flag I added which accepts the name of the java file without the ".java"
cp_minimal is the name of the outputted minimized file

