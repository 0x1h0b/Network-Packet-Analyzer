# Network-Packet-Analyzer 

## Short Description:-
This program allows us to analyze the ethernet/network packets (IPv4 Only) that are routed through our device.
On running this program it displays various important information about the packets origin and destination such as its
addresses and ports,apart from these we can also analyze different layers of the frame to further investigate on 
its segments (UDP ,TCP, ICMP) to display its version and protocol infos.

**NOTE**:- i have not considered the core data that the frame is carrying beacause most of the times it is encrypted 
          unless untill the protocol is http, as those data are not encrypted. HTTP data are packed inside the packet
          as plain text.
 

## Requirements:-
 
   **Python3 -** 
      It can be downloaded and install from it's [official website](https://www.python.org/downloads/).
      It is available for all types of platforms (windows , Linux and mac). In Linux/Mac it comes pre-installed.    
      Here i have used some of python's built in modules (*socket and struct*) for capturing and analyzing packets. 
     so there is no need of installing any external package. 
   
## How to use:-

 Download the project and extract it.          or 
  
  Open terminal and clone the project by typing the following (Assuming you want to save it in desktop)
```
 cd Desktop
 git clone https://github.com/hb10001/Network-Packet-Analyzer.git
 ```
 Now if you wish to clone  through terminal then you must install git first. 
 You can refer to their [official website](https://git-scm.com/) to install git.
 
 Open cmd  and navigate to the project location.
 
 for example if you have saved it in desktop, type-
 ```
 cd Desktop/Network-Packet-Analyzer/
 ```
 
 After you have reached inside the project folder. try listing files present inside it by the command-
 ```
 ls -la
 ```
 you should be able to see a python script 'main.py'.
 
 Now run the script-
 ``` 
 sudo python3 main.py
 ```
  As the code works by creating sockets, we need the root/administrator privelege to create them.
  By this you give permission to capture the network packets. 
 
 Thats it. Now the script should run properly without any error.
 
 
 **windows user-** 

As there is no sudo like option in  windows command line Interface.So make sure that at the time when you are 
 opening cmd , you run it as an administrator.
                    
 *Right-Click-On-CMD >> Run-As-Administrator*
 
 ## Output:-
 
 you should get an output similar to this -

![Output](Output.png "Sample Output")

## To Do:-

we know that HTTP data are not encrypted,they are transmitted as plain text.and also for the fact that they use port 80
as their source and destination ports. so we can use these facts to generalize that whenever the port address is 80 we 
should pass the core data to a function which is capable of properly formatting the texts and display it to the user.



 
