# LTE5G
AVPs and Parameter search 

No doubt wireshark is a good open source tool with exellent filtering methods to troubleshoot the problems
However sometime there could be a need to collect the inforation in a more presentable manner. The purpose of this script to 
show the user-input based info from Exported Packet Dissections availabl in json, txt, and xml etc.

The json can be flattend or normalized with script or Pandas, as an example. However, I simply wrote a Python script using txt deissections to achieve the target. This scrip can be sued at any layer; Air, S1AP, GTPv2, Diameter, SIP etc. 

Here are some sample outputs

5G NSAir
--------

str_input = '5g rrc'

![image](https://user-images.githubusercontent.com/47313728/74648773-28eca200-5133-11ea-9066-7759b9385d1d.png)

SIP INVITE
----------
str_input = 'route uri'

![image](https://user-images.githubusercontent.com/47313728/74642451-dd80c680-5127-11ea-9d6a-220209d5ce1e.png)

str_input = 'media type'

![image](https://user-images.githubusercontent.com/47313728/74642788-7c0d2780-5128-11ea-95e3-c89a6c1be52d.png)

Diameter Cx LIR
---------------
str_input = 'public'

![image](https://user-images.githubusercontent.com/47313728/74717074-9573a980-51e4-11ea-9525-219bf8014979.png)

Diameter Cx LIA
---------------
str_input = 'server' 

![image](https://user-images.githubusercontent.com/47313728/74715315-0fa22f00-51e1-11ea-8c10-9b0de297a09d.png)