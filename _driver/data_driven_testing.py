from pyjavaproperties import properties
file_path=r""
input_stream=open(file_path,"r")

prop=properties()
prop.load(input_stream)
NAME=prop.getproperty("name")
AGE=