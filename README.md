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

Diameter Sh UDA
---------------
str_input = 'ps'

![image](https://user-images.githubusercontent.com/47313728/74729356-2e142480-51f9-11ea-9dc1-dc9c9860c9cd.png)

Diameter Rx AAR
---------------
str_input = '450'

![image](https://user-images.githubusercontent.com/47313728/74786345-5899c800-5261-11ea-98d1-9d2f9d50a135.png)

str_input = '513'

![image](https://user-images.githubusercontent.com/47313728/74813734-a71f8480-52aa-11ea-9a10-6b5ad49b7ff7.png)

Diameter S6a ULA
----------------
str_input = 'user-name'

![image](https://user-images.githubusercontent.com/47313728/74788220-fee7cc80-5265-11ea-9975-03d8dc7f5b18.png)

Diameter GxRAR
--------------


Diameter GxRAA
--------------
str_input = '278'

![image](https://user-images.githubusercontent.com/47313728/74814451-25305b00-52ac-11ea-9fa3-51824871c436.png)
