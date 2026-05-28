## **Reticulum Network Stack** _**Release 1.3.0**_ 

## **Mark Qvist** 

**May 21, 2026** 

## **CONTENTS** 

|**1**|**What is Reticulum?**|**What is Reticulum?**||**3**|
|---|---|---|---|---|
||1.1|Current Status<br>. . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|3|
||1.2|Reference Implementation . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|3|
||1.3|What does Reticulum Ofer? . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|4|
||1.4|Where can Reticulum be Used? . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|5|
||1.5|Interface Types and Devices . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|5|
|**2**|**Getting Started Fast**|||**7**|
||2.1|Standalone Reticulum Installation . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|7|
|||2.1.1<br>Resolving Dependency & Installation Issues . . . . . . . . . . . . . . . . . . . . . . . . . .||7|
||2.2|Try Using a Reticulum-based Program|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|8|
||2.3|Using the Included Utilities<br>. . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|8|
||2.4|Creating a Network With Reticulum .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|8|
||2.5|Bootstrapping Connectivity<br>. . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|8|
|||2.5.1<br>Finding Your Way . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|9|
|||2.5.2<br>Build Personal Infrastructure|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|9|
|||2.5.3<br>Mixing Strategies . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|10|
|||2.5.4<br>Network Health & Responsibility. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||10|
|||2.5.5<br>Contributing to the Global Ret . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||10|
||2.6|Connect to the Distributed Backbone|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|10|
||2.7|Hosting Public Entrypoints. . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|11|
||2.8|Connecting Reticulum Instances Over the Internet<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .||12|
||2.9|Adding Radio Interfaces . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|12|
||2.10|Creating and Using Custom Interfaces|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|13|
||2.11|Develop a Program with Reticulum .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|13|
||2.12|Platform-Specifc Install Notes . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|13|
|||2.12.1<br>Android . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|13|
|||2.12.2<br>ARM64 . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|14|
|||2.12.3<br>Debian Bookworm . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|14|
|||2.12.4<br>MacOS<br>. . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|15|
|||2.12.5<br>OpenWRT. . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|16|
|||2.12.6<br>Raspberry Pi<br>. . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|16|
|||2.12.7<br>RISC-V . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|17|
|||2.12.8<br>Ubuntu Lunar . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|17|
|||2.12.9<br>Windows<br>. . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|18|
||2.13|Pure-Python Reticulum. . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|18|
|**3**|**Zen of Reticulum**|||**19**|
||3.1|The Illusion Of The Center. . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|19|
|||3.1.1<br>Fallacy Of The Cloud . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|19|



**i** 

|||3.1.2|Decentralization Or Uncentralizability?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|Decentralization Or Uncentralizability?<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|19|
|---|---|---|---|---|---|
|||3.1.3|Death To The Address|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|20|
||3.2|Physics Of Trust . . . . . . . .||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|20|
|||3.2.1|Hostile Environments .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|20|
|||3.2.2|Encryption Is Not A Feature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||21|
|||3.2.3|Zero-Trust Architectures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||21|
||3.3|Merits Of Scarcity . . . . . . .||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|21|
|||3.3.1|The Bandwidth Fallacy|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|22|
|||3.3.2|Cost Of A Byte . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|22|
|||3.3.3|Flow & Time . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|22|
|||3.3.4|Liberation From Limits|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|23|
||3.4|Sovereignty Through Infrastructure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|||23|
|||3.4.1|A Carrier-Grade Fallacy|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|23|
|||3.4.2|Personal Infrastructure|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|23|
|||3.4.3|The Ability To Disconnect . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||24|
||3.5|Identity and Nomadism<br>. . . .||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|24|
|||3.5.1|Portable Existence<br>. .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|24|
|||3.5.2|Roaming Nodes . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|24|
|||3.5.3|Announcing Presence .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|25|
|||3.5.4|Anchor In The Flow. .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|25|
||3.6|Ethics Of The Tool . . . . . . .||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|25|
|||3.6.1|The Harm Principle . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|26|
|||3.6.2|Public Domain Protocol|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|26|
|||3.6.3|Preserving Human Agency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||26|
||3.7|Design|Patterns For Post-IP Systems. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||27|
|||3.7.1|Store & Forward<br>. . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|27|
|||3.7.2|Naming Is Power . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|28|
|||3.7.3|The Interface Is The Medium . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||28|
|||3.7.4|Emergent Patterns . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|28|
||3.8|Fabric Of The Independent . . .||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|29|
|||3.8.1|The Work Is Finished .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|29|
|||3.8.2|Open Sky . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|29|
|**4**|**Programs Using Reticulum**||||**31**|
||4.1|Programs & Utilities . . . . . .||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|31|
|||4.1.1|Remote Shell . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|31|
|||4.1.2|Nomad Network. . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|32|
|||4.1.3|RNS Page Node . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|32|
|||4.1.4|Retipedia<br>. . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|32|
|||4.1.5|Sideband<br>. . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|33|
|||4.1.6|MeshChatX . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|34|
|||4.1.7|Reticulum Relay Chat .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|35|
|||4.1.8|RetiBBS . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|35|
|||4.1.9|RBrowser . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|36|
|||4.1.10|Reticulum Network Telephone . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||37|
|||4.1.11|LXST Phone<br>. . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|38|
|||4.1.12|LXMFy . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|39|
|||4.1.13|LXMF Interactive Client . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||39|
|||4.1.14|RNS FileSync . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|39|
|||4.1.15|Micron Parser JS . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|39|
|||4.1.16|RNMon . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|39|
||4.2|Protocols . . . . . . . . . . . .||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|40|
|||4.2.1|LXMF . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|40|
|||4.2.2|LXST . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|40|



**ii** 

|||4.2.3|RRC . . . . . . . . . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|40|
|---|---|---|---|---|---|---|---|
||4.3|Interface Modules & Connectivity Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|||||40|
|**5**|**Using**|**Reticulum on Your System**|||||**41**|
||5.1|Confguration & Data<br>. . . . . .||.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|41|
||5.2|Included Utility Programs . . . .||.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|44|
|||5.2.1|The rnsd Utility . . . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|45|
|||5.2.2|The rnstatus Utility . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|45|
|||5.2.3|The rnid Utility . . . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|47|
|||5.2.4|The rnpath Utility . . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|49|
|||5.2.5|The rnprobe Utility . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|50|
|||5.2.6|The rncp Utility . . . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|51|
|||5.2.7|The rngit Utility . . . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|52|
|||5.2.8|The rnx Utility<br>. . . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|53|
|||5.2.9|The rnsh Utility . . . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|54|
|||5.2.10|The rnodeconf Utility . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|58|
||5.3|Discovering Interfaces . . . . . .||.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|59|
||5.4|Remote|Management . . . . . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|61|
||5.5|Blackhole Management<br>. . . . .||.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|61|
|||5.5.1|Local Blackhole Management|||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|62|
|||5.5.2|Automated List Sourcing|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|62|
|||5.5.3|Publishing Blackhole Lists||.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|63|
||5.6|Improving System Confguration.||.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|64|
|||5.6.1|Fixed Serial Port Names|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|64|
|||5.6.2|Reticulum as a System Service . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||||64|
|**6**|**Understanding Reticulum**||||||**67**|
||6.1|Motivation . . . . . . . . . . . .||.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|67|
||6.2|Goals .|. . . . . . . . . . . . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|68|
||6.3|Introduction & Basic Functionality|||.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|68|
|||6.3.1|Destinations . . . . . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|69|
|||6.3.2|Public Key Announcements|||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|71|
|||6.3.3|Identities<br>. . . . . . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|71|
|||6.3.4|Getting Further . . . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|72|
||6.4|Reticulum Transport . . . . . . .||.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|72|
|||6.4.1|Node Types . . . . . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|72|
|||6.4.2|The Announce Mechanism in|||Detail . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|72|
|||6.4.3|Reaching the Destination|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|73|
|||6.4.4|Resources . . . . . . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|75|
||6.5|Network Identities . . . . . . . .||.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|76|
|||6.5.1|Conceptual Overview . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|76|
|||6.5.2|Current Usage . . . . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|76|
|||6.5.3|Future Implications . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|76|
|||6.5.4|Creating and Using a Network Identity . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||||77|
||6.6|Reference Setup<br>. . . . . . . . .||.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|77|
||6.7|Protocol Specifcs<br>. . . . . . . .||.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|78|
|||6.7.1|Packet Prioritisation. . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|78|
|||6.7.2|Interface Access Codes .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|78|
|||6.7.3|Wire Format. . . . . . .|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|79|
|||6.7.4|Announce Propagation Rules|||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|81|
|||6.7.5|Cryptographic Primitives|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|82|
|**7**|**Communications Hardware**||||||**85**|
||7.1|Combining Hardware Types . . .||.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|85|



**iii** 

||7.2|RNode<br>. . . . . . . . .|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|85|
|---|---|---|---|---|---|---|---|
|||7.2.1<br>Creating RNodes||.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|86|
|||7.2.2<br>Supported Boards||and||Devices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|86|
|||7.2.3<br>Installation<br>. .|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|92|
|||7.2.4<br>Usage with Reticulum||||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|93|
||7.3|WiFi-based Hardware<br>.|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|93|
||7.4|Ethernet-based Hardware||.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|93|
||7.5|Serial Lines & Devices .|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|93|
||7.6|Packet Radio Modems .|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|93|
|**8**|**Confguring Interfaces**||||||**95**|
||8.1|Custom Interfaces<br>. . .|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|95|
||8.2|Auto Interface<br>. . . . .|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|95|
||8.3|Backbone Interface . . .|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|97|
|||8.3.1<br>Listeners<br>. . .|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|97|
|||8.3.2<br>Connecting Remotes||||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|98|
||8.4|TCP Server Interface . .|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|98|
||8.5|TCP Client Interface . .|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|100|
||8.6|UDP Interface<br>. . . . .|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|101|
||8.7|I2P Interface . . . . . .|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|102|
||8.8|RNode LoRa Interface .|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|103|
||8.9|RNode Multi Interface .|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|105|
||8.10|Serial Interface . . . . .|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|107|
||8.11|Pipe Interface . . . . . .|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|107|
||8.12|KISS Interface . . . . .|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|108|
||8.13|AX.25 KISS Interface .|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|109|
||8.14|Discoverable Interfaces.|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|110|
|||8.14.1<br>Enabling Discovery|||.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|110|
|||8.14.2<br>Discovery Parameters||||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|110|
|||8.14.3<br>Interface Modes|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|112|
|||8.14.4<br>Security Considerations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|||||112|
|||8.14.5<br>Example Confguration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|||||113|
||8.15|Common Interface Options|||.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|114|
||8.16|Interface Modes<br>. . . .|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|115|
||8.17|Announce Rate Control|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|116|
||8.18|New Destination Rate Limiting||||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|117|
||8.19|Path Request Burst Control||.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|118|
|**9**|**Building Networks**||||||**121**|
||9.1|Concepts & Overview .|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|121|
|||9.1.1<br>Introductory Considerations<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|||||121|
|||9.1.2<br>Destinations, Not Addresses<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|||||122|
|||9.1.3<br>Transport Nodes|and||Instances . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .||123|
|||9.1.4<br>Trustless Networking||||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|124|
|||9.1.5<br>Heterogeneous Connectivity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|||||125|
|**10 **|**Distributed Development**||||||**127**|
||10.1|The Original Architecture||.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|127|
||10.2|The Platform Interregnum||.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|127|
||10.3|Restoration . . . . . . .|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|128|
||10.4|Protocols Over Platforms|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|129|
||10.5|Sovereignty Through Infrastructure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|||||129|
||10.6|Artifact-Centered Workfows|||.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|130|
||10.7|Composable Primitives .|.|.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|130|



**iv** 

||10.8|Distribution Without Intermediaries|Distribution Without Intermediaries|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131|
|---|---|---|---|---|---|
||10.9|Long Archive . . . . . . . . . . . .||.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131|
||10.10|Start Of|The Road<br>. . . . . . . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132|
|**11 **|**Git Over Reticulum**||||**133**|
||11.1|The rngit Utility<br>. . . . . . . . . .||.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133|
||11.2|Repository Creation & Management||.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135|
|||11.2.1|Creating Empty Repositories||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135|
|||11.2.2|Forking Repositories . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135|
|||11.2.3|Mirroring Repositories . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136|
|||11.2.4|Automatic Mirror Synchronization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137|||
|||11.2.5|Manual Synchronization<br>.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137|
|||11.2.6|Git Confguration Parameters||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138|
||11.3|Repository Structure . . . . . . . .||.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138|
|||11.3.1|Confguration . . . . . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138|
||11.4|Permissions . . . . . . . . . . . . .||.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139|
|||11.4.1|Permission Types . . . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139|
|||11.4.2|Permission Hierarchy . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139|
|||11.4.3|Confguration Methods . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140|
|||11.4.4|Work Document Permissions||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140|
|||11.4.5|Creator Permissions . . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140|
|||11.4.6|Permission Examples . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141|
|||11.4.7|Permission Short Forms<br>.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141|
|||11.4.8|Permission Confguration Locations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142|||
||11.5|Remote|Permission Management<br>.|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142|
|||11.5.1|Managing Group Permissions||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142|
|||11.5.2|Managing Repository Permissions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142|||
|||11.5.3|Permission Validation . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142|
||11.6|Identity|& Destination Aliases . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143|
||11.7|Serving|Pages Over Nomad Network||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143|
|||11.7.1|Enabling the Git Page Node||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144|
|||11.7.2|Accessing Repository Pages||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144|
|||11.7.3|Formatting & Syntax Highlighting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144|||
|||11.7.4|Customizing Templates . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145|
|||11.7.5|Repository Statistics<br>. . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146|
|||11.7.6|Confguration Example . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146|
||11.8|Verifed|Releases . . . . . . . . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146|
|||11.8.1|Obtaining Verifed Releases||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147|
|||11.8.2|Creating Signed Releases .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149|
||11.9|Release|Management . . . . . . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151|
|||11.9.1|The Release Workfow<br>. .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151|
|||11.9.2|Release Storage & Structure||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151|
|||11.9.3|Command-Line Interaction|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151|
||11.10|Work Documents . . . . . . . . . .||.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154|
|||11.10.1|Working With Work Documents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154|||
|||11.10.2|Proposing Work Documents||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155|
|||11.10.3|State Management<br>. . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155|
|||11.10.4|Managing Work Document Permissions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156|||
|||11.10.5|Cryptographic Attribution|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157|
|**12 **|**Support Reticulum**||||**159**|
||12.1|Donations. . . . . . . . . . . . . .||.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159|
||12.2|Provide|Feedback. . . . . . . . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 160|



**v** 

|**13 Code Examples**|**13 Code Examples**||**161**|
|---|---|---|---|
|13.1|Minimal<br>. . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161|
|13.2|Announce. . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163|
|13.3|Broadcast . . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167|
|13.4|Echo<br>. . . . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169|
|13.5|Link. . . . . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176|
|13.6|Identifcation . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 181|
|13.7|Requests & Responses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188|||
|13.8|Channel . . . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193|
|13.9|Bufer . . . . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201|
|13.10 Filetransfer . . .||.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207|
|13.11 Custom Interfaces|||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 219|
|**14 Reticulum License**|||**227**|
|**15 API Reference**|||**229**|
|15.1|Reticulum. . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 229|
|15.2|Identity . . . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 231|
|15.3|Destination . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 234|
|15.4|Packet. . . . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 238|
|15.5|Packet Receipt .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239|
|15.6|Link. . . . . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 240|
|15.7|Request Receipt|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243|
|15.8|Resource . . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244|
|15.9|Channel . . . . .|.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245|
|15.10 MessageBase . .||.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246|
|15.11 Bufer . . . . . .||.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247|
|15.12 RawChannelReader|||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 248|
|15.13 RawChannelWriter|||. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 248|
|15.14 Transport . . . .||.|. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 249|
|**Index**|||**251**|



**vi** 

**Reticulum Network Stack, Release 1.3.0** 

This manual aims to provide you with all the information you need to understand Reticulum, build networks or develop programs using it, or to participate in the development of Reticulum itself. 

**CONTENTS** 

**1** 

**Reticulum Network Stack, Release 1.3.0** 

**CONTENTS** 

**2** 

**CHAPTER ONE** 

## **WHAT IS RETICULUM?** 

Reticulum is a cryptography-based networking stack for building both local and wide-area networks with readily available hardware, that can continue to operate under adverse conditions, such as extremely low bandwidth and very high latency. 

To understand the foundational philosophy and goals of this system, read the _Zen of Reticulum_ . 

Reticulum allows you to build wide-area networks with off-the-shelf tools, and offers end-to-end encryption, forward secrecy, autoconfiguring cryptographically backed multi-hop transport, efficient addressing, unforgeable packet acknowledgements and more. 

From a users perspective, Reticulum allows the creation of applications that respect and empower the autonomy and sovereignty of communities and individuals. Reticulum enables secure digital communication that cannot be subjected to outside control, manipulation or censorship. 

Reticulum enables the construction of both small and potentially planetary-scale networks, without any need for hierarchical or bureaucratic structures to control or manage them, while ensuring individuals and communities full sovereignty over their own network segments. 

Reticulum is a **complete networking stack** , and does not need IP or higher layers, although it is easy to utilise IP (with TCP or UDP) as the underlying carrier for Reticulum. It is therefore trivial to tunnel Reticulum over the Internet or private IP networks. Reticulum is built directly on cryptographic principles, allowing resilience and stable functionality in open and trustless networks. 

No kernel modules or drivers are required. Reticulum can run completely in userland, and will run on practically any system that runs Python 3. Reticulum runs well even on small single-board computers like the Pi Zero. 

## **1.1 Current Status** 

All core protocol features are implemented and functioning, but additions will probably occur as real-world use is explored. The API and wire-format can be considered complete and stable, but could change if absolutely warranted. 

## **1.2 Reference Implementation** 

The Python code, for which this documentation is written, and known as the Reticulum Network Stack, is the Reference Implementation of Reticulum. The Reticulum Protocol is defined entirely and authoritatively by this reference implementation, and this manual. It is maintained by Mark Qvist, identified by the Reticulum Identity `<bc7291552be7a58f361522990465165c>` . 

Compatibility with the Reticulum Protocol is defined as having full interoperability, and sufficient functional parity with this reference implementation. Any specific protocol implementation that achieves this is Reticulum. Any that does not is not Reticulum. 

The reference implementation is licensed under the _Reticulum License_ . 

**3** 

**Reticulum Network Stack, Release 1.3.0** 

The Reticulum Protocol was dedicated to the Public Domain in 2016. 

## **1.3 What does Reticulum Offer?** 

- Coordination-less globally unique addressing and identification 

- Fully self-configuring multi-hop routing over heterogeneous carriers 

- Flexible scalability over heterogeneous topologies 

   - Reticulum can carry data over any mixture of physical mediums and topologies 

   - Low-bandwidth networks can co-exist and interoperate with large, high-bandwidth networks 

- Initiator anonymity, communicate without revealing your identity 

   - Reticulum does not include source addresses on any packets 

- Asymmetric X25519 encryption and Ed25519 signatures as a basis for all communication 

   - The foundational Reticulum Identity Keys are 512-bit Elliptic Curve keysets 

- Forward Secrecy is available for all communication types, both for single packets and over links 

- Reticulum uses the following format for encrypted tokens: 

   - Ephemeral per-packet and link keys and derived from an ECDH key exchange on Curve25519 

   - AES-256 in CBC mode with PKCS7 padding 

   - HMAC using SHA256 for authentication 

   - IVs are generated through os.urandom() 

- Unforgeable packet delivery confirmations 

- Flexible and extensible interface system 

   - Reticulum includes a large variety of built-in interface types 

   - Ability to load and utilise custom user- or community-supplied interface types 

   - Easily create your own custom interfaces for communicating over anything 

- Authentication and virtual network segmentation on all supported interface types 

- An intuitive and easy-to-use API 

   - Simpler and easier to use than sockets APIs and simpler, but more powerful 

   - Makes building distributed and decentralised applications much simpler 

- Reliable and efficient transfer of arbitrary amounts of data 

   - Reticulum can handle a few bytes of data or files of many gigabytes 

   - Sequencing, compression, transfer coordination and checksumming are automatic 

   - The API is very easy to use, and provides transfer progress 

- Lightweight, flexible and expandable Request/Response mechanism 

- Efficient link establishment 

   - Total cost of setting up an encrypted and verified link is only 3 packets, totalling 297 bytes 

   - Low cost of keeping links open at only 0.44 bits per second 

- Reliable sequential delivery with Channel and Buffer mechanisms 

**Chapter 1. What is Reticulum?** 

**4** 

**Reticulum Network Stack, Release 1.3.0** 

## **1.4 Where can Reticulum be Used?** 

Over practically any medium that can support at least a half-duplex channel with greater throughput than 5 bits per second, and an MTU of 500 bytes. Data radios, modems, LoRa radios, serial lines, AX.25 TNCs, amateur radio digital modes, ad-hoc WiFi, free-space optical links and similar systems are all examples of the types of interfaces Reticulum was designed for. 

An open-source LoRa-based interface called RNode has been designed as an example transceiver that is very suitable for Reticulum. It is possible to build it yourself, to transform a common LoRa development board into one, or it can be purchased as a complete transceiver from various vendors. 

Reticulum can also be encapsulated over existing IP networks, so there’s nothing stopping you from using it over wired Ethernet or your local WiFi network, where it’ll work just as well. In fact, one of the strengths of Reticulum is how easily it allows you to connect different mediums into a self-configuring, resilient and encrypted mesh. 

As an example, it’s possible to set up a Raspberry Pi connected to both a LoRa radio, a packet radio TNC and a WiFi network. Once the interfaces are added, Reticulum will take care of the rest, and any device on the WiFi network can communicate with nodes on the LoRa and packet radio sides of the network, and vice versa. 

## **1.5 Interface Types and Devices** 

Reticulum implements a range of generalised interface types that covers the communications hardware that Reticulum can run over. If your hardware is not supported, it’s simple to _implement an interface class_ . Currently, Reticulum can use the following devices and communication mediums: 

- Any Ethernet device 

   - WiFi devices 

   - Wired Ethernet devices 

   - Fibre-optic transceivers 

   - Data radios with Ethernet ports 

- LoRa using RNode 

   - Can be installed on many popular LoRa boards 

   - Can be purchased as a ready to use transceiver 

- Packet Radio TNCs, such as OpenModem 

   - Any packet radio TNC in KISS mode 

   - Ideal for VHF and UHF radio 

- Any device with a serial port 

- The I2P network 

- TCP over IP networks 

- UDP over IP networks 

- Anything you can connect via stdio 

   - Reticulum can use external programs and pipes as interfaces 

   - This can be used to easily hack in virtual interfaces 

   - Or to quickly create interfaces with custom hardware 

- Anything else using _custom interface modules_ written in Python 

**1.4. Where can Reticulum be Used?** 

**5** 

**Reticulum Network Stack, Release 1.3.0** 

For a full list and more details, see the _Supported Interfaces_ chapter. 

**Chapter 1. What is Reticulum?** 

**6** 

**CHAPTER TWO** 

## **GETTING STARTED FAST** 

The best way to get started with the Reticulum Network Stack depends on what you want to do. This guide will outline sensible starting paths for different scenarios. 

## **2.1 Standalone Reticulum Installation** 

If you simply want to install Reticulum and related utilities on a system, the easiest way is via the `pip` package manager: 

```
pipinstallrns
```

If you do not already have pip installed, you can install it using the package manager of your system with a command like `sudo apt install python3-pip` , `sudo pamac install python-pip` or similar. 

You can also dowload the Reticulum release wheels from GitHub, or other release channels, and install them offline using `pip` : 

```
pipinstall./rns-1.1.2-py3-none-any.whl
```

On platforms that limit user package installation via `pip` , you may need to manually allow this using the `--break-system-packages` command line flag when installing. This will not actually break any packages, unless you have installed Reticulum directly via your operating system’s package manager. 

```
pipinstallrns--break-system-packages
```

For more detailed installation instructions, please see the _Platform-Specific Install Notes_ section. 

After installation is complete, it might be helpful to refer to the _Using Reticulum on Your System_ chapter. 

## **2.1.1 Resolving Dependency & Installation Issues** 

On some platforms, there may not be binary packages available for all dependencies, and `pip` installation may fail with an error message. In these cases, the issue can usually be resolved by installing the development essentials packages for your platform: 

```
#Debian/Ubuntu/Derivatives
sudoaptinstallbuild-essential
#Arch/Manjaro/Derivatives
sudopamacinstallbase-devel
```

```
#Fedora
sudodnfgroupinstall"DevelopmentTools""DevelopmentLibraries"
```

**7** 

**Reticulum Network Stack, Release 1.3.0** 

With the base development packages installed, `pip` should be able to compile any missing dependencies from source, and complete installation even on platforms that don’t have pre- compiled packages available. 

## **2.2 Try Using a Reticulum-based Program** 

If you simply want to try using a program built with Reticulum, a _range of different programs_ exist that allow basic communication and a various other useful functions, even over extremely low-bandwidth Reticulum networks. 

## **2.3 Using the Included Utilities** 

Reticulum comes with a range of included utilities that make it easier to manage your network, check connectivity and make Reticulum available to other programs on your system. 

You can use `rnsd` to run Reticulum as a background or foreground service, and the `rnstatus` , `rnpath` and `rnprobe` utilities to view and query network status and connectivity. 

To learn more about these utility programs, have a look at the _Using Reticulum on Your System_ chapter of this manual. 

## **2.4 Creating a Network With Reticulum** 

To create a network, you will need to specify one or more _interfaces_ for Reticulum to use. This is done in the Reticulum configuration file, which by default is located at `~/.reticulum/config` . You can get an example configuration file with all options via `rnsd --exampleconfig` . 

When Reticulum is started for the first time, it will create a default configuration file, with one active interface. This default interface uses your existing Ethernet and WiFi networks (if any), and only allows you to communicate with other Reticulum peers within your local broadcast domains. 

To communicate further, you will have to add one or more interfaces. The default configuration includes a number of examples, ranging from using TCP over the internet, to LoRa and Packet Radio interfaces. 

With Reticulum, you only need to configure what interfaces you want to communicate over. There is no need to configure address spaces, subnets, routing tables, or other things you might be used to from other network types. 

Once Reticulum knows which interfaces it should use, it will automatically discover topography and configure transport of data to any destinations it knows about. 

In situations where you already have an established WiFi or Ethernet network, and many devices that want to utilise the same external Reticulum network paths (for example over LoRa), it will often be sufficient to let one system act as a Reticulum gateway, by adding any external interfaces to the configuration of this system, and then enabling transport on it. Any other device on your local WiFi will then be able to connect to this wider Reticulum network just using the default ( _AutoInterface_ ) configuration. 

Possibly, the examples in the config file are enough to get you started. If you want more information, you can read the _Building Networks_ and _Interfaces_ chapters of this manual, but most importantly, start with reading the next section, _Bootstrapping Connectivity_ , as this provides the most essential understanding of how to ensure reliable connectivity with a minimum of maintenance. 

## **2.5 Bootstrapping Connectivity** 

Reticulum is not a service you subscribe to, nor is it a single global network you “join”. It is a _networking stack_ ; a toolkit for building communications systems that align with your specific values, requirements, and operational environment. The way you choose to connect to other Reticulum peers is entirely your own choice. 

**Chapter 2. Getting Started Fast** 

**8** 

**Reticulum Network Stack, Release 1.3.0** 

One of the most powerful aspects of Reticulum is that it provides a multitude of tools to establish, maintain, and optimize connectivity. You can use these tools in isolation or combine them in complex configurations to achieve a vast array of goals. 

Whether your aim is to create a completely private, air-gapped network for your family; to build a resilient community mesh that survives infrastructure collapse; to connect far and wide to as many nodes as possible; or simply to maintain a reliable, encrypted link to a specific organization you care about, Reticulum provides the mechanisms to make it happen. 

There is no “right” or “wrong” way to build a Reticulum network, and you don’t need to be a network engineer just to get started. If the information flows in the way you intend, and your privacy and security requirements are met, your configuration is a success. Reticulum is designed to make the most challenging and difficult scenarios attainable, even when other networking technologies fail. 

## **2.5.1 Finding Your Way** 

When you first start using Reticulum, you need a way to obtain connectivity with the peers you want to communicate with - the process of _bootstrapping connectivity_ . 

## **Important** 

A common mistake in modern networking is the reliance on a few centralized, hard-coded entrypoints. If every user simply connects to the same list of public IP addresses found on a website, the network becomes brittle, centralized, and ultimately fails to deliver on the promise of decentralization and resilience. You have a responsibility here. 

Reticulum encourages the approach of _organic growth_ . Instead of relying on permanent static connections to distant servers, you can use temporary bootstrap connections to continously _discover_ more relevant or local infrastructure. Once discovered, your system can automatically form stronger, more direct links to these peers, and discard the temporary bootstrap links. This results in a web of connections that are geographically relevant, resilient and efficient. 

It _is_ possible to simply add a few public entrypoints to the `[interfaces]` section of your Reticulum configuration and be connected, but a better option is to enable _interface discovery_ and either manually select relevant, local interfaces, or enable discovered interface auto-connection. 

A relevant option in this context is the _bootstrap only_ interface option. This is an automated tool for better distributing connectivity. By enabling interface discovery and auto-connection, and marking an interface as `bootstrap_only` , you tell Reticulum to use that interface primarliy to find connectivity options, and then disconnect it once sufficient entrypoints have been discovered. This helps create a network topology that favors locality and resilience over the simple centralization caused by using only a few static entrypoints. 

Good places to find interface definitions for bootstrapping connectivity are websites like directory.rns.recipes and rmap.world. 

## **2.5.2 Build Personal Infrastructure** 

You do not need a datacenter to be a meaningful part of the Reticulum ecosystem. In fact, the most important nodes in the network are often the smallest ones. 

We strongly encourage everyone, even home users, to think in terms of building **personal infrastructure** . Don’t connect every phone, tablet, and computer in your house directly to a public internet gateway. Instead, repurpose an old computer, a Raspberry Pi, or a supported router to act as your own, personal **Transport Node** : 

- Your local Transport Node sits in your home, connected to your WiFi and perhaps a radio interface (like an RNode). 

- You configure this node with a `bootstrap_only` interface (perhaps a TCP tunnel to a wider network) and enable interface discovery. 

**2.5. Bootstrapping Connectivity** 

**9** 

**Reticulum Network Stack, Release 1.3.0** 

- While you sleep, work, or cook, your node listens to the network. It discovers other local community members, validates their Network Identities, and automatically establishes direct links. 

- Your personal devices now connect to your _local_ node, which is integrated into a living, breathing local mesh. Your traffic flows through local paths provided by other real people in the community rather than bouncing off a distant server. 

**Don’t wait for others to build the networks you want to see** . Every network is important, perhaps even most so those that support individual families and persons. Once enough of this personal, local infrastructure exist, connecting them directly to each other, without traversing the public Internet, becomes inevitable. 

## **2.5.3 Mixing Strategies** 

There is no requirement to commit to a single strategy. The most robust setups often mix static, dynamic, and discovered interfaces. 

- **Static Interfaces:** You maintain a permanent interface to a trusted friend or organization using a static configuration. 

- **Bootstrap Links:** You connect a `bootstrap_only` interface to a public gateway on the Internet to scan for new connectable peers or to regain connectivity if your other interfaces fail. 

- **Local Wide-Area Connectivity:** You run a `RNodeInterface` on a shared frequency, giving you completely self-sovereign and private wide-area access to both your own network and other Reticulum peers globally, without any “service providers” being able to control or monitor how you interact with people. 

By combining these methods, you create a system that is secure against single points of failure, adaptable to changing network conditions, and better integrated into your physical and social reality. 

## **2.5.4 Network Health & Responsibility** 

As you participate in the wider networks you discover and build, you will inevitably encounter peers that are misconfigured, malicious, or simply broken. To protect your resources and those of your local peers, you can utilize the _Blackhole Management_ system. 

Whether you manually block a spamming identity or subscribe to a blackhole list maintained by a trusted Network Identity, these tools help ensure that _your_ transport capacity is used for what _you_ consider legitimate communication. This keeps your local segment efficient and contributes to the health of the wider network. 

## **2.5.5 Contributing to the Global Ret** 

If you have the means to host a stable node with a public IP address, consider becoming a _Public Entrypoint_ . By _publishing your interface as discoverable_ , you provide a potential connection point for others, helping the network grow and reach new areas. 

For guidelines on how to properly configure a public entrypoint, refer to the _Hosting Public Entrypoints_ section. 

## **2.6 Connect to the Distributed Backbone** 

A global, distributed backbone of Reticulum Transport Nodes is being run by volunteers from around the world. This network constitutes a heterogenous collection of both public and private nodes that form an uncoordinated, voluntary inter-networking backbone that currently provides global transport and internetworking capabilities for Reticulum. 

As a good starting point, you can find interface definitions for connecting your own networks to this backbone on websites such as directory.rns.recipes and rmap.world. 

**Chapter 2. Getting Started Fast** 

**10** 

**Reticulum Network Stack, Release 1.3.0** 

## **Tip** 

Don’t rely on just a single connection to the distributed backbone for everyday use. It is much better to have several redundant connections configured, and enable the interface discovery options, so your nodes can continously discover peering opportunities as the network evolves. Refer to the _Bootstrapping Connectivity_ section to understand the options. 

## **2.7 Hosting Public Entrypoints** 

If you want to help build a strong global interconnection backbone, you can host a public (or private) entry-point to a Reticulum network over the Internet. This section offers some helpful pointers. Once you have set up your public entrypoint, it is a great idea to _make it discoverable over Reticulum_ . 

You will need a machine, physical or virtual with a public IP address, that can be reached by other devices on the Internet. 

The most efficient and performant way to host a connectable entry-point supporting many users is to use the `BackboneInterface` . This interface type is fully compatible with the `TCPClientInterface` and `TCPServerInterface` types, but much faster and uses less system resources, allowing your device to handle thousands of connections even on small systems. 

It is also important to set your connectable interface to `gateway` mode, since this will greatly improve network convergence time and path resolution for anyone connecting to your entry-point. 

```
#Thisexampledemonstratesabackboneinterface
#configuredforactingasagatewayforusersto
#connecttoeitherapublicorprivatenetwork
[[PublicGateway]]
type=BackboneInterface
enabled=yes
mode=gateway
listen_on=0.0.0.0
port=4242
#Onpubliclyavailableinterfaces,itis
#essentialtoconfiguresensibleannounce
#ratetargets.
announce_rate_target=3600
announce_rate_penalty=3600
announce_rate_grace=6
```

If instead you want to make a private entry-point from the Internet, you can use the _IFAC name and passphrase options_ to secure your interface with a network name and passphrase. 

```
#Aprivateentry-pointrequiringapre-shared
#networknameandpassphrasetoconnectto.
[[PrivateGateway]]
type=BackboneInterface
enabled=yes
mode=gateway
listen_on=0.0.0.0
```

(continues on next page) 

**2.7. Hosting Public Entrypoints** 

**11** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) `port = 4242 network_name = private_ret passphrase = 2owjajquafIanPecAc` 

If you are hosting an entry-point on an operating system that does not support `BackboneInterface` , you can use `TCPServerInterface` instead, although it will not be as performant. 

## **2.8 Connecting Reticulum Instances Over the Internet** 

Reticulum currently offers three interfaces suitable for connecting instances over the Internet: _Backbone_ , _TCP_ and _I2P_ . Each interface offers a different set of features, and Reticulum users should carefully choose the interface which best suites their needs. 

The `TCPServerInterface` allows users to host an instance accessible over TCP/IP. This method is generally faster, lower latency, and more energy efficient than using `I2PInterface` , however it also leaks more data about the server host. 

The `BackboneInterface` is a very fast and efficient interface type available on POSIX operating systems, designed to handle thousands of connections simultaneously with low memory, processing and I/O overhead. It is fully compatible with the TCP-based interface types. 

TCP connections reveal the IP address of both your instance and the server to anyone who can inspect the connection. Someone could use this information to determine your location or identity. Adversaries inspecting your packets may be able to record packet metadata like time of transmission and packet size. Even though Reticulum encrypts traffic, TCP does not, so an adversary may be able to use packet inspection to learn that a system is running Reticulum, and what other IP addresses connect to it. Hosting a publicly reachable instance over TCP also requires a publicly reachable IP address, which most Internet connections don’t offer anymore. 

The `I2PInterface` routes messages through the Invisible Internet Protocol (I2P). To use this interface, users must also run an I2P daemon in parallel to `rnsd` . For always-on I2P nodes it is recommended to use i2pd. 

By default, I2P will encrypt and mix all traffic sent over the Internet, and hide both the sender and receiver Reticulum instance IP addresses. Running an I2P node will also relay other I2P user’s encrypted packets, which will use extra bandwidth and compute power, but also makes timing attacks and other forms of deep-packet-inspection much more difficult. 

I2P also allows users to host globally available Reticulum instances from non-public IP’s and behind firewalls and NAT. 

In general it is recommended to use an I2P node if you want to host a publicly accessible instance, while preserving anonymity. If you care more about performance, and a slightly easier setup, use TCP. 

## **2.9 Adding Radio Interfaces** 

Once you have Reticulum installed and working, you can add radio interfaces with any compatible hardware you have available. Reticulum supports a wide range of radio hardware, and if you already have any available, it is very likely that it will work with Reticulum. For information on how to configure this, see the _Interfaces_ section of this manual. 

If you do not already have transceiver hardware available, you can easily and cheaply build an _RNode_ , which is a general-purpose long-range digital radio transceiver, that integrates easily with Reticulum. 

To build one yourself requires installing a custom firmware on a supported LoRa development board with an auto-install script or web-based flasher. Please see the _Communications Hardware_ chapter for a guide. If you prefer purchasing a ready-made unit, you can refer to the list of suppliers. 

Other radio-based hardware interfaces are being developed and made available by the broader Reticulum community. You can find more information on such topics over Reticulum-based information sharing systems. 

**Chapter 2. Getting Started Fast** 

**12** 

**Reticulum Network Stack, Release 1.3.0** 

If you have communications hardware that is not already supported by any of the _existing interface types_ , it is easy to write (and potentially publish) a _custom interface module_ that makes it compatible with Reticulum. 

## **2.10 Creating and Using Custom Interfaces** 

While Reticulum includes a flexible and broad range of built-in interfaces, these will not cover every conceivable type of communications hardware that Reticulum can potentially use to communicate. 

It is therefore possible to easily write your own interface modules, that can be loaded at run-time and used on-par with any of the built-in interface types. 

For more information on this subject, and code examples to build on, please see the _Configuring Interfaces_ chapter. 

## **2.11 Develop a Program with Reticulum** 

If you want to develop programs that use Reticulum, the easiest way to get started is to install the latest release of Reticulum via pip: 

```
pipinstallrns
```

The above command will install Reticulum and dependencies, and you will be ready to import and use RNS in your own programs. The next step will most likely be to look at some _Example Programs_ . 

The entire Reticulum API is documented in the _API Reference_ chapter of this manual. Before diving in, it’s probably a good idea to read this manual in full, but at least start with the _Understanding Reticulum_ chapter. 

## **2.12 Platform-Specific Install Notes** 

Some platforms require a slightly different installation procedure, or have various quirks that are worth being aware of. These are listed here. 

## **2.12.1 Android** 

Reticulum can be used on Android in different ways. The easiest way to get started is using an app like Sideband. 

For more control and features, you can use Reticulum and related programs via the Termux app, at the time of writing available on F-droid. 

Termux is a terminal emulator and Linux environment for Android based devices, which includes the ability to use many different programs and libraries, including Reticulum. 

To use Reticulum within the Termux environment, you will need to install `python` and the `python-cryptography` library using `pkg` , the package-manager build into Termux. After that, you can use `pip` to install Reticulum. 

From within Termux, execute the following: 

```
#First,makesureindexesandpackagesareuptodate.
pkgupdate
pkgupgrade
#Theninstallpythonandthecryptographylibrary.
pkginstallpythonpython-cryptography
#Makesurepipisuptodate,andinstallthewheelmodule.
pipinstallwheelpip--upgrade
```

(continues on next page) 

**2.10. Creating and Using Custom Interfaces** 

**13** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
#InstallReticulum
pipinstallrns
```

If for some reason the `python-cryptography` package is not available for your platform via the Termux package manager, you can attempt to build it locally on your device using the following command: 

```
#First,makesureindexesandpackagesareuptodate.
pkgupdate
pkgupgrade
#Theninstalldependenciesforthecryptographylibrary.
pkginstallpythonbuild-essentialopenssllibffirust
#Makesurepipisuptodate,andinstallthewheelmodule.
pipinstallwheelpip--upgrade
#Toallowtheinstallertobuildthecryptographymodule,
#weneedtoletitknowwhatplatformwearecompilingfor:
exportCARGO_BUILD_TARGET="aarch64-linux-android"
#Starttheinstallprocessforthecryptographymodule.
#Dependingonyourdevice,thiscantakeseveralminutes,
#sincethemodulemustbecompiledlocallyonyourdevice.
pipinstallcryptography
#Iftheaboveinstallationsucceeds,youcannowinstall
#Reticulumandanyrelatedsoftware
pipinstallrns
```

It is also possible to include Reticulum in apps compiled and distributed as Android APKs. A detailed tutorial and example source code will be included here at a later point. Until then you can use the Sideband source code as an example and starting point. 

## **2.12.2 ARM64** 

On some architectures, including ARM64, not all dependencies have precompiled binaries. On such systems, you may need to install `python3-dev` (or similar) before installing Reticulum or programs that depend on Reticulum. 

```
#InstallPythonanddevelopmentpackages
sudoaptupdate
sudoaptinstallpython3python3-pippython3-dev
#InstallReticulum
python3-mpipinstallrns
```

With these packages installed, `pip` will be able to build any missing dependencies on your system locally. 

## **2.12.3 Debian Bookworm** 

On versions of Debian released after April 2023, it is no longer possible by default to use `pip` to install packages onto your system. Unfortunately, you will need to use the replacement `pipx` command instead, which places installed packages in an isolated environment. This should not negatively affect Reticulum, but will not work for including and using Reticulum in your own scripts and programs. 

**Chapter 2. Getting Started Fast** 

**14** 

**Reticulum Network Stack, Release 1.3.0** 

```
#Installpipx
sudoaptinstallpipx
#Makeinstalledprogramsavailableonthecommandline
pipxensurepath
#InstallReticulum
pipxinstallrns
```

Alternatively, you can restore normal behaviour to `pip` by creating or editing the configuration file located at `~/. config/pip/pip.conf` , and adding the following section: 

```
[global]
break-system-packages=true
```

For a one-shot installation of Reticulum, without globally enabling the `break-system-packages` option, you can use the following command: 

```
pipinstallrns--break-system-packages
```

## **Note** 

The `--break-system-packages` directive is a somewhat misleading choice of words. Setting it will of course not break any system packages, but will simply allow installing `pip` packages user- and system-wide. While this _could_ in rare cases lead to version conflicts, it does not generally pose any problems, especially not in the case of installing Reticulum. 

## **2.12.4 MacOS** 

To install Reticulum on macOS, you will need to have Python and the `pip` package manager installed. 

Systems running macOS can vary quite widely in whether or not Python is pre-installed, and if it is, which version is installed, and whether the `pip` package manager is also installed and set up. If in doubt, you can download and install Python manually. 

When Python and `pip` is available on your system, simply open a terminal window and use one of the following commands: 

```
#InstallReticulumandutilitieswithpip:
pip3installrns
```

```
#Onsomeversions,youmayneedtousethe
#flag--break-system-packagestoinstall:
pip3installrns--break-system-packages
```

## **Note** 

The `--break-system-packages` directive is a somewhat misleading choice of words. Setting it will of course not break any system packages, but will simply allow installing `pip` packages user- and system-wide. While this _could_ in rare cases lead to version conflicts, it does not generally pose any problems, especially not in the case of installing Reticulum. 

**2.12. Platform-Specific Install Notes** 

**15** 

**Reticulum Network Stack, Release 1.3.0** 

Additionally, some version combinations of macOS and Python require you to manually add your installed `pip` packages directory to your _PATH_ environment variable, before you can use installed commands in your terminal. Usually, adding the following line to your shell init script (for example `~/.zshrc` ) will be enough: 

```
exportPATH=$PATH:~/Library/Python/3.9/bin
```

Adjust Python version and shell init script location according to your system. 

## **2.12.5 OpenWRT** 

On OpenWRT systems with sufficient storage and memory, you can install Reticulum and related utilities using the _opkg_ package manager and _pip_ . 

## **Note** 

At the time of releasing this manual, work is underway to create pre-built Reticulum packages for OpenWRT, with full configuration, service and `uci` integration. Please see the feed-reticulum and reticulum-openwrt repositories for more information. 

To install Reticulum on OpenWRT, first log into a command line session, and then use the following instructions: 

```
#Installdependencies
opkginstallpython3python3-pippython3-cryptographypython3-pyserial
```

```
#InstallReticulum
pipinstallrns
#Startrnsdwithdebugloggingenabled
rnsd-vvv
```

## **Note** 

The above instructions have been verified and tested on OpenWRT 21.02 only. It is likely that other versions may require slightly altered installation commands or package names. You will also need enough free space in your overlay FS, and enough free RAM to actually run Reticulum and any related programs and utilities. 

Depending on your device configuration, you may need to adjust firewall rules for Reticulum connectivity to and from your device to work. Until proper packaging is ready, you will also need to manually create a service or startup script to automatically laucnh Reticulum at boot time. 

Please also note that the _AutoInterface_ requires link-local IPv6 addresses to be enabled for any Ethernet and WiFi devices you intend to use. If `ip a` shows an address starting with `fe80::` for the device in question, `AutoInterface` should work for that device. 

## **2.12.6 Raspberry Pi** 

It is currently recommended to use a 64-bit version of the Raspberry Pi OS if you want to run Reticulum on Raspberry Pi computers, since 32-bit versions don’t always have packages available for some dependencies. If Python and the _pip_ package manager is not already installed, do that first, and then install Reticulum using _pip_ . 

```
#Installdependencies
```

```
sudoaptinstallpython3python3-pippython3-cryptographypython3-pyserial
```

(continues on next page) 

**Chapter 2. Getting Started Fast** 

**16** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
#InstallReticulum
pipinstallrns--break-system-packages
```

## **Note** 

The `--break-system-packages` directive is a somewhat misleading choice of words. Setting it will of course not break any system packages, but will simply allow installing `pip` packages user- and system-wide. While this _could_ in rare cases lead to version conflicts, it does not generally pose any problems, especially not in the case of installing Reticulum. 

While it is possible to install and run Reticulum on 32-bit Rasperry Pi OSes, it will require manually configuring and installing required build dependencies, and is not detailed in this manual. 

## **2.12.7 RISC-V** 

On some architectures, including RISC-V, not all dependencies have precompiled binaries. On such systems, you may need to install `python3-dev` (or similar) before installing Reticulum or programs that depend on Reticulum. 

```
#InstallPythonanddevelopmentpackages
sudoaptupdate
sudoaptinstallpython3python3-pippython3-dev
#InstallReticulum
python3-mpipinstallrns
```

With these packages installed, `pip` will be able to build any missing dependencies on your system locally. 

## **2.12.8 Ubuntu Lunar** 

On versions of Ubuntu released after April 2023, it is no longer possible by default to use `pip` to install packages onto your system. Unfortunately, you will need to use the replacement `pipx` command instead, which places installed packages in an isolated environment. This should not negatively affect Reticulum, but will not work for including and using Reticulum in your own scripts and programs. 

```
#Installpipx
sudoaptinstallpipx
#Makeinstalledprogramsavailableonthecommandline
pipxensurepath
#InstallReticulum
pipxinstallrns
```

Alternatively, you can restore normal behaviour to `pip` by creating or editing the configuration file located at `~/. config/pip/pip.conf` , and adding the following section: 

```
[global]
break-system-packages=true
```

For a one-shot installation of Reticulum, without globally enabling the `break-system-packages` option, you can use the following command: 

**2.12. Platform-Specific Install Notes** 

**17** 

**Reticulum Network Stack, Release 1.3.0** 

```
pipinstallrns--break-system-packages
```

## **Note** 

The `--break-system-packages` directive is a somewhat misleading choice of words. Setting it will of course not break any system packages, but will simply allow installing `pip` packages user- and system-wide. While this _could_ in rare cases lead to version conflicts, it does not generally pose any problems, especially not in the case of installing Reticulum. 

## **2.12.9 Windows** 

On Windows operating systems, the easiest way to install Reticulum is by using the `pip` package manager from the command line (either the command prompt or Windows Powershell). 

If you don’t already have Python installed, download and install Python. At the time of publication of this manual, the recommended version is Python 3.12.7. 

**Important!** When asked by the installer, make sure to add the Python program to your PATH environment variables. If you don’t do this, you will not be able to use the `pip` installer, or run the included Reticulum utility programs (such as `rnsd` and `rnstatus` ) from the command line. 

After installing Python, open the command prompt or Windows Powershell, and type: 

## `pip install rns` 

You can now use Reticulum and all included utility programs directly from your preferred command line interface. 

## **2.13 Pure-Python Reticulum** 

## **Warning** 

If you use the `rnspure` package to run Reticulum on systems that do not support PyCA/cryptography, it is important that you read and understand the _Cryptographic Primitives_ section of this manual. 

In some rare cases, and on more obscure system types, it is not possible to install one or more dependencies. In such situations, you can use the `rnspure` package instead of the `rns` package, or use `pip` with the `--no-dependencies` command-line option. The `rnspure` package requires no external dependencies for installation. Please note that the actual contents of the `rns` and `rnspure` packages are _completely identical_ . The only difference is that the `rnspure` package lists no dependencies required for installation. 

No matter how Reticulum is installed and started, it will load external dependencies only if they are _needed_ and _available_ . If for example you want to use Reticulum on a system that cannot support `pyserial` , it is perfectly possible to do so using the _rnspure_ package, but Reticulum will not be able to use serial-based interfaces. All other available modules will still be loaded when needed. 

**Chapter 2. Getting Started Fast** 

**18** 

**CHAPTER THREE** 

## **ZEN OF RETICULUM** 

## **3.1 The Illusion Of The Center** 

For the better part of a generation, we have been taught to visualize the digital world through the lens of hierarchy. The mental maps we carry are dominated by a single, misleading image: **The Cloud** . 

We imagine the network as a vast, ethereal space “up there” or “out there”. A centralized repository of services and data to which we, the lowly clients, must connect. We build our software with this assumption hardcoded into our logic: _There is a server. The server has the authority. The server knows the way. I must find the server to function_ . 

This is the Client-Server mental model, and it is the primary obstacle to understanding Reticulum. 

## **3.1.1 Fallacy Of The Cloud** 

The first step in the Zen of Reticulum is to realize that _there is no cloud_ . There is only other people’s computers. When you build for the cloud, you are building _for_ a landlord. You are accepting that your application’s existence is conditional on the permission, uptime, and continued goodwill of a central authority. 

In Reticulum, you must shift your thinking from “connecting to” to “being among”. Reticulum is not a service you subscribe to - _it is a fabric you inhabit_ . There is no “up there”. There is only _here_ and _there_ , and the space between them is peer-to-peer. 

## **3.1.2 Decentralization Or Uncentralizability?** 

It is common to hear the word “decentralized” thrown around in modern tech circles. But often, this is merely a marketing term for “slightly distributed centralization”. A blockchain with a few dominant miners, or a federated protocol with a few giant servers. _In practice_ , it’s still centralized. It simply has a few centers instead of one. 

Reticulum goes further. It wants **Uncentralizability** . 

This is not a wishful political stance, but a foundational mathematical characteristic of the protocol, onto which everything else has been built. Reticulum assumes that every peer on the network is potentially hostile, and every link is potentially compromised. It is designed with no “privileged” nodes. While some nodes may act as Transport Instances - forwarding traffic for others - they do so _blindly_ , and they only know about their immediate surroundings, and nothing more. They route based on cryptographic proofs, not on administrative privilege. They cannot see who is talking to whom, nor can they selectively manipulate traffic without breaking their own ability to route entirely. 

The system is designed to make hierarchy structurally impossible. You cannot hijack an address, because there is no central registry to hijack. You cannot block a user, because there is no central switch to flip. You can offer paths through the network, but you can’t force anyone to use them. 

**19** 

**Reticulum Network Stack, Release 1.3.0** 

## **3.1.3 Death To The Address** 

To break free of the center, you must also let go of the concept of the “Address”. 

In the IP world, an address is a location. It is a coordinate in a _deeply hierarchical_ and static grid. If you move your computer to a different house, your address changes. If your router reboots, your address might change. Your _identity_ is bound to your _location_ , and therefore, it is fragile, and easily controlled. 

Reticulum abolishes this link between _Identity_ and _Location_ . 

In Reticulum, an address is not a place; it is a **Hash of an Identity** . It is a cryptographic representation of _who_ you are, not _where_ you are. Because of this, your address is portable. You can take a laptop from a WiFi cafe in Berlin, to a LoRa mesh in the mountains, to a packet radio link on a boat, and your “address” - your _Destination Hash_ - never changes. 

The network does not route to a place; it routes to a _person_ (or a machine). When you send a packet, you are not targeting a coordinate in a grid; you are encrypting a message for a specific entity. The network dynamically discovers where that entity currently resides, and it does so in a way where no one really knows where that entity is actually located physically. 

## **Consider:** 

- **The Old Way:** _“I am at_ `192.168.1.5` . _Come find me”_ . 

- **The Zen Way:** _“I am_ `<327c1b2f87c9353e01769b01090b18f2>` . _Wherever I am, my peers can reach me”_ . 

Once you stop thinking about servers and start thinking about portable identities, where everyone can always reach everyone else directly, the illusion of the center fades away. You realize there _is_ no center holding the network together. No coordinators or bureaucrats required. The network is simply the sum of its peers, communicating directly, sovereignly, and without a master. 

## **3.2 Physics Of Trust** 

_Paranoia Is A Great Design Principle_ 

If we accept that there is no center - that the network is a chaotic, peer-to-peer mesh - we are forced to confront a terrifying reality: **There is no one guarding the door** . 

In the traditional networking mindset, we rely on the concept of the “trusted core”. We assume our local coffee shop WiFi is safe, or that the backbone providers are neutral custodians. We build our security like a castle: strong walls on the outside, soft and trusting on the inside. We use encryption only when we step out into the “wild” internet. 

## **3.2.1 Hostile Environments** 

The Zen of Reticulum requires you to invert this. You must assume that _every_ environment is hostile. This isn’t cynicism, just uncaring physics. 

When you transmit information over radio waves, you are shouting into a crowded room. Anyone can listen. When you traverse the internet, your packets pass through routers controlled by strangers, corporations, and state actors. Assuming privacy in this environment without cryptographic protection is not optimism but gross negligence. 

Reticulum is built on the premise that every link is tapped, and every peer is a potential adversary. If your system cannot survive an adversary owning the physical layer, it cannot survive at all. 

But this is the paradox: By assuming the network is hostile, you make it safe. When you accept the dangers for what they are, they become manageable. When you stop trusting the infrastructure and start trusting the math, you eliminate the single point of failure: Human integrity. 

**Chapter 3. Zen of Reticulum** 

**20** 

**Reticulum Network Stack, Release 1.3.0** 

## **3.2.2 Encryption Is Not A Feature** 

In the world of TCP/IP, encryption is an afterthought. It is a layer we slap on top of the protocol (HTTPS, TLS) to patch the security holes of the original design. It is a “feature” you sometimes _enable_ for “sensitive data”. This is fundamentally flawed, since all data is sensitive. 

## In Reticulum, encryption is **gravity** . 

It is not optional. It is not a plugin. It is the _fundamental force that allows the network to exist_ . If you were to strip the encryption from Reticulum, the routing would break. The Transport system uses cryptographic signatures and entropy to verify paths and pass information. If packets were plaintext, intermediate nodes could not prove that a route was valid, nor could endpoints prevent spoofing or tampering. 

## In Reticulum, the entropy of the encrypted packet _is_ the routing logic. 

To ask for a version of Reticulum without encryption is like asking for a version of the ocean without liquid. You are not asking for a feature change; you’re asking for a different physical universe. We design for a universe where information has mass, structure, and integrity. 

## **3.2.3 Zero-Trust Architectures** 

## We must unlearn our reliance on **Institutional Trust** . 

For decades, we have been trained to trust authorities. We trust a website because a chain of Certificate Authorities (companies we don’t know) vouches for it. We trust an app because it is in an app store (run by a corporation we don’t control). We trust a message because it comes from a phone number assigned by a telecom. Yet, everything in our digital information sphere today is more untrustworthy and risky than a medieval second-hand underwear market. 

## Reticulum replaces institutional trust with **Cryptographic Proof** . 

In Reticulum, you do not trust a node because it has a nice hostname or because it is listed in a directory. You trust it because it holds the private key corresponding to the Destination Hash you are communicating with. This trust is binary, mathematical, and **absolute** . Either the signature matches, or it does not. There is no “maybe”. 

This shift moves the power from the institution to the individual. You become the ultimate arbiter of your own trust relationships. You decide which keys to accept, which paths to follow, and which identities to recognize. 

## **Consider:** 

- **The Old Way:** _“I trust this site because the browser says the lock icon is green”_ . 

- **The Zen Way:** _“I trust this destination because I have verified its hash fingerprint out-of-band, and the math confirms the signature”_ . 

When you internalize the Physics of Trust, you stop looking for protection from firewalls, VPNs, and Terms of Service agreements. You realize that true security comes from the design of the protocol itself. You can stop trusting the cloud, and you start trusting the code - because you can verify it yourself. 

## **3.3 Merits Of Scarcity** 

## _Every Bit Counts_ 

We have grown addicted to abundance. In the modern digital ecosystem, bandwidth is treated as an endless, flat ocean. We stream high-definition video without a thought, we ship entire libraries of code just to render a single button, and we measure performance in gigabits per second. This abundance has hollowed out our craft. When constraints vanish, efficiency dies, and with it, a certain kind of Clarity and Quality. 

Reticulum asks you to step out of the ocean and onto the tightrope. 

**3.3. Merits Of Scarcity** 

**21** 

**Reticulum Network Stack, Release 1.3.0** 

## **3.3.1 The Bandwidth Fallacy** 

The Zen of Reticulum requires the realization that **5 bits per second is a valid speed** . 

To a modern developer, this sounds like paralysis. But there is a profound freedom in limits: When you have a gigabit connection, you can be incredibly sloppy. You can be wasteful. You can push your problems onto the infrastructure. _“It’s slow? Get a faster router”_ . 

But on a high-latency, low-bandwidth link (be it a noisy HF radio channel or a tenuous LoRa hop) you cannot push problems anywhere. You must solve them. The network does not negotiate with waste. 

This forces a shift from consumption to interaction. You are no longer, then, consuming a service provided by a fat pipe; you are engaging in a careful negotiation with the physical medium. The medium becomes a partner in the conversation, not just a dumb conduit. You suddenly need to _understand the world to be in it_ . 

## **3.3.2 Cost Of A Byte** 

In a scarce economy, a byte is not just data, but energy, time, and space. 

Every byte you transmit consumes battery life on a solar-powered node. It occupies valuable airtime that could have been used by another peer. It represents a measurable slice of the electromagnetic spectrum. 

When you internalize this, you begin to write code differently. You stop asking, “How much data can I send?” and start asking, “What is the _minimum_ amount of information required to convey this intent? How can I best utilize my informational entropy?” 

This is where the elegance of Reticulum shines. The protocol is designed to strip away the non-essential. A link establishment takes three very small packets. A destination hash fits in 16 bytes. The overhead is vanishingly small, leaving almost the entire channel for the message itself. 

## **Consider:** 

- **The Old Way:** _“I need to send a status update. I’ll send a JSON object with metadata, timestamps, and user profile info (15KB).”_ 

- **The Zen Way:** _“I need to send a status update. I’ll send a single byte representing the state code. The context is already known.”_ 

This is of course optimization, but more importantly, _it is a form of respect_ . Efficiency in a shared medium is an act of stewardship. By taking only what you need from the network, you leave room for others. The network listens to those who speak with purpose. 

## **3.3.3 Flow & Time** 

Scarcity also teaches us about time. We have become addicted to the _synchronous_ now - the instant ping, the real-time stream. But Reticulum embraces _asynchronous_ time. 

When links are intermittent and latency is measured in minutes or hours, “real-time” is an illusion. Reticulum doesn’t encourage **Store and Forward** as a mere fallback, but as a primary mode of existence. You write a message, it propagates when it can, and it arrives when it arrives. 

This changes the psychological texture of communication. It removes the anxiety of the immediate response. It allows for contemplation. You are not demanding the recipient’s attention _right now_ ; you are placing a gift in their path, to be found when they are ready. 

By designing for delay, you design for resilience. You are no longer building a house of cards that collapses when a single packet drops. You are building a stone arch that distributes the load _over time_ . 

**Chapter 3. Zen of Reticulum** 

**22** 

**Reticulum Network Stack, Release 1.3.0** 

## **3.3.4 Liberation From Limits** 

There is a strange optimism in scarcity. When you are forced to work within strict constraints, you are forced to prioritize. _You_ must decide what truly matters. _That_ is the real core of agency. 

In the infinite fantasy world of The Cloud, everything is urgent, so nothing is. In the economy of Reticulum, the cost of transmission forces you to weigh the value of your message. Do you really need to send that heart beat? Is that photo essential? 

When you strip away the noise, what remains is _signal_ . 

This discipline creates a different kind of developer. It creates a craftsman who understands that the best code is the code you don’t have to write. It creates a user who understands that the most powerful message is the one that is _understood_ , not the one that is loudest. In the world of Reticulum, you are not a mere consumer of bandwidth; you are an architect of intent. 

## **3.4 Sovereignty Through Infrastructure** 

## **Be Your Own Network** 

We live in an era of digital tenancy. We lease our connectivity from ISPs. We rent our storage from cloud providers. We even borrow our identity from social media platforms. We are tenants in a house we did not build, governed by rules we did not write, subject to eviction at the whim of a landlord who has never met us. 

The Zen of Reticulum is the realization that you _can_ own the house. 

## **3.4.1 A Carrier-Grade Fallacy** 

For decades, we have been gaslit into believing that networking is really not just hard, but impossible. It is presented as a dark art reserved for telcos and billionaires, requiring millions of dollars of fiber optics, climate-controlled data centers, and armies of engineers. We are told that building reliable infrastructure is “too complex” for the individual or small organization. 

This is a big, fat lie. 

Physics is simple. A radio wave needs a transmitter and a receiver. A packet needs a path. The “complexity” of the modern internet is largely bureaucratic - a mountain of billing systems, regulatory capture, and legacy cruft designed to keep the gatekeepers in power. 

Reticulum strips away the bureaucracy. It runs on hardware that costs the price of a dinner. It runs on spectrum that is free to use. It demonstrates that a robust, planetary-scale network does not require a Fortune 500 company. It requires only the will to deploy, and the distributed, uncoordinated efforts of many individuals. 

## **3.4.2 Personal Infrastructure** 

This is where the rubber meets the road. You can read about Reticulum, you can understand the theory, but the insights only arrive when you plug in a radio and run a Transport Node. Suddenly, you are no longer a consumer. You’re an operator. 

This shift is subtle but profound. When you run your own infrastructure, the network ceases to be a service that is provided _to_ you. It becomes a space that you _inhabit_ . You become responsible for the flow of information. You gain an intimate understanding of the medium - the way the weather affects the radio waves, the way the topology changes, the way the packets dance through the ether. 

There is a quiet competence that comes from this. You stop asking “Is the internet down?” and start asking “Is _my_ links up?” You stop waiting for a technician and start checking the logs. This is a form of strength. To understand the system that carries your words is to be free from the mystery that keeps you dependent. 

**3.4. Sovereignty Through Infrastructure** 

**23** 

**Reticulum Network Stack, Release 1.3.0** 

## **3.4.3 The Ability To Disconnect** 

Why go to the trouble? Why buy the radio, write the config, and leave the Pi running in the corner? 

Because the old, centralized network is fragile. And because most of us doesn’t even really want to be there anymore. 

The internet we rely on today is a chain of single points of failure. Cut the undersea cable, and a continent goes dark. Shut down the power grid, and the cloud evaporates. Deprioritize the “wrong” traffic, and the flow of information is strangled. 

Sovereignty is the ability to survive the cut, whether or not that cut was an accident or on purpose. 

When you build your own infrastructure, you build a lifeline. Reticulum is designed to function over media that the traditional internet cannot touch - bare wires, battery-powered radios, ad-hoc WiFi meshes. When the grid fails, or the censors arrive, or the bill goes unpaid, your Reticulum network continues to hum. 

This is not about “dropping out” of society. It is about building a substrate on which an actual _Society_ can function. 

## **Consider:** 

- **The Old Way:** _“My connection is slow. I should call my ISP and complain.”_ 

- **The Zen Way:** _“The path is noisy. I will adjust the antenna or find a better route.”_ 

By taking ownership of the infrastructure, you take ownership of your voice. You stop shouting into someone else’s megaphone and start building your own. The network is no longer something that happens to you; it is something you make happen. 

## **3.5 Identity and Nomadism** 

## **A Fluid Self** 

In the old world, you are defined by your coordinates. If you are at `34.109.71.5` , you’re _here_ . If you unplug the cable and walk down the street, you vanish. Your digital self evaporates because it was tethered to the wall. You are a ghost in the endless machinations of gears, levers and transistors, bound to the hardware, and those that own it. 

This creates a subtle, constant anxiety. We are terrified of disconnecting because, in the architecture of the old web, disconnecting is a kind of death. 

The Zen of Reticulum offers a different way to be. 

## **3.5.1 Portable Existence** 

In Reticulum, your identity is not a location, or a username granted by a service. It is a cryptographic key - a complex, unique mathematical signature that exists independently of the physical world. You can carry it only in your mind, if you want to. 

Think of it less like a street address and more like a name. _A true name_ . 

If you travel from Berlin to Tokyo, you do not change your name. You are still you. The people who know you can still recognize you. Reticulum applies this principle to the network layer. Your Destination Hash is **invariant** . It travels with you, stored securely on your device, _immutable as a stone_ . 

This changes the relationship between you and the machine. You are not “logged into” the network via a specific gateway. You _are_ the endpoint. The network does not connect to a place; _it converges on you_ . 

## **3.5.2 Roaming Nodes** 

This freedom introduces a new concept of time and space: **Nomadism** . 

Because your identity is portable, your connectivity can be fluid. You can be sitting at a desk connected to a fiber backbone one moment, and walking through a field connected only to a long-range LoRa mesh the next. To the rest of 

**Chapter 3. Zen of Reticulum** 

**24** 

**Reticulum Network Stack, Release 1.3.0** 

the network, nothing has changed. Your friends do not need to update your contact info. The messages they send do not bounce back. The network senses the shift in the medium and reroutes the flow of data automatically. 

You are no longer a stationary node in a fixed grid. You are a wanderer in a fluid medium. 

The interfaces - whether it is WiFi, Ethernet, Packet Radio, or a physical wire - is merely the clothing your node wears. You change it to suit the environment. Underneath, you remain the same. This is the liberation of the protocol. It treats the physical medium as a transient circumstance, not a definition of self. 

## **Consider:** 

- **The Old Way:** _“I lost connection. I have to reconnect to the VPN to tell them where I am now.”_ 

- **The Zen Way:** _“I moved. The network subtly bends to accomodate this new reality.”_ 

## **3.5.3 Announcing Presence** 

How does the network find a wanderer? It listens. 

In the IP world, we query directories. We ask a server, “Where is Mark?” The server checks its database and gives us a coordinate. This means that someone, somewhere, is keeping track of you. It assumes and _requires_ surveillance. 

Reticulum replaces surveillance with **Announces** . 

Instead of asking a central authority where you are, you simply state your presence. You broadcast a cryptographic proof: “I am here, and I am who I say I am”. This ripples out through the mesh. Your neighbors hear it, update their path tables, and pass it on. 

This is a quiet, organic process. It is the digital equivalent of lighting lanterns in the dark. You do not need to chase the light; you let the light find you. It respects your autonomy. You choose when to announce, how often to speak, and to whom. You also choose when to disappear - for but a moment or perpetually. 

## **3.5.4 Anchor In The Flow** 

There is a deep peace in this nomadism. It teaches you that stability does not come from standing still. Stability comes from _internal coherence_ . 

By holding your own private key, you hold your own center of gravity. The world around you; the infrastructure, the topography and the availability of links can all shift chaotically. Storms can knock out towers. Cables can be cut. The internet can go down. 

But as long as you possess your key, you possess your identity. The entire infrastructure can be destroyed and rebuilt, and you are still you. Nothing lasts, yet nothing is lost. 

You become a sovereign entity moving through the noise, connected not by the rigidity of cables, but by the fluidity of recognition. The network becomes a place you inhabit, rather than a utility you subscribe to: You are at home in the ether. 

## **3.6 Ethics Of The Tool** 

## **Technology With Conscience** 

You have unlearned the center. You have accepted the physics of trust. You have embraced the economy of scarcity and the freedom of unbound nomadism. You are standing in a new space. Now, look at the tool in your hand. 

In the old world, we were taught that technology is neutral. We are told that “guns don’t kill people, people do”, or that a component is just a component, indifferent to what its combinatorial potential is. This is a convenient lie. It serves only to allow the builders to wash their hands of responsibility. 

But we know better now. We know that **architecture is politics** , and _politics is control_ . The way you build a system determines how it will be used. If you build a system optimized for mass surveillance, you _will_ get a panopticon. If 

**3.6. Ethics Of The Tool** 

**25** 

**Reticulum Network Stack, Release 1.3.0** 

you build a system optimized for centralized control, you _will_ get a dictatorship. If you build a system optimized for extraction, you _will_ get a parasite. 

The Zen of Reticulum asserts that a tool is never neutral. 

On the very contrary: A tool is intent, **crystallized** . 

## **3.6.1 The Harm Principle** 

Why does the Reticulum License forbid the software from being used in systems designed to harm humans? Is it not just a restriction on freedom? 

It is a restriction on _license_ , yes, but it is an expansion of _freedom_ . 

Building powerful tools without a moral compass is in no way virtuous or commendable, it is plain and simple irresponsibility. 

A tool that can easily be used to oppress is a real danger to the user. If you build a network that can be turned against you by a tyrant, you are not free. You are merely waiting for the leash to tighten. By encoding the “Harm Principle” into the legal DNA of the reference implementation, we are building a safeguard. We are stating, clearly and immutably, that _this tool_ is for **life** , not for death. 

This aligns the software with the interests of humanity. It cements that the network cannot be conscripted into a killsystem, a weaponized drone controller, or a torture device without breaking the license and the law. It is a line drawn in the sand - not by a government or external authority, but by the creators of the tool itself. 

## **Consider:** 

- **The Old Way:** _“It’s just software. How people use it is not my problem.”_ 

- **The Zen Way:** _“This software is a habitat. I will not allow it to be used to build a cage.”_ 

It is _your_ choice whether to align with this - we are not forcing this stance on anyone. If you choose to align with life over death, with creativity over destruction, we grant you an immensely powerful tool, to own and build with as you please. If you do not, we deny it. 

If you do not like this, we most assuredly do not need you here, and you are on your own. 

## **3.6.2 Public Domain Protocol** 

This leads to a vital distinction: The difference between the _idea_ and the _implementation_ . 

The protocol - the mathematical rules of how Reticulum works - is dedicated to the Public Domain. It belongs to humanity. **No one can own it** . Anyone can implement it, improve it, or adapt it. This is the core idea of free communication, which itself must be forever free. 

But the functional, deployed _reference implementation_ - the Python code, the maintenance, the years of labor - has a conscience. This distinction is the engine of sustainability. It allows the protocol to be universal, while ensuring that the specific labor of the builders is not hijacked to undermine the foundational intent of the project itself. From this document, it should be very clear what this intent is. 

If you want to build a system with Reticulum that manipulates and damages users for profits or targets missiles, you can use the public domain protocol, and start from scratch. But you cannot take our work. You must do your own. This serves as a pillar of accountability. If you want to build a weapon, _you_ go and forge the steel yourself, while the world observes. And when the blood is drawn - it is on **your** hands. 

## **3.6.3 Preserving Human Agency** 

We live in an era of predatory extraction. The open-source commons is being scraped, ingested, and regurgitated by machine learning algorithms, whose corporate owners seek to replace the very humans who built those commons. Our 

**Chapter 3. Zen of Reticulum** 

**26** 

**Reticulum Network Stack, Release 1.3.0** 

code, our words, and our creativity is being used to train systems that are specifically designed to make us obsolete, without offering anything else in return than serfdom and leashes. 

Reticulum stands against this. 

The license protects the software from being used to feed the beast. It draws a hard line: This tool is for _people_ . It is for human-to-human connection. It is not a dataset to be strip-mined for the purpose of building a synthetic overlord, puppeteered by a miniscule conglomerate of controllers. 

This is a radical act of preservation. By protecting the code from AI appropriation, we are protecting space for human agency. We are ensuring that there remains a digital realm where the actors are flesh, blood and soul, where decisions are made by minds, not overlords hiding behind models. 

When you use Reticulum, you are using a tool that respects you. It does not see you as a product to be tracked. It does not see your data as fuel for an algorithm. It sees you as a sovereign, equal peer. 

This changes the foundational premise of using the technology. It restores dignity to the interaction. You are not the user of a service; you are a participant in a mutual covenant. The tool aligns with your autonomy, rather than eroding it. 

In this way, ethics is not a restriction, but a foundation. It is the foundation that helps ensure the network will still belong to you tomorrow. 

## **3.7 Design Patterns For Post-IP Systems** 

## **Practical Philosophy for Developers** 

The philosophy is useless if it cannot be hammered into code. The metaphors we have explored - nomadism, scarcity, trust - are not just poetry, but real-world engineering constraints. When you sit down to write software for Reticulum, these concepts must shape the very structure of your application. 

We are now moving from the _why_ to the _how_ . This is where the abstract becomes concrete, and where you will see the true depth of the patterns we have been weaving. 

## **3.7.1 Store & Forward** 

The web has trained us to be impatient. We write synchronous code. We fire a request and we wait, blocking the UI, holding our breath. If the response doesn’t come in 250 milliseconds, we show a spinner. If it doesn’t come in five seconds, we show an error. We treat network connectivity as a binary state: either we are “online” or we are “broken”. 

This is brittle. It is a rejection of reality. 

In Reticulum, connectivity is a spectrum, and presence is asynchronous. If at all applicable to your intent, you must design your applications to embrace **Store & Forward** . 

Instead of demanding an immediate answer, your application should act as a patient participant. You create a message for someone or something in the mesh. The network holds it. It carries it from node to node, perhaps over hours or days, waiting for the recipient to appear. When they finally surface, the message is delivered. This requires a shift from “request/response” to “event/handler”. How exactly you do this is a challenge for you to solve intelligently within your problem domain, but Reticulum-based systems already exist that does this extremely well, and you can use them for inspiration. 

## **Consider:** 

- **The Old Way:** `Connect() -> Send() -> Wait() -> Crash if timeout.` 

- **The Zen Way:** `Send() -> Continue living. -> Receive() when it arrives.` 

This changes the user experience profoundly. It removes the anxiety of the loading bar. It creates a sense of continuity. The user is not “waiting for the network”; they are interacting with a persistent log of communication that lives in the network itself. 

**3.7. Design Patterns For Post-IP Systems** 

**27** 

**Reticulum Network Stack, Release 1.3.0** 

## **3.7.2 Naming Is Power** 

In the IP world, we are slaves to the Domain Name System. We rely on a hierarchy of registrars to map human-readable names to machine-readable addresses. This hierarchy is a choke point. If the registrar revokes your domain, or if the DNS server goes down, you vanish. 

Reticulum dissolves this hierarchy with **Hash-based Identity** . 

In this design pattern, a name is not a string you look up; it is a cryptographic destination you verify. When you design for Reticulum, you stop asking the user for a URL and start asking for a Destination or Identity Hash. 

This feels strange at first. A hash like `<83b7328926fed0d2e6a10a7671f9e237>` looks alien compared to `myfriend. com` . But that alienness is the armor. It **cannot** be spoofed. It **cannot** be censored by a registrar. It is **absolute** . 

Designing for this means shifting your UI metaphors. You are no longer browsing a web of pages; you are managing a ledger of keys. You are building an “Address Book” that is actually a keyring. The names are given by the user, and the power stays with them. That hashes look complex is directly analogous to the strengths of the bonds formed by their use. It forces the user to engage in a moment of verification, an out-of-band handshake, which restores the human element of trust that SSL certificates stripped away. 

## **3.7.3 The Interface Is The Medium** 

One of the most liberating patterns in Reticulum is **Transport Agnosticism** . 

In traditional networking, your code is often littered with transport logic. “Am I on WiFi? Check bandwidth. Am I on Cellular? Check data plan. Am I on Ethernet?”. You are constantly micromanaging the pipe. 

In Reticulum, you write to the API, and the API writes to the medium. You send a packet to a Destination. You do not care if that packet travels over a TCP tunnel, a LoRa radio wave, or a serial wire interface. That is the stack’s concern. 

This allows you to write **Universal Applications** . Imagine a messaging app. You write it once. It works on a laptop connected to fiber. It works on a phone in the city using WiFi. And, without a single line of code changed, it works on a device in the wilderness, talking only to other devices via radio. 

The pattern is simple: **Never code to the hardware. Code to the intent.** 

## **Consider:** 

- **The Old Way:** `socket.connect(ip, port)` , and then a whole lot more 

- **The Zen Way:** `RNS.Packet(destination, data).send()` 

By abstracting the medium, you make your software immortal to changes in infrastructure. The user might switch from a 4G hotspot to a HF modem tomorrow. Your software doesn’t need to know. It simply continues the conversation. 

## **3.7.4 Emergent Patterns** 

When you combine these patterns - _Store & Forward_ , _Hash-based Identity_ , and _Transport Agnosticism_ - you create software that feels fundamentally different. 

It feels _grounded_ . It doesn’t flicker when the signal drops. It doesn’t panic when the server is down. It has weight. It has persistence. It has _relevance_ . 

You are no longer building a “client” that begs a “server” for attention. You are building an autonomous agent that exists within the mesh. It speaks when it needs to, listens when it can, and carries its identity with it wherever it goes. 

This is the culmination of the Zen. The code is not just a set of instructions: It is a behavioral envelope. It is a way of _being_ in the network. 

**Chapter 3. Zen of Reticulum** 

**28** 

**Reticulum Network Stack, Release 1.3.0** 

## **3.8 Fabric Of The Independent** 

We have stripped away the illusions. We have seen that the center is empty, that trust _must_ be hard, that resources are finite, and that we must own our infrastructure. We have seen that tools have ethics and that our identity can move fluidly. 

This is a reclaiming of the commons. For too long, we have allowed the most vital substrate of human society - _our ability to speak to one another_ - to be colonized by entities that do not share our interests. We have allowed the architecture of our communication to be designed by accountants rather than architects. 

We are taking it back. Not by petitioning the masters, but by building the new world within, over, under and around the shell of the old. 

## **3.8.1 The Work Is Finished** 

The heavy lifting is done. 

The protocol is in the public domain, a gift to humanity that can never be taken away. The software is written, tested, and running on devices scattered across the globe. The manual lies open before you. The source code for the reference implementation is now distributed on hundreds of thousands of devices across the planet. No one can delete or destroy it. The hardware is accessible and abundant. 

It was a hard road to get here, but we got here. Now, there is no roadmap committee waiting for approval. There is no venture capital dictating the user experience. There is no CEO to sign off on the next feature release. 

There is only you. 

The barrier to entry is no longer complexity: It is the mere habit of dependency. You were conditioned to wait. Wait for the app update. Wait for the ISP to fix the line. Wait for the platform to allow the post. Wait for the government to change the policies. Wait for the likes. Wait for the revolution to be televised. 

The revolution never was televised. 

It is packetized. 

## **3.8.2 Open Sky** 

The future of this technology is a construction project. 

It looks like a single node on a windowsill, listening to the static. It looks like a message sent to a neighbor, bypassing the noise of the commercial web. It looks like a community mesh that grows, link by link, hop by hop, carried by hands that care more about connection than profit. 

You have the blueprints. You have the tools. You have the philosophy. The noise of the old world has fallen away, leaving you with the quiet clarity of the open spectrum. 

_Mark, early 2026_ 

**3.8. Fabric Of The Independent** 

**29** 

**Reticulum Network Stack, Release 1.3.0** 

**Chapter 3. Zen of Reticulum** 

**30** 

**CHAPTER FOUR** 

## **PROGRAMS USING RETICULUM** 

This chapter provides a non-exhaustive list of notable programs, systems and application-layer protocols that have been built using Reticulum. 

These programs will let you get a feel for how Reticulum works. Most of them have been designed to run well even over slow networks based on LoRa or packet radio, but all can also be used over fast links, such as local WiFi, wired Ethernet, the Internet, or any combination. 

As such, it is easy to get started experimenting, without having to set up any radio transceivers or infrastructure just to try it out. Launching the programs on separate devices connected to the same WiFi network is enough to get started, and physical radio interfaces can then be added later. 

## **4.1 Programs & Utilities** 

Many different applications using Reticulum already exist, serving a wide variety of purposes from day-to-day communication and information sharing to systems administration and tackling advanced networking and communications challenges. 

Development of Reticulum-based applications and systems is ongoing, so consider this list a non-exhaustive starting point of _some_ of the options available. With a bit of searching, primarily over Reticulum itself, you will find many more interesting things. 

## **4.1.1 Remote Shell** 

The rnsh program lets you establish fully interactive remote shell sessions over Reticulum. It also allows you to pipe any program to or from a remote system, and is similar to how `ssh` works. The `rnsh` program is very efficient, and can facilitate fully interactive shell sessions, even over extremely low-bandwidth links, such as LoRa or packet radio. 

In addition to the default, fully interactive terminal mode, for extremely limited links, `rnsh` offers line-interactive mode, allowing you to interact with remote systems, even when link throughput is counted in a few hundreds of bits per second. 

**31** 

**Reticulum Network Stack, Release 1.3.0** 

## **4.1.2 Nomad Network** 

The terminal-based program Nomad Network provides a complete encrypted communications suite built with Reticulum. It features encrypted messaging (both direct and delayed-delivery for offline users), file sharing, and has a built-in text-browser and page server with support for dynamically rendered pages, user authentication and more. 

**==> picture [468 x 264] intentionally omitted <==**

Nomad Network is a user-facing client for the messaging and information-sharing protocol LXMF. 

## **4.1.3 RNS Page Node** 

RNS Page Node is a simple way to serve pages and files to any other Nomad Network compatible client. Drop-in replacement for NomadNet nodes that primarily serve pages and files. 

## **4.1.4 Retipedia** 

You can host the entirity of Wikipedia (or any `.zim` ) file to other Nomad Network clients using Retipedia. 

**Chapter 4. Programs Using Reticulum** 

**32** 

**Reticulum Network Stack, Release 1.3.0** 

## **4.1.5 Sideband** 

If you would rather use an LXMF client with a graphical user interface, you can take a look at Sideband, which is available for Android, Linux, macOS and Windows. Sideband is an advanced LXMF and LXST client, and a multipurpose Reticulum utility, with features and functionality targeted at advanced users. 

**==> picture [468 x 317] intentionally omitted <==**

Sideband allows you to communicate with other people or LXMF-compatible systems over Reticulum networks using LoRa, Packet Radio, WiFi, I2P, Encrypted QR Paper Messages, or anything else Reticulum supports. 

It also interoperates with all other LXMF clients, and provides advanced features such as voice messaging, real-time voice calls, file attachments, private telemetry sharing, and a full plugin system for expandability. 

**4.1. Programs & Utilities** 

**33** 

**Reticulum Network Stack, Release 1.3.0** 

## **4.1.6 MeshChatX** 

A Reticulum MeshChat fork from the future, with the goal of providing everything you need for Reticulum, LXMF, and LXST in one beautiful and feature-rich application. This project is separate from the original Reticulum MeshChat project, and is not affiliated with the original project, but is a much more up-to-date, comprehensive and well-maintained fork. 

**==> picture [468 x 239] intentionally omitted <==**

Features include full LXST support, custom voicemail, phonebook, contact sharing, and ringtone support, multiidentity handling, modern UI/UX, offline documentation, expanded tools, page archiving, integrated maps, telemetry and improved application security. 

**Chapter 4. Programs Using Reticulum** 

**34** 

**Reticulum Network Stack, Release 1.3.0** 

## **4.1.7 Reticulum Relay Chat** 

Reticulum Relay Chat is a live chat system built on top of the Reticulum Network Stack. It exists to let people talk to each other in real time over Reticulum without dragging in message databases, synchronization engines, or architectural commitments they did not ask for. 

The rrcd program provides a functional, reference RRC hub-server daemon implementation. RRC user clients include rrc-gui and rrc-web. 

RRC is closer in spirit to IRC than to modern “everything platforms.” You connect, you join a room, you talk, and then you leave. If you were present, you saw the conversation. If you were not, the conversation did not wait for you. This is not an accident. This is the entire design. 

## **4.1.8 RetiBBS** 

RetiBBS is a bulletin board system implementation for Reticulum networks. 

**==> picture [469 x 261] intentionally omitted <==**

RetiBBS allows users to communicate through message boards in a secure manner. 

**4.1. Programs & Utilities** 

**35** 

**Reticulum Network Stack, Release 1.3.0** 

## **4.1.9 RBrowser** 

The rBrowser program is a cross-platform, standalone, web-based browser for exploring NomadNetwork Nodes over Reticulum Network. It automatically discovers NomadNet nodes through network announces and provides a userfriendly interface for browsing distributed content with Micron markup support. 

**==> picture [468 x 264] intentionally omitted <==**

Includes useful features like automatic listening for announce, adding nodes to favorites, browsing and rendering any kind of NomadNet links, downloading files from remote nodes, a unique local NomadNet Search Engine and more. 

**Chapter 4. Programs Using Reticulum** 

**36** 

**Reticulum Network Stack, Release 1.3.0** 

## **4.1.10 Reticulum Network Telephone** 

The `rnphone` program, included as part of the LXST package is a command-line Reticulum telephone utility and daemon, that allows building physical, hardware telephones for LXST and Reticulum, as well as simply performing calls via the command line. 

**==> picture [468 x 264] intentionally omitted <==**

It supports interfacing directly with hardware peripherals such as GPIO keypads and LCD displays, providing a modular system for building secure hardware telephones. 

**4.1. Programs & Utilities** 

**37** 

**Reticulum Network Stack, Release 1.3.0** 

## **4.1.11 LXST Phone** 

The LXST Phone program is a cross-platform desktop application for performing LXST voice calls over Reticulum. 

**==> picture [468 x 429] intentionally omitted <==**

It supports various advanced features such as SAS verification, peer blocking, rate limiting, encrypted call history storage and contact management. 

**Chapter 4. Programs Using Reticulum** 

**38** 

**Reticulum Network Stack, Release 1.3.0** 

## **4.1.12 LXMFy** 

LXMFy is a comprehensive and advanced bot creation framework for LXMF, that allows building any kind of automation or bot system running over LXMF and Reticulum. Bot implementations exist for Home Assistant control, LLM integrations, and various other purposes. 

## **4.1.13 LXMF Interactive Client** 

LXMF Interactive Client is a feature-rich, terminal-based LXMF messaging client with many advanced features and an extensible plugin architecture. 

## **4.1.14 RNS FileSync** 

The RNS FileSync program enables automatic file synchronization between devices without requiring central servers, internet connectivity, or cloud services. It works over any network medium supported by Reticulum, including radio, LoRa, WiFi, or the internet, making it ideal for off-grid, privacy-focused, and resilient file sharing. 

## **4.1.15 Micron Parser JS** 

Micron Parser JS is the JavaScript-based parser for the Micron markup language, that most web-based Nomad Network browsers use. If you want to make utilities or tools that display Micron pages, this library is essential. 

## **4.1.16 RNMon** 

RNMon is a monitoring daemon designed to monitor the status of multiple RNS applications and push the metrics to an InfluxDB instance over the influx line protocol. 

**4.1. Programs & Utilities** 

**39** 

**Reticulum Network Stack, Release 1.3.0** 

## **4.2 Protocols** 

A number of standard protocols have emerged through real-world usage and testing in the Reticulum community. While you may sometimes want to use completely custom protocols and implementations when writing Reticulum-based software, using these protocols provides application developers with an easy way to implement advanced functionality quickly and effortlessly. Using them also ensures compatibility and interoperability between many different client applications, creating an open communications ecosystem where users are free to choose the applications that suit their needs, while remaining connected to everyone else. 

## **4.2.1 LXMF** 

LXMF is a simple and flexible messaging format and delivery protocol that allows a wide variety of applications, while using as little bandwidth as possible. It offers zero-conf message routing, end-to-end encryption and Forward Secrecy, and can be transported over any kind of medium that Reticulum supports. 

LXMF is efficient enough that it can deliver messages over extremely low-bandwidth systems such as packet radio or LoRa. Encrypted LXMF messages can also be encoded as QR-codes or text-based URIs, allowing completely analog paper message transport. 

Using Propagation Nodes, LXMF also offer a way to store and forward messages to users or endpoints that are not directly reachable at the time of message emission. 

## **4.2.2 LXST** 

LXST is a simple and flexible real-time streaming format and delivery protocol that allows a wide variety of applications, while using as little bandwidth as possible. It is built on top of Reticulum and offers zero-conf stream routing, end-to-end encryption and Forward Secrecy, and can be transported over any kind of medium that Reticulum supports. It currently powers real-time voice and telephony applications over Reticulum. 

## **4.2.3 RRC** 

The Reticulum Relay Chat protocol, is a live chat system built on top of the Reticulum Network Stack. It exists to provide near real-time group communication without dragging in message history databases, federation machinery, or architectural guilt. 

RRC is intentionally simple. It does not pretend to be email, a mailbox, or a distributed archive. It behaves more like a conversation in a room. If you were there, you heard it. If you were not, you did not. That is not a bug, that is the point. 

## **4.3 Interface Modules & Connectivity Resources** 

This section provides a list of various community-provided interface modules, guides and resources for creating Reticulum networks over special or challenging mediums. 

- Custom interface module for running RNS over HTTP 

- Guide for running Reticulum over ICMP using `PipeInterface` 

- Guide for running Reticulum over DNS with Iodine 

- Guide for running Reticulum over HF radio 

- Modem73 is a KISS TNC OFDM modem frontend that can be used with Reticulum 

**Chapter 4. Programs Using Reticulum** 

**40** 

**CHAPTER FIVE** 

## **USING RETICULUM ON YOUR SYSTEM** 

Reticulum is not installed as a driver or kernel module, as one might expect of a networking stack. Instead, Reticulum is distributed as a Python module, containing the networking core, and a set of utility and daemon programs. 

This means that no special privileges are required to install or use it. It is also very light-weight, and easy to transfer to, and install on new systems. 

When you have Reticulum installed, any program or application that uses Reticulum will automatically load and initialise Reticulum when it starts, if it is not already running. 

In many cases, this approach is sufficient. When any program needs to use Reticulum, it is loaded, initialised, interfaces are brought up, and the program can now communicate over any Reticulum networks available. If another program starts up and also wants access to the same Reticulum network, the already running instance is simply shared. This works for any number of programs running concurrently, and is very easy to use, but depending on your use case, there are other options. 

## **5.1 Configuration & Data** 

Reticulum stores all information that it needs to function in a single file-system directory. When Reticulum is started, it will look for a valid configuration directory in the following places: 

- `/etc/reticulum` 

- `~/.config/reticulum` 

- `~/.reticulum` 

If no existing configuration directory is found, the directory `~/.reticulum` is created, and the default configuration will be automatically created here. You can move it to one of the other locations if you wish. 

It is also possible to use completely arbitrary configuration directories by specifying the relevant command-line parameters when running Reticulum-based programs. You can also run multiple separate Reticulum instances on the same physical system, either in isolation from each other, or connected together. 

In most cases, a single physical system will only need to run one Reticulum instance. This can either be launched at boot, as a system service, or simply be brought up when a program needs it. In either case, any number of programs running on the same system will automatically share the same Reticulum instance, if the configuration allows for it, which it does by default. 

The entire configuration of Reticulum is found in the `~/.reticulum/config` file. When Reticulum is first started on a new system, a basic, but fully functional configuration file is created. The default configuration looks like this: 

```
#ThisisthedefaultReticulumconfigfile.
#Youshouldprobablyeditittoincludeanyadditional,
#interfacesandsettingsyoumightneed.
```

(continues on next page) 

**41** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
#Onlythemostbasicoptionsareincludedinthisdefault
#configuration.Toseeamoreverbose,andmuchlonger,
#configurationexample,youcanrunthecommand:
#rnsd--exampleconfig
```

## `[reticulum]` 

```
#IfyouenableTransport,yoursystemwillroutetraffic
#forotherpeers,passannouncesandservepathrequests.
#Thisshouldbedoneforsystemsthataresuitedtoact
#astransportnodes,ie.iftheyarestationaryand
#always-on.Thisdirectiveisoptionalandcanberemoved
#forbrevity.
```

## `enable_transport = No` 

```
#Bydefault,thefirstprogramtolaunchtheReticulum
#NetworkStackwillcreateasharedinstance,thatother
#programscancommunicatewith.Onlythesharedinstance
#opensalltheconfiguredinterfacesdirectly,andother
#localprogramscommunicatewiththesharedinstanceover
#alocalsocket.Thisiscompletelytransparenttothe
#user,andshouldgenerallybeturnedon.Thisdirective
#isoptionalandcanberemovedforbrevity.
```

## `share_instance = Yes` 

```
#Ifyouwanttorunmultiple*different*sharedinstances
#onthesamesystem,youwillneedtospecifydifferent
#instancenamesforeach.Onplatformssupportingdomain
#sockets,thiscanbedonewiththeinstance_nameoption:
```

## `instance_name = default` 

_`# Some platforms don` '_ _`t support domain sockets, and if that # is the case, you can isolate different instances by # specifying a unique set of ports for each:`_ 

```
#shared_instance_port=37428
#instance_control_port=37429
```

```
#IfyouwanttoexplicitlyuseTCPforsharedinstance
#communication,insteadofdomainsockets,thisisalso
#possible,byusingthefollowingoption:
#shared_instance_type=tcp
```

(continues on next page) 

**Chapter 5. Using Reticulum on Your System** 

**42** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
#Onsystemswhererunninginstancesmaynothaveaccess
#tothesamesharedReticulumconfigurationdirectory,
#itisstillpossibletoallowfullinteractivityfor
#runninginstances,bymanuallyspecifyingasharedRPC
#key.Inalmostallcases,thisoptionisnotneeded,but
#itcanbeusefulonoperatingsystemssuchasAndroid.
#Thekeymustbespecifiedasbytesinhexadecimal.
```

```
#rpc_key=e5c032d3ec4e64a6aca9927ba8ab73336780f6d71790
```

```
#ItispossibletoallowremotemanagementofReticulum
#systemsusingthevariousbuilt-inutilities,suchas
#rnstatusandrnpath.Youwillneedtospecifyoneor
#moreReticulumIdentityhashesforauthenticatingthe
#queriesfromclientprograms.Forthispurpose,youcan
#useexistingidentityfiles,orgeneratenewoneswith
#thernidutility.
```

_`# enable_remote_management = yes # remote_management_allowed = 9fb6d773498fb3feda407ed8ef2c3229,`_ `␣` _˓→_ _`2d882c5586e548d79b5af27bca1776dc`_ 

```
#YoucanconfigureReticulumtopanicandforciblyclose
#ifanunrecoverableinterfaceerroroccurs,suchasthe
#hardwaredeviceforaninterfacedisappearing.Thisis
#anoptionaldirective,andcanbeleftoutforbrevity.
#Thisbehaviourisdisabledbydefault.
```

```
#panic_on_interface_error=No
```

```
#WhenTransportisenabled,itispossibletoallowthe
#TransportInstancetorespondtoproberequestsfrom
#thernprobeutility.Thiscanbeausefultooltotest
#connectivity.Whenthisoptionisenabled,theprobe
#destinationwillbegeneratedfromtheIdentityofthe
#TransportInstance,andprintedtothelogatstartup.
#Optional,anddisabledbydefault.
```

```
#respond_to_probes=No
```

## `[logging]` 

```
#Validloglevelsare0through7:
#0:Logonlycriticalinformation
#1:Logerrorsandlowerloglevels
#2:Logwarningsandlowerloglevels
#3:Lognoticesandlowerloglevels
#4:Loginfoandlower(thisisthedefault)
#5:Verboselogging
```

(continues on next page) 

**5.1. Configuration & Data** 

**43** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
#6:Debuglogging
#7:Extremelogging
loglevel=4
```

```
#Theinterfacessectiondefinesthephysicalandvirtual
#interfacesReticulumwillusetocommunicateon.This
#sectionwillcontainexamplesforavarietyofinterface
#types.Youcanmodifytheseorusethemasabasisfor
#yourownconfig,orsimplyremovetheunusedones.
```

```
[interfaces]
```

```
#Thisinterfaceenablescommunicationwithother
#link-localReticulumnodesoverUDP.Itdoesnot
#needanyfunctionalIPinfrastructurelikerouters
#orDHCPservers,butwillrequirethatatleastlink-
#localIPv6isenabledinyouroperatingsystem,which
#shouldbeenabledbydefaultinalmostanyOS.See
#theReticulumManualformoreconfigurationoptions.
```

```
[[DefaultInterface]]
type=AutoInterface
interface_enabled=True
```

If Reticulum infrastructure already exists locally, you probably don’t need to change anything, and you may already be connected to a wider network. If not, you will probably need to add relevant _interfaces_ to the configuration, in order to communicate with other systems. 

You can generate a much more verbose configuration example by running the command: 

## `rnsd --exampleconfig` 

The output includes examples for most interface types supported by Reticulum, along with additional options and configuration parameters. 

It is a good idea to read the comments and explanations in the above default config. It will teach you the basic concepts you need to understand to configure your network. Once you have done that, take a look at the _Interfaces_ chapter of this manual. 

## **5.2 Included Utility Programs** 

Reticulum includes a range of useful utilities, both for managing your Reticulum networks, and for carrying out common tasks over Reticulum networks, such as transferring files to remote systems, and executing commands and programs remotely. 

If you often use Reticulum from several different programs, or simply want Reticulum to stay available all the time, for example if you are hosting a transport node, you might want to run Reticulum as a separate service that other programs, applications and services can utilise. 

**Chapter 5. Using Reticulum on Your System** 

**44** 

**Reticulum Network Stack, Release 1.3.0** 

## **5.2.1 The rnsd Utility** 

It is very easy to run Reticulum as a service. Simply run the included `rnsd` command. When `rnsd` is running, it will keep all configured interfaces open, handle transport if it is enabled, and allow any other programs to immediately utilise the Reticulum network it is configured for. 

You can even run multiple instances of `rnsd` with different configurations on the same system. 

## **Usage Examples** 

Run `rnsd` : 

```
$rnsd
```

```
[2023-08-1817:59:56][Notice]Startedrnsdversion0.5.8
```

Run `rnsd` in service mode, ensuring all logging output is sent directly to file: 

```
$rnsd-s
```

Generate a verbose and detailed configuration example, with explanations of all the various configuration options, and interface configuration examples: 

```
$rnsd--exampleconfig
```

## **All Command-Line Options** 

```
usage:rnsd.py[-h][--configCONFIG][-v][-q][-s][--exampleconfig][--version]
```

```
ReticulumNetworkStackDaemon
```

```
options:
-h,--helpshowthishelpmessageandexit
--configCONFIGpathtoalternativeReticulumconfigdirectory
-v,--verbose
-q,--quiet
-s,--servicernsdisrunningasaserviceandshouldlogtofile
-i,--interactivedropintointeractiveshellafterinitialisation
--exampleconfigprintverboseconfigurationexampletostdoutandexit
--versionshowprogram'sversionnumberandexit
```

You can easily add `rnsd` as an always-on service by _configuring a service_ . 

## **5.2.2 The rnstatus Utility** 

Using the `rnstatus` utility, you can view the status of configured Reticulum interfaces, similar to the `ifconfig` program. 

## **Usage Examples** 

Run `rnstatus` : 

```
$rnstatus
SharedInstance[37428]
Status:Up
Serving:1program
```

(continues on next page) 

**5.2. Included Utility Programs** 

**45** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
Rate:1.00Gbps
Traffic:83.13KB↑
86.10KB↓
AutoInterface[Local]
Status:Up
Mode:Full
Rate:10.00Mbps
Peers:1reachable
Traffic:63.23KB↑
80.17KB↓
TCPInterface[RNSTestnetDublin/dublin.connect.reticulum.network:4965]
Status:Up
Mode:Full
Rate:10.00Mbps
Traffic:187.27KB↑
74.17KB↓
RNodeInterface[RNodeUHF]
Status:Up
Mode:AccessPoint
Rate:1.30kbps
Access:64-bitIFACby<...e702c42ba8>
Traffic:8.49KB↑
9.23KB↓
ReticulumTransportInstance<5245a8efe1788c6a1cd36144a270e13b>running
```

Filter output to only show some interfaces: 

```
$rnstatusrnode
RNodeInterface[RNodeUHF]
Status:Up
Mode:AccessPoint
Rate:1.30kbps
Access:64-bitIFACby<...e702c42ba8>
Traffic:8.49KB↑
9.23KB↓
ReticulumTransportInstance<5245a8efe1788c6a1cd36144a270e13b>running
```

**All Command-Line Options** 

```
usage:rnstatus[-h][--configCONFIG][--version][-a][-A]
[-l][-t][-sSORT][-r][-j][-Rhash][-ipath]
[-wseconds][-d][-D][-m][-Iseconds][-v][filter]
ReticulumNetworkStackStatus
positionalarguments:
```

(continues on next page) 

**Chapter 5. Using Reticulum on Your System** 

**46** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

## `filter` 

```
onlydisplayinterfaceswithnamesincludingfilter
```

```
options:
```

- `-h, --help show this help message and exit --config CONFIG path to alternative Reticulum config directory --version show program's version number and exit -a, --all show all interfaces -A, --announce-stats show announce stats -l, --link-stats show link stats -t, --totals display traffic totals -s, --sort SORT sort interfaces by [rate, traffic, rx, tx, rxs, txs, announces, arx, atx, held]` 

- `-r, --reverse reverse sorting -j, --json output in JSON format -R hash transport identity hash of remote instance to get status from -i path path to identity used for remote management -w seconds timeout before giving up on remote queries -d, --discovered list discovered interfaces -D show details and config entries for discovered interfaces -m, --monitor continuously monitor status` 

- `-I, --monitor-interval seconds` 

```
refreshintervalformonitormode(default:1)
```

- `-v, --verbose` 

## **Note** 

When using `-R` to query a remote transport instance, you must also specify `-i` with the path to a management identity file that is authorized for remote management on the target system. 

## **5.2.3 The rnid Utility** 

With the `rnid` utility, you can generate, manage and view Reticulum Identities. The program can also calculate Destination hashes, and perform encryption and decryption of files. 

Using `rnid` , it is possible to asymmetrically encrypt files and information for any Reticulum destination hash, and also to create and verify cryptographic signatures. 

## **Usage Examples** 

Generate a new Identity: 

```
$rnid-g./new_identity
```

Display Identity key information: 

```
$rnid-i./new_identity-p
```

```
LoadedIdentity<984b74a3f768bef236af4371e6f248cd>fromnew_id
PublicKey:0f4259fef4521ab75a3409e353fe9073eb10783b4912a6a9937c57bf44a62c1e
PrivateKey:Hidden
```

Encrypt a file for an LXMF user: 

**5.2. Included Utility Programs** 

**47** 

**Reticulum Network Stack, Release 1.3.0** 

```
$rnid-i8dd57a738226809646089335a6b03695-emy_file.txt
```

`Recalled Identity <bc7291552be7a58f361522990465165c> for destination` _˓→_ `<8dd57a738226809646089335a6b03695> Encrypting my_file.txt File my_file.txt encrypted for <bc7291552be7a58f361522990465165c> to my_file.txt.rfe` 

If the Identity for the destination is not already known, you can fetch it from the network by using the `-R` command-line option: 

```
$rnid-R-i30602def3b3506a28ed33db6f60cc6c9-emy_file.txt
```

`Requesting unknown Identity for <30602def3b3506a28ed33db6f60cc6c9>... Received Identity <2b489d06eaf7c543808c76a5332a447d> for destination` _˓→_ `<30602def3b3506a28ed33db6f60cc6c9> from the network Encrypting my_file.txt File my_file.txt encrypted for <2b489d06eaf7c543808c76a5332a447d> to my_file.txt.rfe` 

Decrypt a file using the Reticulum Identity it was encrypted for: 

```
$rnid-i./my_identity-dmy_file.txt.rfe
```

```
LoadedIdentity<2225fdeecaf6e2db4556c3c2d7637294>from./my_identity
Decrypting./my_file.txt.rfe...
File./my_file.txt.rfedecryptedwith<2225fdeecaf6e2db4556c3c2d7637294>to./my_file.txt
```

## **All Command-Line Options** 

```
usage:rnid.py[-h][--configpath][-iidentity][-gpath][-v][-q][-aaspects]
[-Haspects][-epath][-dpath][-spath][-Vpath][-rpath][-wpath]
[-f][-R][-tseconds][-p][-P][--version]
```

```
ReticulumIdentity&EncryptionUtility
```

`options: -h, --help show this help message and exit --config path path to alternative Reticulum config directory -i, --identity identity hexadecimal Reticulum identity or destination hash, or path to␣` _˓→_ `Identity file -g, --generate file generate a new Identity -m, --import identity_data import Reticulum identity in hex, base32 or base64 format -x, --export export identity to hex, base32 or base64 format -v, --verbose increase verbosity -q, --quiet decrease verbosity -a, --announce aspects announce a destination based on this Identity -H, --hash aspects show destination hashes for other aspects for this Identity -e, --encrypt file encrypt file -d, --decrypt file decrypt file -s, --sign path sign file -V, --validate path validate signature` 

(continues on next page) 

**Chapter 5. Using Reticulum on Your System** 

**48** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
-r,--readfileinputfilepath
-w,--writefileoutputfilepath
-f,--forcewriteoutputevenifitoverwritesexistingfiles
-R,--requestrequestunknownIdentitiesfromthenetwork
-tsecondsidentityrequesttimeoutbeforegivingup
-p,--print-identityprintidentityinfoandexit
-P,--print-privateallowdisplayingprivatekeys
-b,--base64Usebase64-encodedinputandoutput
-B,--base32Usebase32-encodedinputandoutput
--versionshowprogram'sversionnumberandexit
```

## **5.2.4 The rnpath Utility** 

With the `rnpath` utility, you can look up and view paths for destinations on the Reticulum network. 

## **Usage Examples** 

Resolve path to a destination: 

```
$rnpathc89b4da064bf66d280f0e4d8abfd9806
```

`Path found, destination <c89b4da064bf66d280f0e4d8abfd9806> is 4 hops away via` _˓→_ `<f53a1c4278e0726bb73fcc623d6ce763> on TCPInterface[Testnet/dublin.connect.reticulum.` _˓→_ `network:4965]` 

## **All Command-Line Options** 

```
usage:rnpath[-h][--configCONFIG][--version][-t][-mhops][-r][-d][-D]
[-x][-wseconds][-Rhash][-ipath][-Wseconds][-b][-B][-U]
[--durationDURATION][--reasonREASON][-p][-j][-v]
[destination][list_filter]
```

```
ReticulumPathManagementUtility
```

**==> picture [398 x 224] intentionally omitted <==**

**----- Start of picture text -----**<br>
|||||||||||
|---|---|---|---|---|---|---|---|---|---|
|positional|arguments:|
|destination|hexadecimal|hash|of|the|destination|
|list_filter|filter|for|remote|blackhole|list|view|
|options:|
|-h,|--help|show|this|help|message|and|exit|
|--config|CONFIG|path|to|alternative|Reticulum|config|directory|
|--version|show|program's|version|number|and|exit|
|-t,|--table|show|all|known|paths|
|-m,|--max|hops|maximum|hops|to|filter|path|table|by|
|-r,|--rates|show|announce|rate|info|
|-d,|--drop|remove|the|path|to|a|destination|
|-D,|--drop-announces|drop|all|queued|announces|
|-x,|--drop-via|drop|all|paths|via|specified|transport|instance|
|-w|seconds|timeout|before|giving|up|
|-R|hash|transport|identity|hash|of|remote|instance|to|manage|
|-i|path|path|to|identity|used|for|remote|management|
|-W|seconds|timeout|before|giving|up|on|remote|queries|
|-b,|--blackholed|list|blackholed|identities|

**----- End of picture text -----**<br>


(continues on next page) 

**5.2. Included Utility Programs** 

**49** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
-B,--blackholeblackholeidentity
-U,--unblackholeunblackholeidentity
--durationDURATIONdurationofblackholeenforcementinhours
--reasonREASONreasonforblackholingidentity
-p,--blackholed-list
viewpublishedblackholelistforremotetransportinstance
-j,--jsonoutputinJSONformat
-v,--verbose
```

## **5.2.5 The rnprobe Utility** 

The `rnprobe` utility lets you probe a destination for connectivity, similar to the `ping` program. Please note that probes will only be answered if the specified destination is configured to send proofs for received packets. Many destinations will not have this option enabled, so most destinations will not be probable. 

You can enable a probe-reply destination on Reticulum Transport Instances by setting the `respond_to_probes` configuration directive. Reticulum will then print the probe destination to the log on Transport Instance startup. 

## **Usage Examples** 

Probe a destination: 

```
$rnprobernstransport.probe2d03725b327348980d570f739a3a5708
```

```
Sent16byteprobeto<2d03725b327348980d570f739a3a5708>
Validreplyreceivedfrom<2d03725b327348980d570f739a3a5708>
Round-triptimeis38.469millisecondsover2hops
```

Send a larger probe: 

```
$rnprobernstransport.probe2d03725b327348980d570f739a3a5708-s256
```

```
Sent16byteprobeto<2d03725b327348980d570f739a3a5708>
Validreplyreceivedfrom<2d03725b327348980d570f739a3a5708>
Round-triptimeis38.781millisecondsover2hops
```

If the interface that receives the probe replies supports reporting radio parameters such as **RSSI** and **SNR** , the `rnprobe` utility will print these as part of the result as well. 

```
$rnprobernstransport.probee7536ee90bd4a440e130490b87a25124
```

```
Sent16byteprobeto<e7536ee90bd4a440e130490b87a25124>
Validreplyreceivedfrom<e7536ee90bd4a440e130490b87a25124>
Round-triptimeis1.809secondsover1hop[RSSI-73dBm][SNR12.0dB]
```

## **All Command-Line Options** 

```
usage:rnprobe[-h][--configCONFIG][-sSIZE][-nPROBES]
[-tseconds][-wseconds][--version][-v]
[full_name][destination_hash]
ReticulumProbeUtility
positionalarguments:
```

(continues on next page) 

**Chapter 5. Using Reticulum on Your System** 

**50** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
full_namefulldestinationnameindottednotation
destination_hashhexadecimalhashofthedestination
options:
-h,--helpshowthishelpmessageandexit
--configCONFIGpathtoalternativeReticulumconfigdirectory
-sSIZE,--sizeSIZEsizeofprobepacketpayloadinbytes
-nPROBES,--probesPROBES
numberofprobestosend
-tseconds,--timeoutseconds
timeoutbeforegivingup
-wseconds,--waitseconds
timebetweeneachprobe
--versionshowprogram'sversionnumberandexit
-v,--verbose
```

## **5.2.6 The rncp Utility** 

The `rncp` utility is a simple file transfer tool. Using it, you can transfer files through Reticulum. 

## **Usage Examples** 

Run rncp on the receiving system, specifying which identities are allowed to send files: 

```
$rncp--listen-a1726dbad538775b5bf9b0ea25a4079c8-ac50cc4e4f7838b6c31f60ab9032cbc62
```

You can also specify allowed identity hashes (one per line) in the file ~/.rncp/allowed_identities and simply running the program in listener mode: 

```
$rncp--listen
```

From another system, copy a file to the receiving system: 

```
$rncp~/path/to/file.tgz73cbd378bb0286ed11a707c13447bb1e
```

Or fetch a file from the remote system: 

```
$rncp--fetch~/path/to/file.tgz73cbd378bb0286ed11a707c13447bb1e
```

The default identity file is stored in `~/.reticulum/identities/rncp` , but you can use another one, which will be created if it does not already exist 

```
$rncp~/path/to/file.tgz73cbd378bb0286ed11a707c13447bb1e-i/path/to/identity
```

## **All Command-Line Options** 

```
usage:rncp[-h][--configpath][-v][-q][-S][-l][-F][-f]
[-jpath][-bseconds][-aallowed_hash][-n][-p]
[-iidentity][-wseconds][--version][file][destination]
ReticulumFileTransferUtility
positionalarguments:
filefiletobetransferred
```

(continues on next page) 

**5.2. Included Utility Programs** 

**51** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
destination
```

```
hexadecimalhashofthereceiver
```

```
options:
-h,--helpshowthishelpmessageandexit
--configpathpathtoalternativeReticulumconfigdirectory
-v,--verboseincreaseverbosity
-q,--quietdecreaseverbosity
-S,--silentdisabletransferprogressoutput
-l,--listenlistenforincomingtransferrequests
-C,--no-compressdisableautomaticcompression
-F,--allow-fetchallowauthenticatedclientstofetchfiles
-f,--fetchfetchfilefromremotelistenerinsteadofsending
-j,--jailpathrestrictfetchrequeststospecifiedpath
-s,--savepathsavereceivedfilesinspecifiedpath
-O,--overwriteAllowoverwritingreceivedfiles,insteadofaddingpostfix
-bsecondsannounceinterval,0toonlyannounceatstartup
-aallowed_hashallowthisidentity(oraddin~/.rncp/allowed_identities)
-n,--no-authacceptrequestsfromanyone
-p,--print-identityprintidentityanddestinationinfoandexit
-iidentitypathtoidentitytouse
-wsecondssendertimeoutbeforegivingup
-P,--phy-ratesdisplayphysicallayertransferrates
--versionshowprogram'sversionnumberandexit
```

## **5.2.7 The rngit Utility** 

The `rngit` utility provides full Git repository hosting and interaction over Reticulum, as well as many other useful features for software development, collaboration and publishing. It allows you to host Git repositories on Reticulum nodes, interact with remote repositories using standard Git commands through the `rns://` URL scheme, and to publish software releases. 

The system consists of two parts: The `rngit` node that hosts and manages repositories, and the `git-remote-rns` helper that enables Git to communicate with rngit nodes. As soon as you have RNS installed on your system, you can transparently use Git with Reticulum-hosted repositories just like any other type of remote. Git over Reticulum uses URLs in the following format: `rns://DESTINATION_HASH/group/repo` . 

If you set a branch to track a Reticulum remote as the default upstream, you can simply use `git` as you normally would; all commands work transparently and as expected. 

## **Warning** 

**The rngit program is a new addition to RNS!** This functionality was introduced in RNS 1.2.0. While great care has been taken to design a secure, but highly configurable and flexible permission system for allowing many users to interact with many different repositories on a single node, `rngit` has not been tested extensively in the wild! Be careful when hosting repositories, especially if they are public or semi-public. 

For the full documentation on the _rngit_ system, see the _Git Over Reticulum_ chapter of this manual. 

**Chapter 5. Using Reticulum on Your System** 

**52** 

**Reticulum Network Stack, Release 1.3.0** 

## **5.2.8 The rnx Utility** 

The `rnx` utility is a basic remote command execution program. It allows you to execute commands on remote systems over Reticulum, and to view returned command output. For a fully interactive remote shell solution, be sure to also take a look at the rnsh program. 

## **Usage Examples** 

Run rnx on the listening system, specifying which identities are allowed to execute commands: 

```
$rnx--listen-a941bed5e228775e5a8079fc38b1ccf3f-a1b03013c25f1c2ca068a4f080b844a10
```

From another system, run a command on the remote: 

```
$rnx7a55144adf826958a9529a3bcf08b149"cat/proc/cpuinfo"
```

Or enter the interactive mode pseudo-shell: 

```
$rnx7a55144adf826958a9529a3bcf08b149-x
```

The default identity file is stored in `~/.reticulum/identities/rnx` , but you can use another one, which will be created if it does not already exist 

```
$rnx7a55144adf826958a9529a3bcf08b149-i/path/to/identity-x
```

## **All Command-Line Options** 

```
usage:rnx[-h][--configpath][-v][-q][-p][-l][-iidentity][-x][-b][-n][-N]
[-d][-m][-aallowed_hash][-wseconds][-Wseconds][--stdinSTDIN]
[--stdoutSTDOUT][--stderrSTDERR][--version][destination][command]
```

```
ReticulumRemoteExecutionUtility
```

**==> picture [367 x 272] intentionally omitted <==**

**----- Start of picture text -----**<br>
||||||||||
|---|---|---|---|---|---|---|---|---|
|positional|arguments:|
|destination|hexadecimal|hash|of|the|listener|
|command|command|to|be|execute|
|optional|arguments:|
|-h,|--help|show|this|help|message|and|exit|
|--config|path|path|to|alternative|Reticulum|config|directory|
|-v,|--verbose|increase|verbosity|
|-q,|--quiet|decrease|verbosity|
|-p,|--print-identity|print|identity|and|destination|info|and|exit|
|-l,|--listen|listen|for|incoming|commands|
|-i|identity|path|to|identity|to|use|
|-x,|--interactive|enter|interactive|mode|
|-b,|--no-announce|don't|announce|at|program|start|
|-a|allowed_hash|accept|from|this|identity|
|-n,|--noauth|accept|files|from|anyone|
|-N,|--noid|don't|identify|to|listener|
|-d,|--detailed|show|detailed|result|output|
|-m|mirror|exit|code|of|remote|command|
|-w|seconds|connect|and|request|timeout|before|giving|up|
|-W|seconds|max|result|download|time|
|--stdin|STDIN|pass|input|to|stdin|
|--stdout|STDOUT|max|size|in|bytes|of|returned|stdout|

**----- End of picture text -----**<br>


(continues on next page) 

**5.2. Included Utility Programs** 

**53** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
--stderrSTDERRmaxsizeinbytesofreturnedstderr
--versionshowprogram'sversionnumberandexit
```

## **5.2.9 The rnsh Utility** 

The `rnsh` utility provides a fully interactive remote shell over Reticulum. It allows you to establish encrypted, authenticated shell sessions on remote systems, complete with terminal emulation, pipe support, and window resizing. 

While the `rnx` utility is useful for simple remote command execution and retrieving output, `rnsh` provides a complete interactive terminal experience, making it ideal for remote administration and management tasks that require real-time interaction, just like SSH does for IP networks. 

`rnsh` operates in two modes: a _listener_ mode that accepts incoming connections, and an _initiator_ mode that connects to a remote listener. Both sides authenticate using Reticulum Identities, ensuring that only authorised peers can establish sessions. 

## **Note** 

`rnsh` provides a genuine interactive terminal over Reticulum. It supports full terminal emulation including escape sequences, window resizing, signal forwarding, and piping of standard input, output and error streams. This makes it suitable for running text editors, terminal multiplexers, and any other interactive programs on remote systems. 

## **Usage Examples** 

Start `rnsh` in listener mode, accepting connections from specific identities: 

```
$rnsh-l-a941bed5e228775e5a8079fc38b1ccf3f-a1b03013c25f1c2ca068a4f080b844a10
```

You can also specify allowed identity hashes (one per line) in the file `~/.rnsh/allowed_identities` or `~/.config/ rnsh/allowed_identities` , and simply run the program in listener mode: 

```
$rnsh-l
```

Connect to a remote listener from another system: 

```
$rnsh7a55144adf826958a9529a3bcf08b149
```

Specify a command to run on the remote system, separating `rnsh` options from the remote command with `--` : 

```
$rnsh7a55144adf826958a9529a3bcf08b149--top
```

Set a default command for the listener, in case the initiator does not supply one, or when remote command execution is disabled: 

```
$rnsh-l--/bin/bash--login
```

Use the `-m` flag to mirror the exit code of the remote process: 

```
$rnsh-m7a55144adf826958a9529a3bcf08b149--/usr/local/bin/check-status
```

Use the `-p` flag to display the identity and destination hash for a listener: 

**Chapter 5. Using Reticulum on Your System** 

**54** 

**Reticulum Network Stack, Release 1.3.0** 

```
$rnsh-l-p
```

```
Identity:<984b74a3f768bef236af4371e6f248cd>
Listeningon:7a55144adf826958a9529a3bcf08b149
```

Use a specific identity file rather than the default: 

```
$rnsh-l-i/path/to/identity
```

Announce the listener destination on startup, and periodically: 

```
$rnsh-l-b900
```

The `-b` option specifies the announce period in seconds. Use `0` to announce only once at startup. 

## **Authentication & Authorisation** 

By default, `rnsh` requires that connecting initiators identify themselves with a Reticulum Identity whose hash is present in the list of allowed identities. Allowed identities can be specified on the command line with the `-a` option, and can be used multiple times: 

```
$rnsh-l-a941bed5e228775e5a8079fc38b1ccf3f-a1b03013c25f1c2ca068a4f080b844a10
```

You can also maintain a list of allowed identity hashes in the file `~/.rnsh/allowed_identities` or `~/.config/ rnsh/allowed_identities` , with one hex hash per line. This file is reloaded every time a new connection is received, so changes take effect immediately without restarting `rnsh` . 

If you want to accept connections from any identity (for testing or in fully trusted environments), you can disable authentication with the `-n` option: 

```
$rnsh-l-n
```

## **Warning** 

Disabling authentication with `-n` means that **any** Reticulum peer that can reach your listener will be able to execute commands on your system. Only use this option if you _really_ know what you’re doing. 

## **Remote Command Control** 

When running in listener mode, `rnsh` allows you to control how remote commands are handled: 

- By default, the listener accepts the command sent by the initiator. If the initiator does not supply a command, the listener’s default shell is used. 

- Use `-C` ( `--no-remote-command` ) to disable execution of commands received from the initiator. Only the listener’s default command (or the command specified after `--` ) will be executed: 

```
$rnsh-l-C--/usr/local/bin/safe-script
```

- Use `-A` ( `--remote-command-as-args` ) to append the initiator’s command to the listener’s default command instead of replacing it. This can be useful for restricting the remote to a specific program while still allowing the initiator to pass arguments: 

```
$rnsh-l-A--/usr/bin/top
```

**5.2. Included Utility Programs** 

**55** 

**Reticulum Network Stack, Release 1.3.0** 

## **Service Names** 

When running in listener mode, `rnsh` uses a service name to differentiate between multiple listener instances that may share the same identity. By default, the service name is `default` . You can specify a different service name with the `-s` option: 

```
$rnsh-l-smonitoring
```

This allows you to run multiple listeners on the same node, each with a different service name and purpose. 

## **Initiator Options** 

When connecting to a remote listener, several options are available: 

- Use `-N` ( `--no-id` ) to disable sending your identity to the remote listener. Note that the listener must have authentication disabled ( `-n` ) for the connection to succeed in this case. 

- Use `-m` ( `--mirror` ) to make the initiator return with the exit code of the remote process, rather than always returning `0` . 

- Use `-w` ( `--timeout` ) to specify the connection and request timeout in seconds. By default, the timeout matches the Reticulum path request timeout. 

## **Identity & Destination** 

The default identity file for `rnsh` is stored at `~/.reticulum/identities/rnsh` , but you can specify a different one with the `-i` option, which will be created if it does not already exist: 

```
$rnsh-l-i/path/to/identity
```

To display the identity and destination information for a listener, use the `-p` option. When combined with `-l` , both the identity and the listening destination hash are displayed: 

```
$rnsh-p
Identity:<984b74a3f768bef236af4371e6f248cd>
$rnsh-l-p
Identity:<984b74a3f768bef236af4371e6f248cd>
Listeningon:7a55144adf826958a9529a3bcf08b149
```

## **Verbosity** 

Like other Reticulum utilities, `rnsh` supports the `-v` and `-q` flags to increase or decrease logging verbosity. Multiple flags can be specified to further adjust the log level. The default log level is `INFO` for listeners and `ERROR` for initiators. 

```
$rnsh-l-vv#Listenerwithdebug-leveloutput
$rnsh-q7a55144adf826958a9529a3bcf08b149#Quietinitiator
```

By default, all log output is routed to `~/.rnsh/logfile` for initiators. 

## **Escape Sequences** 

During an active `rnsh` session, the following escape sequences are available. These are only recognised immediately after a newline character: 

- `~~` - Send a literal tilde character 

- `~.` - Terminate the session and exit immediately 

- `~L` - Toggle line-interactive mode 

**Chapter 5. Using Reticulum on Your System** 

**56** 

**Reticulum Network Stack, Release 1.3.0** 

- `~?` - Display the escape sequence quick reference 

## **All Command-Line Options** 

```
usage:rnsh[-h][--configCONFIG][--identityIDENTITY][-v][-q][-p]
[--version][-l][-sSERVICE][-bPERIOD][-aHASH][-n][-A][-C]
[-N][-m][-wSECONDS]
[destination]
```

**==> picture [408 x 464] intentionally omitted <==**

**----- Start of picture text -----**<br>
||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|
|Reticulum|Remote|Shell|Utility|
|positional|arguments:|
|destination|hexadecimal|hash|of|the|destination|to|connect|to|
|options:|
|-h,|--help|show|this|help|message|and|exit|
|--config,|-c|CONFIG|path|to|alternative|Reticulum|config|directory|
|--identity,|-i|IDENTITY|
|path|to|identity|file|to|use|
|-v,|--verbose|increase|verbosity|
|-q,|--quiet|decrease|verbosity|
|-p,|--print-identity|print|identity|and|destination|info|and|exit|
|--version|show|program's|version|number|and|exit|
|-l,|--listen|listen|(server)|mode;|any|command|specified|after|--|
|will|be|used|as|the|default|command|when|the|initiator|
|does|not|provide|one|or|when|remote|command|execution|
|is|disabled;|if|no|command|is|specified,|the|default|
|shell|of|the|user|running|rnsh|will|be|used|
|-s,|--service|SERVICE|
|service|name|for|identity|file|if|not|the|default|
|-b,|--announce|PERIOD|
|announce|on|startup|and|every|PERIOD|seconds;|specify|
|0|to|announce|on|startup|only|
|-a,|--allowed|HASH|allow|this|identity|to|connect|(may|be|specified|
|multiple|times);|allowed|identities|can|also|be|
|specified|in|~/.rnsh/allowed_identities|or|
|~/.config/rnsh/allowed_identities,|one|hash|per|line|
|-n,|--no-auth|disable|authentication|(allow|any|identity|to|connect)|
|-A,|--remote-command-as-args|
|concatenate|remote|command|to|the|argument|list|of|the|
|default|program|or|shell|
|-C,|--no-remote-command|
|disable|executing|command|lines|received|from|the|
|remote|initiator|
|-N,|--no-id|disable|identity|announcement|on|connect|
|-m,|--mirror|return|with|the|exit|code|of|the|remote|process|
|-w,|--timeout|SECONDS|
|connect|and|request|timeout|in|seconds|

**----- End of picture text -----**<br>


```
Whenspecifyingacommandtoexecute,separaternshoptionsfromthecommand
anditsargumentswith--.Forexample:
```

```
rnsh-l--/bin/bash--login
rnsh<destination>--ls-la/tmp
```

**5.2. Included Utility Programs** 

**57** 

**Reticulum Network Stack, Release 1.3.0** 

## **5.2.10 The rnodeconf Utility** 

The `rnodeconf` utility allows you to inspect and configure existing _RNodes_ , and to create and provision new _RNodes_ from any supported hardware devices. 

## **All Command-Line Options** 

```
usage:rnodeconf[-h][-i][-a][-u][-U][--fw-versionversion]
```

```
[--fw-urlurl][--nocheck][-e][-E][-C]
[--baud-flashbaud_flash][-N][-T][-b][-B][-p][-Di]
[--display-addrbyte][--freqHz][--bwHz][--txpdBm]
[--sffactor][--crrate][--eeprom-backup][--eeprom-dump]
[--eeprom-wipe][-P][--trust-keyhexbytes][--version][-f]
[-r][-k][-S][-HFIRMWARE_HASH][--platformplatform]
[--productproduct][--modelmodel][--hwrevrevision]
[port]
```

```
RNodeConfigurationandfirmwareutility.Thisprogramallowsyoutochange
varioussettingsandstartupmodesofRNode.Itcanalsoinstall,flashand
updatethefirmwareonsupporteddevices.
```

`positional arguments: port serial port where RNode is attached options: -h, --help show this help message and exit -i, --info Show device info -a, --autoinstall Automatic installation on various supported devices -u, --update Update firmware to the latest version -U, --force-update Update to specified firmware even if version matches or is older␣` _˓→_ `than installed version --fw-version version Use a specific firmware version for update or autoinstall --fw-url url Use an alternate firmware download URL --nocheck Don't check for firmware updates online -e, --extract Extract firmware from connected RNode for later use -E, --use-extracted Use the extracted firmware for autoinstallation or update -C, --clear-cache Clear locally cached firmware files --baud-flash baud_flash Set specific baud rate when flashing device. Default is 921600 -N, --normal Switch device to normal mode -T, --tnc Switch device to TNC mode -b, --bluetooth-on Turn device bluetooth on -B, --bluetooth-off Turn device bluetooth off -p, --bluetooth-pair Put device into bluetooth pairing mode -D, --display i Set display intensity (0-255) -t, --timeout s Set display timeout in seconds, 0 to disable -R, --rotation rotation Set display rotation, valid values are 0 through 3 --display-addr byte Set display address as hex byte (00 - FF) --recondition-display Start display reconditioning --np i Set NeoPixel intensity (0-255) --freq Hz Frequency in Hz for TNC mode --bw Hz Bandwidth in Hz for TNC mode` 

(continues on next page) 

**Chapter 5. Using Reticulum on Your System** 

**58** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

- `--txp dBm TX power in dBm for TNC mode --sf factor Spreading factor for TNC mode (7 - 12) --cr rate Coding rate for TNC mode (5 - 8) -x, --ia-enable Enable interference avoidance -X, --ia-disable Disable interference avoidance -c, --config Print device configuration --eeprom-backup Backup EEPROM to file --eeprom-dump Dump EEPROM to console --eeprom-wipe Unlock and wipe EEPROM -P, --public Display public part of signing key --trust-key hexbytes Public key to trust for device verification --version Print program version and exit -f, --flash Flash firmware and bootstrap EEPROM -r, --rom Bootstrap EEPROM without flashing firmware -k, --key Generate a new signing key and exit -S, --sign Display public part of signing key -H, --firmware-hash FIRMWARE_HASH Set installed firmware hash` 

- `--platform platform Platform specification for device bootstrap --product product Product specification for device bootstrap --model model Model code for device bootstrap --hwrev revision Hardware revision for device bootstrap` 

For more information on how to create your own RNodes, please read the _Creating RNodes_ section of this manual. 

## **5.3 Discovering Interfaces** 

Reticulum includes built-in functionality for discovering connectable interfaces over Reticulum itself. This is particularly useful in situations where you want to do one or more of the following: 

- Discover connectable entrypoints available on the Internet 

- Find connectable radio access points in the physical world 

- Maintain connectivity to RNS instances with unknown or changing IP addresses 

Discovered interfaces can be **auto-connected** by Reticulum, which makes it possible to create setups where an arbitrary interface can act simply as a bootstrap connection, that can be torn down again once more suitable interfaces have been discovered and connected. 

The interface discovery mechanism uses announces sent over Reticulum itself, and supports both publicly readable interfaces and private, encrypted discovery, that can only be decoded by specified _network identities_ . It is also possible to specify which network identities should be considered valid sources for discovered interfaces, so that interfaces published by unknown entities are ignored. 

## **Note** 

A _network identity_ is a normal Reticulum identity keyset that can be used by one or more transport nodes to identify them as belonging to the same overall network. In the context of interface discovery, this makes it easy to manage connecting to only the particular networks you care about, even if those networks utilize many individual physical transport node. 

This also makes it convenient to auto-connect discovered interfaces only for networks you have some level of trust in. 

**5.3. Discovering Interfaces** 

**59** 

**Reticulum Network Stack, Release 1.3.0** 

For information on how to make your interfaces discoverable, see the _Discoverable Interfaces_ chapter of this manual. The current section will focus on how to actually _discover and connect to_ interfaces available on the network. 

In its most basic form, enabling interface discovery is as simple as setting `discover_interfaces` to `true` in your Reticulum config: 

```
[reticulum]
...
discover_interfaces=yes
...
```

Once this option is enabled, your RNS instance will start listening for interface discovery announces, and store them for later use or inspection. You can list discovered interfaces with the `rnstatus` utility: 

```
$rnstatus-d
```

**==> picture [385 x 45] intentionally omitted <==**

**----- Start of picture text -----**<br>
|||||||||||
|---|---|---|---|---|---|---|---|---|---|
|Name|Type|Status|Last|Heard|Value|Location|
|-------------------------------------------------------------------------|
|Sideband|Hub|Backbone|✓|Available|1h|ago|16|46.2316,|6.0536|
|RNS|Amsterdam|Backbone|✓|Available|32m|ago|16|52.3865,|4.9037|

**----- End of picture text -----**<br>


You can view more detailed information about discovered interfaces, including configuration snippets for pasting directly into your `[interfaces]` config, by using the `rnstatus -D` option: 

```
$rnstatus-Dsideband
```

```
TransportID:521c87a83afb8f29e4455e77930b973b
Name:SidebandHub
Type:BackboneInterface
Status:Available
Transport:Enabled
Distance:2hops
Discovered:9hand40mago
LastHeard:1hand15mago
Location:46.2316,6.0536
Address:sideband.connect.reticulum.network:7822
StampValue:16
ConfigurationEntry:
[[SidebandHub]]
type=BackboneInterface
enabled=yes
remote=sideband.connect.reticulum.network
target_port=7822
transport_identity=521c87a83afb8f29e4455e77930b973b
```

In addition to providing local interface discovery information and control, the `rnstatus` utility can export discovered interface data in machine-readable JSON format using the `rnstatus -d --json` option. This can be useful for exporting the data to external applications such as status pages, access point maps and similar. 

To control what sources are considered valid for discovered sources, additional configuration options can be specified for the interface discovery system. 

- The `interface_discovery_sources` option is a list of the network or transport identities from which interfaces will be accepted. If this option is set, all others will be ignored. If this option is not set, discovered interfaces will be accepted from any source, but are still subject to stamp value requirements. 

**Chapter 5. Using Reticulum on Your System** 

**60** 

**Reticulum Network Stack, Release 1.3.0** 

- The `required_discovery_value` options specifies the minimum stamp value required for the interface announce to be considered valid. To make it computationally difficult to spam the network with a large number of defunct or malicious interfaces, each announced interface requires a valid cryptographical stamp, of configurable difficulty value. 

- The `autoconnect_discovered_interfaces` value defaults to `0` , and specifies the maximum number of discovered interfaces that should be auto-connected at any given time. If set to a number greater than `0` , Reticulum automatically manages discovered interface connections, and will bring discovered interfaces up and down based on availability. You can at any time add discovered interfaces to your configuration manually, to persistently keep them available. 

- The `network_identity` option specifies the _network identity_ for this RNS instance. This identity is used both to sign (and potentially encrypt) _outgoing_ interface discovery announces, and to decrypt incoming discovery information. 

The configuration snippet below contains an example of setting these additional configuration options: 

```
[reticulum]
...
discover_interfaces=yes
interface_discovery_sources=521c87a83afb8f29e4455e77930b973b
required_discovery_value=16
autoconnect_discovered_interfaces=3
network_identity=~/.reticulum/storage/identities/my_network
...
```

## **5.4 Remote Management** 

It is possible to allow remote management of Reticulum systems using the various built-in utilities, such as `rnstatus` and `rnpath` . To do so, you will need to set the `enable_remote_management` directive in the `[reticulum]` section of the configuration file. You will also need to specify one or more Reticulum Identity hashes for authenticating the queries from client programs. For this purpose, you can use existing identity files, or generate new ones with the rnid utility. 

The following is a truncated example of enabling remote management in the Reticulum configuration file: 

`[reticulum] ... enable_remote_management = yes remote_management_allowed = 9fb6d773498fb3feda407ed8ef2c3229,␣` _˓→_ `2d882c5586e548d79b5af27bca1776dc ...` 

For a complete example configuration, you can run `rnsd --exampleconfig` . 

## **5.5 Blackhole Management** 

Reticulum networks are fundamentally permissionless and open, allowing anyone with a compatible interface to participate. While this openness is essential for a resilient and decentralized network, it also exposes the network to potential abuse, such as peers flooding the network with excessive announce broadcasts or other forms of resource exhaustion. 

The **Blackhole** system provides tools to help manage this problem. It allows operators and individual users to block specific identities at the Transport layer, preventing them from propagating announces through your node, and for other nodes to reach them through your network. 

**5.4. Remote Management** 

**61** 

**Reticulum Network Stack, Release 1.3.0** 

## **Important** 

There is fundamentally **no way** to _globally_ block or censor any identity or destination in Reticulum networks. The blackhole functionality will prevent announces from (and traffic to) all destinations associated with the blackholed identity _on your own network segments only_ . 

This provides users and operators with control over what they want to allow _on their own network segments_ , but there is no way to globally censor or remove an identity, as long as _someone_ is willing to provide transport for it. 

This functionality serves a dual purpose: 

- **For Individual Users:** It offers a simple way to maintain a quiet and efficient local network by manually blocking spammy or unwanted peers. 

- **For Network Operators:** It enables the creation of federated, community-wide security standards. By publishing and sharing blackhole lists, operators can protect large infrastructures and distribute spam filtering rules across the mesh without manual intervention. 

## **5.5.1 Local Blackhole Management** 

The most immediate way to manage unwanted identities is through manual configuration using the `rnpath` utility. This allows you to instantly block or unblock specific identities on your local Transport Instance. 

## **Blackholing an Identity** 

To block an identity, use the `-B` (or `--blackhole` ) flag followed by the identity hash. You can optionally specify a duration and a reason, which are useful for logging and future reference. 

```
$rnpath-B3a4f8b9c1d2e3f4g5h6i7j8k9l0m1n2o
```

You can also add a duration (in hours) and a reason: 

```
$rnpath-B3a4f8b9c1d2e3f4g5h6i7j8k9l0m1n2o--duration24--reason"Excessiveannounces"
```

## **Lifting Blackholes** 

To remove an identity from the blackhole, use the `-U` (or `--unblackhole` ) flag: 

```
$rnpath-U3a4f8b9c1d2e3f4g5h6i7j8k9l0m1n2o
```

## **Viewing the Blackhole List** 

To see all identities currently blackholed on your local instance, use the `-b` (or `--blackholed` ) flag: 

```
$rnpath-b
```

```
<3a4f8b9c1d2e3f4g5h6i7j8k9l0m1n2o>blackholedfor23h,56m(Excessiveannounces)
<399ea050ce0eed1816c300bcb0840938>blackholedindefinitely(Announcespam)
<d56a4fa02c0a77b3575935aedd90bdb2>blackholedindefinitely(Announcespam)
<2b9ec651326d9bc274119054c70fb75e>blackholedindefinitely(Announcespam)
<1178a8f1fad405bf2ad153bf5036bdfd>blackholedindefinitely(Announcespam)
```

## **5.5.2 Automated List Sourcing** 

Manually blocking identities is effective for immediate threats, but maintaining an up-to-date blocklist for a large network is impractical. Reticulum supports **automated list sourcing** , allowing your node to subscribe to blackhole lists maintained by trusted peers, or a central authority you manage yourself. 

**Chapter 5. Using Reticulum on Your System** 

**62** 

**Reticulum Network Stack, Release 1.3.0** 

## **Warning** 

**Verify Before Subscribing!** Subscribing to a blackhole source is a powerful action that grants that source the ability to dictate who you can communicate with. Before adding a source to your configuration, verify that the maintainer aligns with your usage policy and values. Blindly subscribing to untrusted lists could inadvertently block legitimate peers or essential services. 

When enabled, your Transport Instance will periodically (approximately once per hour) connect to configured sources, retrieve their latest blackhole lists, and automatically merge them into your local blocklist. This provides “set-andforget” protection for both individual users and large networks. 

## **Configuration** 

To enable automated sourcing, add the `blackhole_sources` option to the `[reticulum]` section of your configuration file. This option accepts a comma-separated list of Transport Identity hashes that you trust to provide valid blackhole lists. 

```
[reticulum]
...
#Automaticallyfetchblackholelistsfromthesetrustedsources
blackhole_sources=521c87a83afb8f29e4455e77930b973b,68a4aa91ac350c4087564e8a69f84e86
...
```

## **How It Works** 

1. When enabled, the `BlackholeUpdater` service runs in the background. 

2. For every identity hash listed in `blackhole_sources` , it attempts to establish a temporary link to its associated``rnstransport.info.blackhole`` destination. 

3. It requests the `/list` path, which returns a dictionary of blackholed identities and their associated metadata. 

4. The received list is merged with your local `blackholed_identities` database. 

5. The lists are persisted to disk, ensuring they survive restarts. 

## **Note** 

You can verify the external lists you are subscribed to, and their contents, without importing them by using `rnpath -p` . See the _rnpath utility documentation_ for details on querying remote blackhole lists. 

## **5.5.3 Publishing Blackhole Lists** 

If you are operating a public gateway, a community hub, or simply wish to share your blackhole list with others, you can configure your instance to act as a blackhole list publisher. This allows other nodes to subscribe to _your_ definitions of unwanted traffic. 

## **Enabling Publishing** 

To publish your local blackhole list, enable the `publish_blackhole` option in the `[reticulum]` section: 

```
[reticulum]
...
publish_blackhole=yes
...
```

**5.5. Blackhole Management** 

**63** 

**Reticulum Network Stack, Release 1.3.0** 

When this is enabled, your Transport Instance will register a request handler at `rnstransport.info.blackhole` . Any peer that connects to this destination and requests `/list` will receive the complete set of identities currently present in your local blackhole database. 

## **Federation and Trust** 

The blackhole system relies on the trust relationship between the subscriber and the publisher. By subscribing to a source, you are implicitly trusting that source to only block identities that are genuinely detrimental to the network. 

As the ecosystem matures, this system is designed to integrate with **Network Identities** . This allows communities to verify that a published blackhole list is actually provided by a specific network or organization with a certain level of reputation and trustworthiness, adding a layer of cryptographic trust to the federation process. This prevents malicious actors from publishing fake lists intended to censor legitimate traffic. 

For operators, this creates a scalable model where maintaining a single high-quality blocklist can protect thousands of downstream peers, drastically reducing the administrative. 

## **5.6 Improving System Configuration** 

If you are setting up a system for permanent use with Reticulum, there is a few system configuration changes that can make this easier to administrate. These changes will be detailed here. 

## **5.6.1 Fixed Serial Port Names** 

On a Reticulum instance with several serial port based interfaces, it can be beneficial to use the fixed device names for the serial ports, instead of the dynamically allocated shorthands such as `/dev/ttyUSB0` . Under most Debian-based distributions, including Ubuntu and Raspberry Pi OS, these nodes can be found under `/dev/serial/by-id` . 

You can use such a device path directly in place of the numbered shorthands. Here is an example of a packet radio TNC configured as such: 

```
[[PacketRadioKISSInterface]]
type=KISSInterface
interface_enabled=True
outgoing=true
port=/dev/serial/by-id/usb-FTDI_FT230X_Basic_UART_43891CKM-if00-port0
speed=115200
databits=8
parity=none
stopbits=1
preamble=150
txtail=10
persistence=200
slottime=20
```

Using this methodology avoids potential naming mix-ups where physical devices might be plugged and unplugged in different orders, or when device name assignment varies from one boot to another. 

## **5.6.2 Reticulum as a System Service** 

Instead of starting Reticulum manually, you can install `rnsd` as a system service and have it start automatically at boot. 

**Chapter 5. Using Reticulum on Your System** 

**64** 

**Reticulum Network Stack, Release 1.3.0** 

## **Systemwide Service** 

If you installed Reticulum with `pip` , the `rnsd` program will most likely be located in a user-local installation path only, which means `systemd` will not be able to execute it. In this case, you can simply symlink the `rnsd` program into a directory that is in systemd’s path: 

```
sudoln-s$(whichrnsd)/usr/local/bin/
```

You can then create the service file `/etc/systemd/system/rnsd.service` with the following content: 

```
[Unit]
Description=ReticulumNetworkStackDaemon
After=multi-user.target
[Service]
#IfyourunReticulumonWiFidevices,
#orotherdevicesthatneedsomeextra
#timetoinitialise,youmightwantto
#addashortdelaybeforeReticulumis
#startedbysystemd:
#ExecStartPre=/bin/sleep10
Type=simple
Restart=always
RestartSec=3
User=USERNAMEHERE
ExecStart=rnsd--service
[Install]
WantedBy=multi-user.target
```

Be sure to replace `USERNAMEHERE` with the user you want to run `rnsd` as. 

To manually start `rnsd` run: 

```
sudosystemctlstartrnsd
```

If you want to automatically start `rnsd` at boot, run: 

```
sudosystemctlenablernsd
```

## **Userspace Service** 

Alternatively you can use a user systemd service instead of a system wide one. This way the whole setup can be done as a regular user. Create a user systemd service files `~/.config/systemd/user/rnsd.service` with the following content: 

```
[Unit]
Description=ReticulumNetworkStackDaemon
After=default.target
```

```
[Service]
#IfyourunReticulumonWiFidevices,
#orotherdevicesthatneedsomeextra
#timetoinitialise,youmightwantto
#addashortdelaybeforeReticulumis
```

(continues on next page) 

**5.6. Improving System Configuration** 

**65** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
#startedbysystemd:
#ExecStartPre=/bin/sleep10
Type=simple
Restart=always
RestartSec=3
ExecStart=RNS_BIN_DIR/rnsd--service
[Install]
WantedBy=default.target
```

Replace `RNS_BIN_DIR` with the path to your Reticulum binary directory (eg. /home/USERNAMEHERE/rns/bin). 

Start user service: 

```
systemctl--userdaemon-reload
systemctl--userstartrnsd.service
```

If you want to automatically start `rnsd` without having to log in as the USERNAMEHERE, do: 

```
sudologinctlenable-lingerUSERNAMEHERE
systemctl--userenablernsd.service
```

**Chapter 5. Using Reticulum on Your System** 

**66** 

**CHAPTER SIX** 

## **UNDERSTANDING RETICULUM** 

This chapter will briefly describe the overall purpose and operating principles of Reticulum. It should give you an overview of how the stack works, and an understanding of how to develop networked applications using Reticulum. 

This chapter is not an exhaustive source of information on Reticulum, at least not yet. Currently, the only complete repository, and final authority on how Reticulum actually functions, is the Python reference implementation and API reference. That being said, this chapter is an essential resource in understanding how Reticulum works from a high-level perspective, along with the general principles of Reticulum, and how to apply them when creating your own networks or software. 

After reading this chapter, you should be well-equipped to understand how a Reticulum network operates, what it can achieve, and how you can use it yourself. This chapter also seeks to provide an overview of the sentiments and the philosophy behind Reticulum, what problems it seeks to solve, and how it approaches those solutions. 

## **6.1 Motivation** 

The primary motivation for designing and implementing Reticulum has been the current lack of reliable, functional and secure minimal-infrastructure modes of digital communication. It is my belief that it is highly desirable to create a reliable and efficient way to set up long-range digital communication networks that can securely allow exchange of information between people and machines, with no central point of authority, control, censorship or barrier to entry. 

Almost all of the various networking systems in use today share a common limitation: They require large amounts of coordination and centralised trust and power to function. To join such networks, you need approval of gatekeepers in control. This need for coordination and trust inevitably leads to an environment of central control, where it’s very easy for infrastructure operators or governments to control or alter traffic, and censor or persecute unwanted actors. It also makes it completely impossible to freely deploy and use networks at will, like one would use other common tools that enhance individual agency and freedom. 

Reticulum aims to require as little coordination and trust as possible. It aims to make secure, anonymous and permissionless networking and information exchange a tool that anyone can just pick up and use. 

Since Reticulum is completely medium agnostic, it can be used to build networks on whatever is best suited to the situation, or whatever you have available. In some cases, this might be packet radio links over VHF frequencies, in other cases it might be a 2.4 GHz network using off-the-shelf radios, or it might be using common LoRa development boards. 

At the time of release of this document, the fastest and easiest setup for development and testing is using LoRa radio modules with an open source firmware (see the section _Reference Setup_ ), connected to any kind of computer or mobile device that Reticulum can run on. 

The ultimate aim of Reticulum is to allow anyone to be their own network operator, and to make it cheap and easy to cover vast areas with a myriad of independent, interconnectable and autonomous networks. Reticulum **is not** _one network_ , it **is a tool** to build _thousands of networks_ . Networks without kill-switches, surveillance, censorship and control. Networks that can freely interoperate, associate and disassociate with each other, and require no central oversight. Networks for human beings. _Networks for the people_ . 

**67** 

**Reticulum Network Stack, Release 1.3.0** 

## **6.2 Goals** 

To be as widely usable and efficient to deploy as possible, the following goals have been used to guide the design of Reticulum: 

## • **Fully useable as open source software stack** 

Reticulum must be implemented with, and be able to run using only open source software. This is critical to ensuring the availability, security and transparency of the system. 

## • **Hardware layer agnosticism** 

Reticulum must be fully hardware agnostic, and shall be useable over a wide range of physical networking layers, such as data radios, serial lines, modems, handheld transceivers, wired Ethernet, WiFi, or anything else that can carry a digital data stream. Hardware made for dedicated Reticulum use shall be as cheap as possible and use off-the-shelf components, so it can be easily modified and replicated by anyone interested in doing so. 

## • **Very low bandwidth requirements** 

Reticulum should be able to function reliably over links with a transmission capacity as low as _5 bits per second_ . 

## • **Encryption by default** 

Reticulum must use strong encryption by default for all communication. 

## • **Initiator Anonymity** 

It must be possible to communicate over a Reticulum network without revealing any identifying information about oneself. 

## • **Unlicensed use** 

Reticulum shall be functional over physical communication mediums that do not require any form of license to use. Reticulum must be designed in a way, so it is usable over ISM radio frequency bands, and can provide functional long distance links in such conditions, for example by connecting a modem to a PMR or CB radio, or by using LoRa or WiFi modules. 

## • **Supplied software** 

In addition to the core networking stack and API, that allows a developer to build applications with Reticulum, a basic set of Reticulum-based communication tools must be implemented and released along with Reticulum itself. These shall serve both as a functional, basic communication suite, and as an example and learning resource to others wishing to build applications with Reticulum. 

## • **Ease of use** 

The reference implementation of Reticulum is written in Python, to make it easy to use and understand. A programmer with only basic experience should be able to use Reticulum to write networked applications. 

## • **Low cost** 

It shall be as cheap as possible to deploy a communication system based on Reticulum. This should be achieved by using cheap off-the-shelf hardware that potential users might already own. The cost of setting up a functioning node should be less than $100 even if all parts needs to be purchased. 

## **6.3 Introduction & Basic Functionality** 

Reticulum is a networking stack suited for high-latency, low-bandwidth links. Reticulum is at its core a _message oriented_ system. It is suited for both local point-to-point or point-to-multipoint scenarios where all nodes are within range of each other, as well as scenarios where packets need to be transported over multiple hops in a complex network to reach the recipient. 

Reticulum does away with the idea of addresses and ports known from IP, TCP and UDP. Instead Reticulum uses the singular concept of _destinations_ . Any application using Reticulum as its networking stack will need to create one or more destinations to receive data, and know the destinations it needs to send data to. 

**Chapter 6. Understanding Reticulum** 

**68** 

**Reticulum Network Stack, Release 1.3.0** 

All destinations in Reticulum are _represented_ as a 16 byte hash. This hash is derived from truncating a full SHA256 hash of identifying characteristics of the destination. To users, the destination addresses will be displayed as 16 hexadecimal bytes, like this example: `<13425ec15b621c1d928589718000d814>` . 

The truncation size of 16 bytes (128 bits) for destinations has been chosen as a reasonable trade-off between address space and packet overhead. The address space accommodated by this size can support many billions of simultaneously active devices on the same network, while keeping packet overhead low, which is essential on low-bandwidth networks. In the very unlikely case that this address space nears congestion, a one-line code change can upgrade the Reticulum address space all the way up to 256 bits, ensuring the Reticulum address space could potentially support galacticscale networks. This is obviously complete and ridiculous over-allocation, and as such, the current 128 bits should be sufficient, even far into the future. 

By default Reticulum encrypts all data using elliptic curve cryptography and AES. Any packet sent to a destination is encrypted with a per-packet derived key. Reticulum can also set up an encrypted channel to a destination, called a _Link_ . Both data sent over Links and single packets offer _Initiator Anonymity_ . Links additionally offer _Forward Secrecy_ by default, employing an Elliptic Curve Diffie Hellman key exchange on Curve25519 to derive per-link ephemeral keys. Asymmetric, link-less packet communication can also provide forward secrecy, with automatic key ratcheting, by enabling ratchets on a per-destination basis. The multi-hop transport, coordination, verification and reliability layers are fully autonomous and also based on elliptic curve cryptography. 

Reticulum also offers symmetric key encryption for group-oriented communications, as well as unencrypted packets (for local broadcast purposes **only** ). 

Reticulum can connect to a variety of interfaces such as radio modems, data radios and serial ports, and offers the possibility to easily tunnel Reticulum traffic over IP links such as the Internet or private IP networks. 

## **6.3.1 Destinations** 

To receive and send data with the Reticulum stack, an application needs to create one or more destinations. Reticulum uses three different basic destination types, and one special: 

## • **Single** 

The _single_ destination type is the most common type in Reticulum, and should be used for most purposes. It is always identified by a unique public key. Any data sent to this destination will be encrypted using ephemeral keys derived from an ECDH key exchange, and will only be readable by the creator of the destination, who holds the corresponding private key. 

- **Plain** 

A _plain_ destination type is unencrypted, and suited for traffic that should be broadcast to a number of users, or should be readable by anyone. Traffic to a _plain_ destination is not encrypted. Generally, _plain_ destinations can be used for broadcast information intended to be public. Plain destinations are only reachable directly, and packets addressed to plain destinations are never transported over multiple hops in the network. To be transportable over multiple hops in Reticulum, information _must_ be encrypted, since Reticulum uses the per-packet encryption to verify routing paths and keep them alive. 

## • **Group** 

The _group_ special destination type, that defines a symmetrically encrypted virtual destination. Data sent to this destination will be encrypted with a symmetric key, and will be readable by anyone in possession of the key, but as with the _plain_ destination type, packets to this type of destination are not currently transported over multiple hops, although a planned upgrade to Reticulum will allow globally reachable _group_ destinations. 

## • **Link** 

A _link_ is a special destination type, that serves as an abstract channel to a _single_ destination, directly connected or over multiple hops. The _link_ also offers reliability and more efficient encryption, forward secrecy, initiator anonymity, and as such can be useful even when a node is directly reachable. It also offers a more capable API and allows easily carrying out requests and responses, large data transfers and more. 

**6.3. Introduction & Basic Functionality** 

**69** 

**Reticulum Network Stack, Release 1.3.0** 

## **Destination Naming** 

Destinations are created and named in an easy to understand dotted notation of _aspects_ , and represented on the network as a hash of this value. The hash is a SHA-256 truncated to 128 bits. The top level aspect should always be a unique identifier for the application using the destination. The next levels of aspects can be defined in any way by the creator of the application. 

Aspects can be as long and as plentiful as required, and a resulting long destination name will not impact efficiency, as names are always represented as truncated SHA-256 hashes on the network. 

As an example, a destination for a environmental monitoring application could be made up of the application name, a device type and measurement type, like this: 

```
appname:environmentlogger
aspects:remotesensor,temperature
fullname:environmentlogger.remotesensor.temperature
hash:4faf1b2e0a077e6a9d92fa051f256038
```

For the _single_ destination, Reticulum will automatically append the associated public key as a destination aspect before hashing. This is done to ensure only the correct destination is reached, since anyone can listen to any destination name. Appending the public key ensures that a given packet is only directed at the destination that holds the corresponding private key to decrypt the packet. 

**Take note!** There is a very important concept to understand here: 

- Anyone can use the destination name `environmentlogger.remotesensor.temperature` 

- Each destination that does so will still have a unique destination hash, and thus be uniquely addressable, because their public keys will differ. 

In actual use of _single_ destination naming, it is advisable not to use any uniquely identifying features in aspect naming. Aspect names should be general terms describing what kind of destination is represented. The uniquely identifying aspect is always achieved by appending the public key, which expands the destination into a uniquely identifiable one. Reticulum does this automatically. 

Any destination on a Reticulum network can be addressed and reached simply by knowing its destination hash (and public key, but if the public key is not known, it can be requested from the network simply by knowing the destination hash). The use of app names and aspects makes it easy to structure Reticulum programs and makes it possible to filter what information and data your program receives. 

To recap, the different destination types should be used in the following situations: 

- **Single** 

When private communication between two endpoints is needed. Supports multiple hops. 

- **Group** 

When private communication between two or more endpoints is needed. Supports multiple hops indirectly, but must first be established through a _single_ destination. 

- **Plain** 

When plain-text communication is desirable, for example when broadcasting information, or for local discovery purposes. 

To communicate with a _single_ destination, you need to know its public key. Any method for obtaining the public key is valid, but Reticulum includes a simple mechanism for making other nodes aware of your destinations public key, called the _announce_ . It is also possible to request an unknown public key from the network, as all transport instances serve as a distributed ledger of public keys. 

Note that public key information can be shared and verified in other ways than using the built-in _announce_ functionality, and that it is therefore not required to use the _announce_ and _path request_ functionality to obtain public keys. It is by 

**Chapter 6. Understanding Reticulum** 

**70** 

**Reticulum Network Stack, Release 1.3.0** 

far the easiest though, and should definitely be used if there is not a very good reason for doing it differently. 

## **6.3.2 Public Key Announcements** 

An _announce_ will send a special packet over any relevant interfaces, containing all needed information about the destination hash and public key, and can also contain some additional, application specific data. The entire packet is signed by the sender to ensure authenticity. It is not required to use the announce functionality, but in many cases it will be the simplest way to share public keys on the network. The announce mechanism also serves to establish end-to-end connectivity to the announced destination, as the announce propagates through the network. 

As an example, an announce in a simple messenger application might contain the following information: 

- The announcers destination hash 

- The announcers public key 

- Application specific data, in this case the users nickname and availability status 

- A random blob, making each new announce unique 

- An Ed25519 signature of the above information, verifying authenticity 

With this information, any Reticulum node that receives it will be able to reconstruct an outgoing destination to securely communicate with that destination. You might have noticed that there is one piece of information lacking to reconstruct full knowledge of the announced destination, and that is the aspect names of the destination. These are intentionally left out to save bandwidth, since they will be implicit in almost all cases. The receiving application will already know them. If a destination name is not entirely implicit, information can be included in the application specific data part that will allow the receiver to infer the naming. 

It is important to note that announces will be forwarded throughout the network according to a certain pattern. This will be detailed in the section _The Announce Mechanism in Detail_ . 

In Reticulum, destinations are allowed to move around the network at will. This is very different from protocols such as IP, where an address is always expected to stay within the network segment it was assigned in. This limitation does not exist in Reticulum, and any destination is _completely portable_ over the entire topography of the network, and _can even be moved to other Reticulum networks_ than the one it was created in, and still become reachable. To update its reachability, a destination simply needs to send an announce on any networks it is part of. After a short while, it will be globally reachable in the network. 

Seeing how _single_ destinations are always tied to a private/public key pair leads us to the next topic. 

## **6.3.3 Identities** 

In Reticulum, an _identity_ does not necessarily represent a personal identity, but is an abstraction that can represent any kind of _verifiable entity_ . This could very well be a person, but it could also be the control interface of a machine, a program, robot, computer, sensor or something else entirely. In general, any kind of agent that can act, or be acted upon, or store or manipulate information, can be represented as an identity. An _identity_ can be used to create any number of destinations. 

A _single_ destination will always have an _identity_ tied to it, but not _plain_ or _group_ destinations. Destinations and identities share a multilateral connection. You can create a destination, and if it is not connected to an identity upon creation, it will just create a new one to use automatically. This may be desirable in some situations, but often you will probably want to create the identity first, and then use it to create new destinations. 

As an example, we could use an identity to represent the user of a messaging application. Destinations can then be created by this identity to allow communication to reach the user. In all cases it is of great importance to store the private keys associated with any Reticulum Identity securely and privately, since obtaining access to the identity keys equals obtaining access and controlling reachability to any destinations created by that identity. 

**6.3. Introduction & Basic Functionality** 

**71** 

**Reticulum Network Stack, Release 1.3.0** 

## **6.3.4 Getting Further** 

The above functions and principles form the core of Reticulum, and would suffice to create functional networked applications in local clusters, for example over radio links where all interested nodes can directly hear each other. But to be truly useful, we need a way to direct traffic over multiple hops in the network. 

In the following sections, two concepts that allow this will be introduced, _paths_ and _links_ . 

## **6.4 Reticulum Transport** 

The methods of routing used in traditional networks are fundamentally incompatible with the physical medium types and circumstances that Reticulum was designed to handle. These mechanisms mostly assume trust at the physical layer, and often needs a lot more bandwidth than Reticulum can assume is available. Since Reticulum is designed to survive running over open radio spectrum, no such trust can be assumed, and bandwidth is often very limited. 

To overcome such challenges, Reticulum’s _Transport_ system uses asymmetric elliptic curve cryptography to implement the concept of _paths_ that allow discovery of how to get information closer to a certain destination. It is important to note that no single node in a Reticulum network knows the complete path to a destination. Every Transport node participating in a Reticulum network will only know the most direct way to get a packet one hop closer to it’s destination. 

## **6.4.1 Node Types** 

Currently, Reticulum distinguishes between two types of network nodes. All nodes on a Reticulum network are _Reticulum Instances_ , and some are also _Transport Nodes_ . If a system running Reticulum is fixed in one place, and is intended to be kept available most of the time, it is a good contender to be a _Transport Node_ . 

Any Reticulum Instance can become a Transport Node by enabling it in the configuration. This distinction is made by the user configuring the node, and is used to determine what nodes on the network will help forward traffic, and what nodes rely on other nodes for wider connectivity. 

If a node is an _Instance_ it should be given the configuration directive `enable_transport = No` , which is the default setting. 

If it is a _Transport Node_ , it should be given the configuration directive `enable_transport = Yes` . 

## **6.4.2 The Announce Mechanism in Detail** 

When an _announce_ for a destination is transmitted by a Reticulum instance, it will be forwarded by any transport node receiving it, but according to some specific rules: 

- If this exact announce has already been received before, ignore it. 

- If not, record into a table which Transport Node the announce was received from, and how many times in total it has been retransmitted to get here. 

- If the announce has been retransmitted _m+1_ times, it will not be forwarded any more. By default, _m_ is set to 128. 

- After a randomised delay, the announce will be retransmitted on all interfaces that have bandwidth available for processing announces. By default, the maximum bandwidth allocation for processing announces is set at 2%, but can be configured on a per-interface basis. 

- If any given interface does not have enough bandwidth available for retransmitting the announce, the announce will be assigned a priority inversely proportional to its hop count, and be inserted into a queue managed by the interface. 

- When the interface has bandwidth available for processing an announce, it will prioritise announces for destinations that are closest in terms of hops, thus prioritising reachability and connectivity of local nodes, even on slow networks that connect to wider and faster networks. 

**Chapter 6. Understanding Reticulum** 

**72** 

**Reticulum Network Stack, Release 1.3.0** 

- After the announce has been re-transmitted, and if no other nodes are heard retransmitting the announce with a greater hop count than when it left this node, transmitting it will be retried _r_ times. By default, _r_ is set to 1. 

- If a newer announce from the same destination arrives, while an identical one is already waiting to be transmitted, the newest announce is discarded. If the newest announce contains different application specific data, it will replace the old announce. 

Once an announce has reached a transport node in the network, any other node in direct contact with that transport node will be able to reach the destination the announce originated from, simply by sending a packet addressed to that destination. Any transport node with knowledge of the announce will be able to direct the packet towards the destination by looking up the most efficient next node to the destination. 

According to these rules, an announce will propagate throughout the network in a predictable way, and make the announced destination reachable in a short amount of time. Fast networks that have the capacity to process many announces can reach full convergence very quickly, even when constantly adding new destinations. Slower segments of such networks might take a bit longer to gain full knowledge about the wide and fast networks they are connected to, but can still do so over time, while prioritising full and quickly converging end-to-end connectivity for their local, slower segments. 

## **Tip** 

Even very slow networks, that simply don’t have the capacity to ever reach _full_ convergence will generally still be able to reach **any other destination on any connected segments** , since interconnecting transport nodes will prioritize announces into the slower segments that are actually requested by nodes on these. 

This means that slow, low-capacity or low-resource segments **don’t** need to have full network knowledge, since paths can always be recursively resolved from other segments that do have knowledge about them. 

In general, even extremely complex networks, that utilize the maximum 128 hops will converge to full end-to-end connectivity in about one minute, given there is enough bandwidth available to process the required amount of announces. 

## **6.4.3 Reaching the Destination** 

In networks with changing topology and trustless connectivity, nodes need a way to establish _verified connectivity_ with each other. Since the underlying network mediums are assumed to be trustless, Reticulum must provide a way to guarantee that the peer you are communicating with is actually who you expect. Reticulum offers two ways to do this. 

For exchanges of small amounts of information, Reticulum offers the _Packet_ API, which works exactly like you would expect - on a per packet level. The following process is employed when sending a packet: 

- A packet is always created with an associated destination and some payload data. When the packet is sent to a _single_ destination type, Reticulum will automatically create an ephemeral encryption key, perform an ECDH key exchange with the destination’s public key (or ratchet key, if available), and encrypt the information. 

- It is important to note that this key exchange does not require any network traffic. The sender already knows the public key of the destination from an earlier received announce, and can thus perform the ECDH key exchange locally, before sending the packet. 

- The public part of the newly generated ephemeral key-pair is included with the encrypted token, and sent along with the encrypted payload data in the packet. 

- When the destination receives the packet, it can itself perform an ECDH key exchange and decrypt the packet. 

- A new ephemeral key is used for every packet sent in this way. 

- Once the packet has been received and decrypted by the addressed destination, that destination can opt to _prove_ its receipt of the packet. It does this by calculating the SHA-256 hash of the received packet, and signing this hash with its Ed25519 signing key. Transport nodes in the network can then direct this _proof_ back to the packets origin, where the signature can be verified against the destination’s known public signing key. 

**6.4. Reticulum Transport** 

**73** 

**Reticulum Network Stack, Release 1.3.0** 

- In case the packet is addressed to a _group_ destination type, the packet will be encrypted with the pre-shared AES-256 key associated with the destination. In case the packet is addressed to a _plain_ destination type, the payload data will not be encrypted. Neither of these two destination types can offer forward secrecy. In general, it is recommended to always use the _single_ destination type, unless it is strictly necessary to use one of the others. 

For exchanges of larger amounts of data, or when longer sessions of bidirectional communication is desired, Reticulum offers the _Link_ API. To establish a _link_ , the following process is employed: 

- First, the node that wishes to establish a link will send out a _link request_ packet, that traverses the network and locates the desired destination. Along the way, the Transport Nodes that forward the packet will take note of this _link request_ , and mark it as pending. 

- Second, if the destination accepts the _link request_ , it will send back a packet that proves the authenticity of its identity (and the receipt of the link request) to the initiating node. All nodes that initially forwarded the packet will also be able to verify this proof, and thus accept the validity of the _link_ throughout the network. The link is now marked as _established_ . 

- When the validity of the _link_ has been accepted by forwarding nodes, these nodes will remember the _link_ , and it can subsequently be used by referring to a hash representing it. 

- As a part of the _link request_ , an Elliptic Curve Diffie-Hellman key exchange takes place, that sets up an efficiently encrypted tunnel between the two nodes. As such, this mode of communication is preferred, even for situations when nodes can directly communicate, when the amount of data to be exchanged numbers in the tens of packets, or whenever the use of the more advanced API functions is desired. 

- When a _link_ has been set up, it automatically provides message receipt functionality, through the same _proof_ mechanism discussed before, so the sending node can obtain verified confirmation that the information reached the intended recipient. 

- Once the _link_ has been set up, the initiator can remain anonymous, or choose to authenticate towards the destination using a Reticulum Identity. This authentication is happening inside the encrypted link, and is only revealed to the verified destination, and no intermediaries. 

In a moment, we will discuss the details of how this methodology is implemented, but let’s first recap what purposes this methodology serves. We first ensure that the node answering our request is actually the one we want to communicate with, and not a malicious actor pretending to be so. At the same time we establish an efficient encrypted channel. The setup of this is relatively cheap in terms of bandwidth, so it can be used just for a short exchange, and then recreated as needed, which will also rotate encryption keys. The link can also be kept alive for longer periods of time, if this is more suitable to the application. The procedure also inserts the _link id_ , a hash calculated from the link request packet, into the memory of forwarding nodes, which means that the communicating nodes can thereafter reach each other simply by referring to this _link id_ . 

The combined bandwidth cost of setting up a link is 3 packets totalling 297 bytes (more info in the _Binary Packet Format_ section). The amount of bandwidth used on keeping a link open is practically negligible, at 0.45 bits per second. Even on a slow 1200 bits per second packet radio channel, 100 concurrent links will still leave 96% channel capacity for actual data. 

## **Link Establishment in Detail** 

After exploring the basics of the announce mechanism, finding a path through the network, and an overview of the link establishment procedure, this section will go into greater detail about the Reticulum link establishment process. 

The _link_ in Reticulum terminology should not be viewed as a direct node-to-node link on the physical layer, but as an abstract channel, that can be open for any amount of time, and can span an arbitrary number of hops, where information will be exchanged between two nodes. 

- When a node in the network wants to establish verified connectivity with another node, it will randomly generate a new X25519 private/public key pair. It then creates a _link request_ packet, and broadcast it. 

**Chapter 6. Understanding Reticulum** 

**74** 

**Reticulum Network Stack, Release 1.3.0** 

_It should be noted that the X25519 public/private keypair mentioned above is two separate keypairs: An encryption key pair, used for derivation of a shared symmetric key, and a signing key pair, used for signing and verifying messages on the link. They are sent together over the wire, and can be considered as single public key for simplicity in this explanation._ 

- The _link request_ is addressed to the destination hash of the desired destination, and contains the following data: The newly generated X25519 public key _LKi_ . 

- The broadcasted packet will be directed through the network according to the rules laid out previously. 

- Any node that forwards the link request will store a _link id_ in it’s _link table_ , along with the amount of hops the packet had taken when received. The link id is a hash of the entire link request packet. If the link request packet is not _proven_ by the addressed destination within some set amount of time, the entry will be dropped from the _link table_ again. 

- When the destination receives the link request packet, it will decide whether to accept the request. If it is accepted, the destination will also generate a new X25519 private/public key pair, and perform a Diffie Hellman Key Exchange, deriving a new symmetric key that will be used to encrypt the channel, once it has been established. 

- A _link proof_ packet is now constructed and transmitted over the network. This packet is addressed to the _link id_ of the _link_ . It contains the following data: The newly generated X25519 public key _LKr_ and an Ed25519 signature of the _link id_ and _LKr_ made by the _original signing key_ of the addressed destination. 

- By verifying this _link proof_ packet, all nodes that originally transported the _link request_ packet to the destination from the originator can now verify that the intended destination received the request and accepted it, and that the path they chose for forwarding the request was valid. In successfully carrying out this verification, the transporting nodes marks the link as active. An abstract bi-directional communication channel has now been established along a path in the network. Packets can now be exchanged bi-directionally from either end of the link simply by adressing the packets to the _link id_ of the link. 

- When the source receives the _proof_ , it will know unequivocally that a verified path has been established to the destination. It can now also use the X25519 public key contained in the _link proof_ to perform it’s own Diffie Hellman Key Exchange and derive the symmetric key that is used to encrypt the channel. Information can now be exchanged reliably and securely. 

## **Note** 

It’s important to note that this methodology ensures that the source of the request does not need to reveal any identifying information about itself. **The link initiator remains completely anonymous** . 

When using _links_ , Reticulum will automatically verify all data sent over the link, and can also automate retransmissions if _Resources_ are used. 

## **6.4.4 Resources** 

For exchanging small amounts of data over a Reticulum network, the _Packet_ interface is sufficient, but for exchanging data that would require many packets, an efficient way to coordinate the transfer is needed. 

This is the purpose of the Reticulum _Resource_ . A _Resource_ can automatically handle the reliable transfer of an arbitrary amount of data over an established _Link_ . Resources can auto-compress data, will handle breaking the data into individual packets, sequencing the transfer, integrity verification and reassembling the data on the other end. 

_Resources_ are programmatically very simple to use, and only requires a few lines of codes to reliably transfer any amount of data. They can be used to transfer data stored in memory, or stream data directly from files. 

**6.4. Reticulum Transport** 

**75** 

**Reticulum Network Stack, Release 1.3.0** 

## **6.5 Network Identities** 

In Reticulum, every peer and application utilizes a cryptographic **Identity** to verify authenticity and establish encrypted channels. While standard identities are typically used to represent a single user, device, or service, Reticulum introduces the concept of a **Network Identity** to represent a logical group of nodes or an entire community infrastructure. 

A Network Identity is, at its core, a standard Reticulum Identity keyset. However, its purpose and usage differ from a personal identity. Instead of identifying a single entity, a Network Identity acts as a shared credential that federates multiple independent Transport Instances under a single, verifiable administrative domain. 

## **6.5.1 Conceptual Overview** 

You can think of a standard Reticulum Identity as a self-sovereign, privately created passport for a single person. A Network Identity, conversely, is akin to a cryptographic flag, or a charter that flies over a fleet of ships. It signifies that while the ships may operate independently and be physically distant, they belong to the same organization, follow the same protocols, and are expected to act in concert. 

When you configure a Network Identity on one or more of your nodes, you are effectively declaring that these nodes constitute a specific “network” within a broader Reticulum mesh. This allows other peers to recognize interfaces not just as “a node named Alice”, but as “a gateway belonging to The Eastern Ret Of Freedom”. 

## **6.5.2 Current Usage** 

At present, the primary function of a Network Identity is within the _Interface Discovery_ system. 

When a Transport Instance broadcasts a discovery announce for an interface, it can optionally sign that announce with a Network Identity, instead of just its local transport identity. Remote peers receiving the announce can then verify the signature. This provides functionality for two important distinctions: 

1. **Authenticity:** It proves that the interface was published by an operator who possesses the private key for that Network Identity. 

2. **Trust Boundaries:** It allows users to configure their systems to only accept and connect to interfaces that belong to specific Network Identities, effectively creating “whitelisted” zones of trusted infrastructure. 

## **Note** 

If you enable encryption on your discovery announces, the Network Identity is used as the shared secret. Only peers who have been explicitly provided with the Network Identity’s full keyset (and have it configured locally) will be able to decrypt and utilize the connection details. 

This functionality will be expanded in the future, so that peers with delegated keys can be allowed to decrypt discovery announces without holding the root network key. Currently, the functionality is sufficient for sharing interface information privately where you control all nodes that must decrypt the discovered interfaces. 

## **6.5.3 Future Implications** 

While the current implementation focuses on interface discovery, the concept of Network Identities serves as the foundational building block for future Reticulum features designed to support large-scale, organic mesh formation. 

As the ecosystem evolves, Network Identities will facilitate: 

- **Distributed Name Resolution:** A system where networks can publish name-to-identity mappings, allowing human-readable names to resolve without centralized servers. 

- **Service Publishing:** Networks will be able to announce specific capabilities, services, or information endpoints available publicly or to their members. 

**Chapter 6. Understanding Reticulum** 

**76** 

**Reticulum Network Stack, Release 1.3.0** 

- **Inter-Network Federation:** Trust relationships between different networks, allowing for seamless but managed flow of traffic and information across distinct administrative boundaries. 

- **Distributed Blackhole Management:** A reputation-based system for blackhole list distribution, where trusted Network Identities can sign and publish lists of blackholed identities. This allows communities to collaboratively enforce security standards and filter spam or malicious identities across the parts of the wider mesh that they are responsible for. 

By adopting the use of Network Identities now, you are preparing your infrastructure to be compatible with this future functionality. 

## **6.5.4 Creating and Using a Network Identity** 

Since a Network Identity is simply a standard Reticulum Identity, you create one using the built-in tools. 

1. **Generate the Identity:** Use the `rnid` utility to generate a new identity file that will serve as your Network Identity. 

```
$rnid-g~/.reticulum/storage/identities/my_network
```

2. **Distribute the Public Key:** The public key must be distributed to any Transport Instance that needs to verify your network’s announces and discovery information. By default, if your node is set up to use a network identity, this happens automatically (using the standard announce mechanism). 

3. **Configure Instances:** In the `[reticulum]` section of the configuration file on every node within your network, point the `network_identity` option to the file you created. 

```
[reticulum]
...
network_identity=~/.reticulum/storage/identities/my_network
...
```

Once configured, your instances will automatically utilize this identity for signing discovery announces (and potentially decrypting network-private information), presenting a unified front to the wider network. 

## **6.6 Reference Setup** 

This section will detail a recommended _Reference Setup_ for Reticulum. It is important to note that Reticulum is designed to be usable on more or less any computing device, and over more or less any medium that allows you to send and receive data, which satisfies some very low minimum requirements. 

The communication channel must support at least half-duplex operation, and provide an average throughput of 5 bits per second or greater, and supports a physical layer MTU of 500 bytes. The Reticulum stack should be able to run on more or less any hardware that can provide a Python 3.x runtime environment. 

That being said, this reference setup has been outlined to provide a common platform for anyone who wants to help in the development of Reticulum, and for everyone who wants to know a recommended setup to get started experimenting. A reference system consists of three parts: 

- **An Interface Device** 

Which provides access to the physical medium whereupon the communication takes place, for example a radio with an integrated modem. A setup with a separate modem connected to a radio would also be an interface device. 

- **A Host Device** 

Some sort of computing device that can run the necessary software, communicate with the interface device, and provide user interaction. 

**6.6. Reference Setup** 

**77** 

**Reticulum Network Stack, Release 1.3.0** 

## • **A Software Stack** 

The software implementing the Reticulum protocol and applications using it. 

The reference setup can be considered a relatively stable platform to develop on, and also to start building networks or applications on. While details of the implementation might change at the current stage of development, it is the goal to maintain hardware compatibility for as long as entirely possible, and the current reference setup has been determined to provide a functional platform for many years into the future. The current Reference System Setup is as follows: 

## • **Interface Device** 

A data radio consisting of a LoRa radio module, and a microcontroller with open source firmware, that can connect to host devices via USB. It operates in either the 430, 868 or 900 MHz frequency bands. More details can be found on the RNode Page. 

## • **Host Device** 

Any computer device running Linux and Python. A Raspberry Pi with a Debian based OS is a good place to start, but anything can be used. 

## • **Software Stack** 

The most recently released Python Implementation of Reticulum, running on a Linux-based operating system. 

## **Note** 

To avoid confusion, it is very important to note, that the reference interface device **does not** use the LoRaWAN standard, but uses a custom MAC layer on top of the plain LoRa modulation! As such, you will need a plain LoRa radio module connected to a controller with the correct firmware. Full details on how to get or make such a device is available on the RNode Page. 

With the current reference setup, it should be possible to get on a Reticulum network for around 100$ even if you have none of the hardware already, and need to purchase everything. 

This reference setup is of course just a recommendation for getting started easily, and you should tailor it to your own specific needs, or whatever hardware you have available. 

## **6.7 Protocol Specifics** 

This chapter will detail protocol specific information that is essential to the implementation of Reticulum, but noncritical in understanding how the protocol works on a general level. It should be treated more as a reference than as essential reading. 

## **6.7.1 Packet Prioritisation** 

Currently, Reticulum is completely priority-agnostic regarding _general_ traffic. All traffic is handled on a first-come, first-serve basis. Announce re-transmission and other maintenance traffic is handled according to the re-transmission times and priorities described earlier in this chapter. 

## **6.7.2 Interface Access Codes** 

Reticulum can create named virtual networks, and networks that are only accessible by knowing a preshared passphrase. The configuration of this is detailed in the _Common Interface Options_ section. To implement this feature, Reticulum uses the concept of Interface Access Codes, that are calculated and verified per-packet. 

An interface with a named virtual network or passphrase authentication enabled will derive a shared Ed25519 signing identity, and for every outbound packet generate a signature of the entire packet. This signature is then inserted into the packet as an Interface Access Code before transmission. Depending on the speed and capabilities of the interface, 

**Chapter 6. Understanding Reticulum** 

**78** 

**Reticulum Network Stack, Release 1.3.0** 

the IFAC can be the full 512-bit Ed25519 signature, or a truncated version. Configured IFAC length can be inspected for all interfaces with the `rnstatus` utility. 

Upon receipt, the interface will check that the signature matches the expected value, and drop the packet if it does not. This ensures that only packets sent with the correct naming and/or passphrase parameters are allowed to pass onto the network. 

## **6.7.3 Wire Format** 

- `== Reticulum Wire Format ======` 

```
AReticulumpacketiscomposedofthefollowingfields:
```

- `[HEADER 2 bytes] [ADDRESSES 16/32 bytes] [CONTEXT 1 byte] [DATA 0-465 bytes]` 

- `The HEADER field is 2 bytes long.` 

   - `Byte 1: [IFAC Flag], [Header Type], [Context Flag], [Propagation Type], [Destination Type] and [Packet Type]` 

   - `Byte 2: Number of hops` 

- `Interface Access Code field if the IFAC flag was set.` 

   - `The length of the Interface Access Code can vary from 1 to 64 bytes according to physical interface capabilities and configuration.` 

- `The ADDRESSES field contains either 1 or 2 addresses.` 

   - `Each address is 16 bytes long.` 

   - `The Header Type flag in the HEADER field determines whether the ADDRESSES field contains 1 or 2 addresses.` 

   - `Addresses are SHA-256 hashes truncated to 16 bytes.` 

- `The CONTEXT field is 1 byte.` 

   - `It is used by Reticulum to determine packet context.` 

- `The DATA field is between 0 and 465 bytes.` 

   - `It contains the packets data payload.` 

```
IFACFlag
```

```
-----------------
open0Packetforpublicallyaccessibleinterface
authenticated1Interfaceauthenticationisincludedinpacket
HeaderTypes
-----------------
type10Twobyteheader,one16byteaddressfield
type21Twobyteheader,two16byteaddressfields
ContextFlag
-----------------
unset0Thecontextflagisusedforvarioustypes
set1ofsignalling,dependingonpacketcontext
```

(continues on next page) 

**6.7. Protocol Specifics** 

**79** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
PropagationTypes
-----------------
broadcast0
transport1
DestinationTypes
-----------------
single00
group01
plain10
link11
PacketTypes
-----------------
data00
announce01
linkrequest10
proof11
+-PacketExample-+
HEADERFIELDDESTINATIONFIELDSCONTEXTFIELDDATAFIELD
_______|_______________________|________________________|________|_
||||||||
0101000000000100[HASH1,16bytes][HASH2,16bytes][CONTEXT,1byte][DATA]
||||||
|||||+--Hops=4
||||+-------PacketType=DATA
|||+---------DestinationType=SINGLE
||+-----------PropagationType=TRANSPORT
|+-------------HeaderType=HEADER_2(twobyteheader,twoaddressfields)
+--------------AccessCodes=DISABLED
+-PacketExample-+
HEADERFIELDDESTINATIONFIELDCONTEXTFIELDDATAFIELD
_______|______________|_______________|________|_
||||||||
0000000000000111[HASH1,16bytes][CONTEXT,1byte][DATA]
||||||
|||||+--Hops=7
||||+-------PacketType=DATA
|||+---------DestinationType=SINGLE
||+-----------PropagationType=BROADCAST
|+-------------HeaderType=HEADER_1(twobyteheader,oneaddressfield)
+--------------AccessCodes=DISABLED
```

(continues on next page) 

**Chapter 6. Understanding Reticulum** 

**80** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
+-PacketExample-+
HEADERFIELDIFACFIELDDESTINATIONFIELDCONTEXTFIELDDATAFIELD
_______|_____________|_____________|_______________|________|_
||||||||||
1000000000000111[IFAC,Nbytes][HASH1,16bytes][CONTEXT,1byte][DATA]
||||||
|||||+--Hops=7
||||+-------PacketType=DATA
|||+---------DestinationType=SINGLE
||+-----------PropagationType=BROADCAST
|+-------------HeaderType=HEADER_1(twobyteheader,oneaddressfield)
+--------------AccessCodes=ENABLED
Sizeexamplesofdifferentpackettypes
---------------------------------------
Thefollowingtablelistsexamplesizesofvarious
packettypes.Thesizelistedarethecompleteon-
wiresizecountingallfieldsincludingheaders,
butexcludinganyinterfaceaccesscodes.
-PathRequest:51bytes
-Announce:167bytes
-LinkRequest:83bytes
-LinkProof:115bytes
-LinkRTTpacket:99bytes
-Linkkeepalive:20bytes
```

## **6.7.4 Announce Propagation Rules** 

The following table illustrates the rules for automatically propagating announces from one interface type to another, for all possible combinations. For the purpose of announce propagation, the _Full_ and _Gateway_ modes are identical. 

**6.7. Protocol Specifics** 

**81** 

**Reticulum Network Stack, Release 1.3.0** 

**==> picture [469 x 349] intentionally omitted <==**

See the _Interface Modes_ section for a conceptual overview of the different interface modes, and how they are configured. 

## **6.7.5 Cryptographic Primitives** 

Reticulum uses a simple suite of efficient, strong and well-tested cryptographic primitives, with widely available implementations that can be used both on general-purpose CPUs and on microcontrollers. 

One of the primary considerations for choosing this particular set of primitives is that they can be implemented _safely_ with relatively few pitfalls, on practically all current computing platforms. 

The primitives listed here **are authoritative** . Anything claiming to be Reticulum, but not using these exact primitives **is not** Reticulum, and possibly an intentionally compromised or weakened clone. The utilised primitives are: 

- Ed25519 for signatures 

- X25519 for ECDH key exchanges 

- HKDF for key derivation 

- Encrypted tokens are based on the Fernet spec 

   - Ephemeral keys derived from an ECDH key exchange on Curve25519 

   - AES-256 in CBC mode with PKCS7 padding 

   - HMAC using SHA256 for message authentication 

   - IVs must be generated through `os.urandom()` or better 

   - No Fernet version and timestamp metadata fields 

**Chapter 6. Understanding Reticulum** 

**82** 

**Reticulum Network Stack, Release 1.3.0** 

- SHA-256 

- SHA-512 

In the default installation configuration, the `X25519` , `Ed25519` and `AES-256-CBC` primitives are provided by OpenSSL (via the PyCA/cryptography package). The hashing functions `SHA-256` and `SHA-512` are provided by the standard Python hashlib. The `HKDF` , `HMAC` , `Token` primitives, and the `PKCS7` padding function are always provided by the following internal implementations: 

- `RNS/Cryptography/HKDF.py` 

- `RNS/Cryptography/HMAC.py` 

- `RNS/Cryptography/Token.py` 

- `RNS/Cryptography/PKCS7.py` 

Reticulum also includes a complete implementation of all necessary primitives in pure Python. If OpenSSL & PyCA are not available on the system when Reticulum is started, Reticulum will instead use the internal pure-python primitives. A trivial consequence of this is performance, with the OpenSSL backend being _much_ faster. The most important consequence however, is the potential loss of security by using primitives that has not seen the same amount of scrutiny, testing and review as those from OpenSSL. 

Using the normal RNS installation procedures, it is not possible to install Reticulum on a system without the required OpenSSL primitives being available, and if they are not, they will be resolved and installed as a dependency. It is only possible to use the pure-python primitives by manually specifying this, for example by using the `rnspure` package. 

## **Warning** 

If you want to use the internal pure-python primitives, it is **highly advisable** that you have a good understanding of the risks that this pose, and make an informed decision on whether those risks are acceptable to you. 

**6.7. Protocol Specifics** 

**83** 

**Reticulum Network Stack, Release 1.3.0** 

**Chapter 6. Understanding Reticulum** 

**84** 

**CHAPTER SEVEN** 

## **COMMUNICATIONS HARDWARE** 

One of the truly valuable aspects of Reticulum is the ability to use it over almost any conceivable kind of communications medium. The _interface types_ available for configuration in Reticulum are flexible enough to cover the use of most wired and wireless communications hardware available, from decades-old packet radio modems to modern millimeter-wave backhaul systems. 

If you already have or operate some kind of communications hardware, there is a very good chance that it will work with Reticulum out of the box. In case it does not, it is possible to provide the necessary glue with very little effort using for example the _PipeInterface_ or the _TCPClientInterface_ in combination with code like TCP KISS Server by simplyequipped. 

It is also very easy to write and load _custom interface modules_ into Reticulum, allowing you to communicate with more or less anything you can think of. 

While this broad support and flexibility is very useful, an abundance of options can sometimes make it difficult to know where to begin, especially when you are starting from scratch. 

This chapter will outline a few different sensible starting paths to get real-world functional wireless communications up and running with minimal cost and effort. Two fundamental devices categories will be covered, _RNodes_ and _WiFi-based radios_ . Additionally, other common options will be briefly described. 

Knowing how to employ just a few different types of hardware will make it possible to build a wide range of useful networks with little effort. 

## **7.1 Combining Hardware Types** 

It is useful to combine different link and hardware types when designing and building a network. One useful design pattern is to employ high-capacity point-to-point links based on WiFi or millimeter-wave radios (with high-gain directional antennas) for the network backbone, and using LoRa-based RNodes for covering large areas with connectivity for client devices. 

## **7.2 RNode** 

Reliable and general-purpose long-range digital radio transceiver systems are commonly either very expensive, difficult to set up and operate, hard to source, power-hungry, or all of the above at the same time. In an attempt to alleviate this situation, the transceiver system _RNode_ was designed. It is important to note that RNode is not one specific device, from one particular vendor, but _an open plaform_ that anyone can use to build interoperable digital transceivers suited to their needs and particular situations. 

An RNode is a general purpose, interoperable, low-power and long-range, reliable, open and flexible radio communications device. Depending on its components, it can operate on many different frequency bands, and use many different modulation schemes, but most commonly, and for the purposes of this chapter, we will limit the discussion to RNodes using _LoRa_ modulation in common ISM bands. 

**85** 

**Reticulum Network Stack, Release 1.3.0** 

**Avoid Confusion!** RNodes can use LoRa as a _physical-layer modulation_ , but it does not use, and has nothing to do with the _LoRaWAN_ protocol and standard, commonly used for centrally controlled IoT devices. RNodes use _raw LoRa modulation_ , without any additional protocol overhead. All high-level protocol functionality is handled directly by Reticulum. 

## **7.2.1 Creating RNodes** 

RNode has been designed as a system that is easy to replicate across time and space. You can put together a functioning transceiver using commonly available components, and a few open source software tools. While you can design and build RNodes completely from scratch, to your exact desired specifications, this chapter will explain the easiest possible approach to creating RNodes: Using common LoRa development boards. This approach can be boiled down to two simple steps: 

1. Obtain one or more _supported development boards_ 

2. Install the RNode firmware with the _automated installer_ 

Once the firmware has been installed and provisioned by the install script, it is ready to use with any software that supports RNodes, including Reticulum. The device can be used with Reticulum by adding an _RNodeInterface_ to the configuration. 

## **7.2.2 Supported Boards and Devices** 

To create one or more RNodes, you will need to obtain supported development boards or completed devices. The following boards and devices are supported by the auto-installer. 

**==> picture [352 x 115] intentionally omitted <==**

## **LilyGO T-Beam Supreme** 

- **Transceiver IC** Semtech SX1262 or SX1268 

- **Device Platform** ESP32 

- **Manufacturer** LilyGO 

**Chapter 7. Communications Hardware** 

**86** 

**Reticulum Network Stack, Release 1.3.0** 

**==> picture [352 x 177] intentionally omitted <==**

## **LilyGO T-Beam** 

- **Transceiver IC** Semtech SX1262, SX1268, SX1276 or SX1278 

- **Device Platform** ESP32 

- **Manufacturer** LilyGO 

**==> picture [235 x 134] intentionally omitted <==**

## **LilyGO T3S3** 

- **Transceiver IC** Semtech SX1262, SX1268, SX1276 or SX1278 

- **Device Platform** ESP32 

- **Manufacturer** LilyGO 

**7.2. RNode** 

**87** 

**Reticulum Network Stack, Release 1.3.0** 

**==> picture [212 x 162] intentionally omitted <==**

## **RAK4631-based Boards** 

- **Transceiver IC** Semtech SX1262 or SX1268 

- **Device Platform** nRF52 

- **Manufacturer** RAK Wireless 

**==> picture [212 x 116] intentionally omitted <==**

## **OpenCom XL** 

- **Transceiver ICs** Semtech SX1262 and SX1280 (dual transceiver) 

- **Device Platform** nRF52 

- **Manufacturer** Liberated Embedded Systems 

**==> picture [320 x 77] intentionally omitted <==**

## **Unsigned RNode v2.x** 

- **Transceiver IC** Semtech SX1276 or SX1278 

- **Device Platform** ESP32 

**Chapter 7. Communications Hardware** 

**88** 

**Reticulum Network Stack, Release 1.3.0** 

- **Manufacturer** unsigned.io 

**==> picture [216 x 135] intentionally omitted <==**

## **LilyGO LoRa32 v2.1** 

- **Transceiver IC** Semtech SX1276 or SX1278 

- **Device Platform** ESP32 

- **Manufacturer** LilyGO 

**==> picture [216 x 135] intentionally omitted <==**

## **LilyGO LoRa32 v2.0** 

- **Transceiver IC** Semtech SX1276 or SX1278 

- **Device Platform** ESP32 

- **Manufacturer** LilyGO 

**==> picture [216 x 135] intentionally omitted <==**

**7.2. RNode** 

**89** 

**Reticulum Network Stack, Release 1.3.0** 

## **LilyGO LoRa32 v1.0** 

- **Transceiver IC** Semtech SX1276 or SX1278 

- **Device Platform** ESP32 

- **Manufacturer** LilyGO 

**==> picture [212 x 303] intentionally omitted <==**

## **LilyGO T-Deck** 

- **Transceiver IC** Semtech SX1262 or SX1268 

- **Device Platform** ESP32 

- **Manufacturer** LilyGO 

**==> picture [212 x 93] intentionally omitted <==**

**Chapter 7. Communications Hardware** 

**90** 

**Reticulum Network Stack, Release 1.3.0** 

## **LilyGO T-Echo** 

- **Transceiver IC** Semtech SX1262 or SX1268 

- **Device Platform** nRF52 

- **Manufacturer** LilyGO 

**==> picture [272 x 127] intentionally omitted <==**

## **Heltec T114** 

- **Transceiver IC** Semtech SX1262 or SX1268 

- **Device Platform** nRF52 

- **Manufacturer** Heltec Automation 

**==> picture [272 x 146] intentionally omitted <==**

## **Heltec LoRa32 v4.0** 

- **Transceiver IC** Semtech SX1262 

- **Device Platform** ESP32 

- **Manufacturer** Heltec Automation 

**7.2. RNode** 

**91** 

**Reticulum Network Stack, Release 1.3.0** 

**==> picture [272 x 136] intentionally omitted <==**

## **Heltec LoRa32 v3.0** 

- **Transceiver IC** Semtech SX1262 or SX1268 

- **Device Platform** ESP32 

- **Manufacturer** Heltec Automation 

**==> picture [272 x 137] intentionally omitted <==**

## **Heltec LoRa32 v2.0** 

- **Transceiver IC** Semtech SX1276 or SX1278 

- **Device Platform** ESP32 

- **Manufacturer** Heltec Automation 

## **7.2.3 Installation** 

Once you have obtained compatible boards, you can install the RNode Firmware using the RNode Configuration Utility. If you have installed Reticulum on your system, the `rnodeconf` program will already be available. If not, make sure that `Python3` and `pip` is installed on your system, and then install Reticulum with with `pip` : 

## `pip install rns` 

Once installation has completed, it is time to start installing the firmware on your devices. Run `rnodeconf` in autoinstall mode like so: 

## `rnodeconf --autoinstall` 

The utility will guide you through the installation process by asking a series of questions about your hardware. Simply follow the guide, and the utility will auto-install and configure your devices. 

**Chapter 7. Communications Hardware** 

**92** 

**Reticulum Network Stack, Release 1.3.0** 

## **7.2.4 Usage with Reticulum** 

When the devices have been installed and provisioned, you can use them with Reticulum by adding the _relevant interface section_ to the configuration file of Reticulum. In the configuraion you can specify all interface parameters, such as serial port and on-air parameters. 

## **7.3 WiFi-based Hardware** 

It is possible to use all kinds of both short- and long-range WiFi-based hardware with Reticulum. Any kind of hardware that fully supports bridged Ethernet over the WiFi interface will work with the _AutoInterface_ in Reticulum. Most devices will behave like this by default, or allow it via configuration options. 

This means that you can simply configure the physical links of the WiFi based devices, and start communicating over them using Reticulum. It is not necessary to enable any IP infrastructure such as DHCP servers, DNS or similar, as long as at least Ethernet is available, and packets are passed transparently over the physical WiFi-based devices. 

Below is a list of example WiFi (and similar) radios that work well for high capacity Reticulum links over long distances: 

- Ubiquiti airMAX radios 

- Ubiquiti LTU radios 

- MikroTik radios 

This list is by no means exhaustive, and only serves as a few examples of radio hardware that is relatively cheap while providing long range and high capacity for Reticulum networks. As in all other cases, it is also possible for Reticulum to co-exist with IP networks running concurrently on such devices. 

## **7.4 Ethernet-based Hardware** 

Reticulum can run over any kind of hardware that can provide a switched Ethernet-based medium. This means that anything from a plain Ethernet switch, to fiber-optic systems, to data radios with Ethernet interfaces can be used by Reticulum. 

The Ethernet medium does not need to have any IP infrastructure such as DHCP servers or routing set up, but in case such infrastructure does exist, Reticulum will simply co-exist with. 

To use Reticulum over Ethernet-based mediums, it is generally enough to use the included _AutoInterface_ . This interface also works over any kind of virtual networking adapter, such as `tun` and `tap` devices in Linux. 

## **7.5 Serial Lines & Devices** 

Using Reticulum over any kind of raw serial line is also possible with the _SerialInterface_ . This interface type is also useful for using Reticulum over communications hardware that provides a serial port interface. 

## **7.6 Packet Radio Modems** 

Any packet radio modem that provides a standard KISS interface over USB, serial or TCP can be used with Reticulum. This includes virtual software modems such as FreeDV TNC and Dire Wolf. 

**7.3. WiFi-based Hardware** 

**93** 

**Reticulum Network Stack, Release 1.3.0** 

**Chapter 7. Communications Hardware** 

**94** 

**CHAPTER EIGHT** 

## **CONFIGURING INTERFACES** 

Reticulum supports using many kinds of devices as networking interfaces, and allows you to mix and match them in any way you choose. The number of distinct network topologies you can create with Reticulum is more or less endless, but common to them all is that you will need to define one or more _interfaces_ for Reticulum to use. 

The following sections describe the interfaces currently available in Reticulum, and gives example configurations for the respective interface types. 

For a high-level overview of how networks can be formed over different interface types, have a look at the _Building Networks_ chapter of this manual. 

## **8.1 Custom Interfaces** 

In addition to the built-in interface types, Reticulum is **fully extensible** with custom, user- or community-supplied interfaces, and creating custom interface modules is straightforward. Please see the _custom interface_ example for basic interface code to build upon. 

## **8.2 Auto Interface** 

The `AutoInterface` enables communication with other discoverable Reticulum nodes over any kind of local Ethernet or WiFi-based medium. Even though it uses IPv6 for peer discovery, and UDP for packet transport, it **does not** need any functional IP infrastructure like routers or DHCP servers, on your physical network. 

## **Warning** 

If you have **firewall** software running on your computer, it may block traffic required for `AutoInterface` to work. If this is the case, you will have to allow UDP traffic on port `29716` and `42671` . 

As long as there is at least some sort of switching medium present between peers (a wired switch, a hub, a WiFi access point or similar, or simply two devices connected directly by Ethernet cable), it will work without any configuration, setup or intermediary devices. 

For `AutoInterface` peer discovery to work, it’s also required that link-local IPv6 support is available on your system, which it should be by default in all current operating systems, both desktop and mobile. 

## **Note** 

Almost all current Ethernet and WiFi hardware will work without any kind of configuration or setup with `AutoInterface` , but a small subset of devices turn on options that limit device-to-device communication by de- 

**95** 

**Reticulum Network Stack, Release 1.3.0** 

fault, resulting in `AutoInterface` peer discovery being blocked. This issue is most commonly seen on very cheap, ISP-supplied WiFi routers, and can sometimes be turned off in the router configuration. 

```
#Thisexampledemonstratesabare-minimumsetup
#ofanAutoInterface.Itwillallowcommunica-
#tionwithallotherreachabledevicesonall
#usablephysicalethernet-baseddevicesthat
#areavailableonthesystem.
[[DefaultInterface]]
type=AutoInterface
enabled=yes
```

```
#Thisexampledemonstratesanmorespecifically
#configuredAutoInterface,thatonlyusesspe-
#cificphysicalinterfaces,andhasanumberof
#otherconfigurationoptionsset.
[[DefaultInterface]]
type=AutoInterface
enabled=yes
```

```
#YoucancreatemultipleisolatedReticulum
#networksonthesamephysicalLANby
#specifyingdifferentGroupIDs.
group_id=reticulum
```

```
#Youcanalsochoosethemulticastaddresstype:
#temporary(default,TemporaryMulticastAddress)
#orpermanent(PermanentMulticastAddress)
multicast_address_type=permanent
```

```
#Youcanalsoselectspecificallywhich
#kernelnetworkingdevicestouse.
devices=wlan0,eth1
```

```
#OrletAutoInterfaceuseallsuitable
#devicesexceptforalistofignoredones.
ignored_devices=tun0,eth0
```

If you are connected to the Internet with IPv6, and your provider will route IPv6 multicast, you can potentially configure the Auto Interface to globally autodiscover other Reticulum nodes within your selected Group ID. You can specify the discovery scope by setting it to one of `link` , `admin` , `site` , `organisation` or `global` . 

```
[[DefaultInterface]]
type=AutoInterface
enabled=yes
#Configureglobaldiscovery
group_id=custom_network_name
discovery_scope=global
#Otherconfigurationoptions
```

(continues on next page) 

**Chapter 8. Configuring Interfaces** 

**96** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
discovery_port=48555
data_port=49555
```

## **8.3 Backbone Interface** 

The Backbone interface is a very fast and resource efficient interface type, primarily intended for interconnecting Reticulum instances over many different types of mediums. It uses a kernel-event I/O backend, and can handle thousands of interfaces and/or clients with relatively low system resource utilisation. **This interface type is currently only supported on Linux and Android** . 

## **Note** 

The Backbone Interface is fully compatible with the `TCPServerInterface` and `TCPClientInterface` types, and they can be used interchangably, and cross-connect with each other. On systems that support `BackboneInterface` , it is generally recommended to use it, unless you need specific options or features that the TCP server and client interfaces provide. 

While the goal is to support _all_ socket types and I/O devices provided by the underlying operating system, the initial release only provides support for TCP connections over IPv4 and IPv6. 

For all types of connections over a `BackboneInterface` , Reticulum will gracefully handle intermittency, link loss, and connections that come and go. 

## **8.3.1 Listeners** 

The following examples illustrates various ways to set up `BackboneInterface` listeners. 

```
#Thisexampledemonstratesabackboneinterface
#thatlistensforincomingconnectionsonthe
#specifiedIPaddressandportnumber.
[[BackboneListener]]
type=BackboneInterface
enabled=yes
listen_on=0.0.0.0
port=4242
#AlternativelyyoucanbindtoaspecificIP
[[BackboneListener]]
type=BackboneInterface
enabled=yes
listen_on=10.0.0.88
port=4242
#Oraspecificnetworkdevice
[[BackboneListener]]
type=BackboneInterface
enabled=yes
device=eth0
port=4242
```

**8.3. Backbone Interface** 

**97** 

**Reticulum Network Stack, Release 1.3.0** 

If you are using the interface on a device which has both IPv4 and IPv6 addresses available, you can use the `prefer_ipv6` option to bind to the IPv6 address: 

```
#Thisexampledemonstratesabackboneinterface
#listeningontheIPv6addressofaspecified
#kernelnetworkingdevice.
[[BackboneListener]]
type=BackboneInterface
enabled=yes
prefer_ipv6=yes
device=eth0
port=4242
```

To use the `BackboneInterface` over Yggdrasil, you can simply specify the Yggdrasil `tun` device and a listening port, like so: 

```
#Thisexampledemonstratesabackboneinterface
#listeningforconnectionsoverYggdrasil.
[[YggdrasilBackboneInterface]]
type=BackboneInterface
enabled=yes
device=tun0
port=4343
```

## **8.3.2 Connecting Remotes** 

The following examples illustrates various ways to connect to remote `BackboneInterface` listeners. As noted above, `BackboneInterface` interfaces can also connect to remote `TCPServerInterface` , and as such these interface types can be used interchangably. 

_`# Here` '_ _`s an example of a backbone interface that # connects to a remote listener.`_ `[[Backbone Remote]] type = BackboneInterface enabled = yes remote = amsterdam.connect.reticulum.network target_port = 4251` 

To connect to remotes over Yggdrasil, simply specify the target Yggdrasil IPv6 address and port, like so: 

```
[[YggdrasilRemote]]
type=BackboneInterface
enabled=yes
target_host=201:5d78:af73:5caf:a4de:a79f:3278:71e5
target_port=4343
```

## **8.4 TCP Server Interface** 

The TCP Server interface is suitable for allowing other peers to connect over the Internet or private IPv4 and IPv6 networks. When a TCP server interface has been configured, other Reticulum peers can connect to it with a TCP Client interface. 

**Chapter 8. Configuring Interfaces** 

**98** 

**Reticulum Network Stack, Release 1.3.0** 

```
#ThisexampledemonstratesaTCPserverinterface.
#ItwilllistenforincomingconnectionsonallIP
#interfacesonport4242.
[[TCPServerInterface]]
type=TCPServerInterface
enabled=yes
listen_ip=0.0.0.0
listen_port=4242
```

```
#AlternativelyyoucanbindtoaspecificIP
[[TCPServerInterface]]
type=TCPServerInterface
enabled=yes
listen_ip=10.0.0.88
listen_port=4242
#Oraspecificnetworkdevice
[[TCPServerInterface]]
type=TCPServerInterface
enabled=yes
device=eth0
listen_port=4242
```

If you are using the interface on a device which has both IPv4 and IPv6 addresses available, you can use the `prefer_ipv6` option to bind to the IPv6 address: 

```
#ThisexampledemonstratesaTCPserverinterface.
#Itwilllistenforincomingconnectionsonthe
#specifiedIPaddressandportnumber.
[[TCPServerInterface]]
type=TCPServerInterface
enabled=yes
prefer_ipv6=True
device=eth0
port=4242
```

To use the TCP Server Interface over Yggdrasil, you can simply specify the Yggdrasil `tun` device and a listening port, like so: 

```
[[YggdrasilTCPServerInterface]]
type=TCPServerInterface
enabled=yes
device=tun0
listen_port=4343
```

## **Note** 

The TCP interfaces support tunneling over I2P, but to do so reliably, you must use the i2p_tunneled option: 

```
[[TCPServeronI2P]]
```

(continues on next page) 

**8.4. TCP Server Interface** 

**99** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
type=TCPServerInterface
enabled=yes
listen_ip=127.0.0.1
listen_port=5001
i2p_tunneled=yes
```

In almost all cases, it is easier to use the dedicated `I2PInterface` , but for complete control, and using I2P routers running on external systems, this option also exists. 

## **8.5 TCP Client Interface** 

To connect to a TCP server interface, you can use the TCP client interface. Many TCP Client interfaces from different peers can connect to the same TCP Server interface at the same time. 

The TCP interface types can also tolerate intermittency in the IP link layer. This means that Reticulum will gracefully handle IP links that go up and down, and restore connectivity after a failure, once the other end of a TCP interface reappears. 

_`# Here` '_ _`s an example of a TCP Client interface. The # target_host can be a hostname or an IPv4 or IPv6 address.`_ `[[TCP Client Interface]] type = TCPClientInterface enabled = yes target_host = 127.0.0.1 target_port = 4242` 

To use the TCP Client Interface over Yggdrasil, simply specify the target Yggdrasil IPv6 address and port, like so: 

```
[[YggdrasilTCPClientInterface]]
type=TCPClientInterface
enabled=yes
target_host=201:5d78:af73:5caf:a4de:a79f:3278:71e5
target_port=4343
```

It is also possible to use this interface type to connect via other programs or hardware devices that expose a KISS interface on a TCP port, for example software-based soundmodems. To do this, use the `kiss_framing` option: 

_`# Here` '_ _`s an example of a TCP Client interface that connects # to a software TNC soundmodem on a KISS over TCP port.`_ `[[TCP KISS Interface]] type = TCPClientInterface enabled = yes kiss_framing = True target_host = 127.0.0.1 target_port = 8001 fixed_mtu = 500` 

**Caution!** Only use the KISS framing option when connecting to external devices and programs like soundmodems and similar over TCP. When using the `TCPClientInterface` in conjunction with the `TCPServerInterface` you should never enable `kiss_framing` , since this will disable internal reliability and recovery mechanisms that greatly improves performance over unreliable and intermittent TCP links. 

For KISS devices that need only supports a particular MTU, you can use the `fixed_mtu` option. 

**Chapter 8. Configuring Interfaces** 

**100** 

**Reticulum Network Stack, Release 1.3.0** 

## **Note** 

The TCP interfaces support tunneling over I2P, but to do so reliably, you must use the i2p_tunneled option: 

```
[[TCPClientoverI2P]]
type=TCPClientInterface
enabled=yes
target_host=127.0.0.1
target_port=5001
i2p_tunneled=yes
```

## **8.6 UDP Interface** 

A UDP interface can be useful for communicating over IP networks, both private and the internet. It can also allow broadcast communication over IP networks, so it can provide an easy way to enable connectivity with all other peers on a local area network. 

## **Warning** 

Using broadcast UDP traffic has performance implications, especially on WiFi. If your goal is simply to enable easy communication with all peers in your local Ethernet broadcast domain, the _Auto Interface_ performs _much_ better, and is even easier to use. 

```
#Thisexampleenablescommunicationwithother
#localReticulumpeersoverUDP.
[[UDPInterface]]
type=UDPInterface
enabled=yes
listen_ip=0.0.0.0
listen_port=4242
forward_ip=255.255.255.255
forward_port=4242
#Theaboveconfigurationwillallowcommunication
#withinthelocalbroadcastdomainsofalllocal
#IPinterfaces.
#Insteadofspecifyinglisten_ip,listen_port,
#forward_ipandforward_port,youcanalsobind
#toaspecificnetworkdevicelikebelow.
#device=eth0
#port=4242
#Assumingtheeth0devicehastheaddress
#10.55.0.72/24,theaboveconfigurationwould
#beequivalenttothefollowingmanualsetup.
#Notethatwearebothlisteningandforwardingto
```

(continues on next page) 

**8.6. UDP Interface** 

**101** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
#thebroadcastaddressofthenetworksegments.
#listen_ip=10.55.0.255
#listen_port=4242
#forward_ip=10.55.0.255
#forward_port=4242
```

```
#Youcanofcoursealsocommunicateonlywith
#asingleIPaddress
#listen_ip=10.55.0.15
#listen_port=4242
#forward_ip=10.55.0.16
#forward_port=4242
```

## **8.7 I2P Interface** 

The I2P interface lets you connect Reticulum instances over the Invisible Internet Protocol. This can be especially useful in cases where you want to host a globally reachable Reticulum instance, but do not have access to any public IP addresses, have a frequently changing IP address, or have firewalls blocking inbound traffic. 

Using the I2P interface, you will get a globally reachable, portable and persistent I2P address that your Reticulum instance can be reached at. 

To use the I2P interface, you must have an I2P router running on your system. The easiest way to achieve this is to download and install the latest release of the `i2pd` package. For more details about I2P, see the geti2p.net website. 

When an I2P router is running on your system, you can simply add an I2P interface to Reticulum: 

```
[[I2P]]
type=I2PInterface
enabled=yes
connectable=yes
```

On the first start, Reticulum will generate a new I2P address for the interface and start listening for inbound traffic on it. This can take a while the first time, especially if your I2P router was also just started, and is not yet well-connected to the I2P network. When ready, you should see I2P base32 address printed to your log file. You can also inspect the status of the interface using the `rnstatus` utility. 

To connect to other Reticulum instances over I2P, just add a comma-separated list of I2P base32 addresses to the `peers` option of the interface: 

```
[[I2P]]
type=I2PInterface
enabled=yes
connectable=yes
peers=5urvjicpzi7q3ybztsef4i5ow2aq4soktfj7zedz53s47r54jnqq.b32.i2p
```

It can take anywhere from a few seconds to a few minutes to establish I2P connections to the desired peers, so Reticulum handles the process in the background, and will output relevant events to the log. 

**Note** 

**Chapter 8. Configuring Interfaces** 

**102** 

**Reticulum Network Stack, Release 1.3.0** 

While the I2P interface is the simplest way to use Reticulum over I2P, it is also possible to tunnel the TCP server and client interfaces over I2P manually. This can be useful in situations where more control is needed, but requires manual tunnel setup through the I2P daemon configuration. 

It is important to note that the two methods are _interchangably compatible_ . You can use the I2PInterface to connect to a TCPServerInterface that was manually tunneled over I2P, for example. This offers a high degree of flexibility in network setup, while retaining ease of use in simpler use-cases. 

## **8.8 RNode LoRa Interface** 

To use Reticulum over LoRa, the RNode interface can be used, and offers full control over LoRa parameters. 

## **Warning** 

Radio frequency spectrum is a legally controlled resource, and legislation varies widely around the world. It is your responsibility to be aware of any relevant regulation for your location, and to make decisions accordingly. 

_`# Here` '_ _`s an example of how to add a LoRa interface # using the RNode LoRa transceiver.`_ `[[RNode LoRa Interface]] type = RNodeInterface` _`# Enable interface if you want use it!`_ `enabled = yes` _`# Serial port for the device`_ `port = /dev/ttyUSB0` _`# You can connect wirelessly to the # RNode device if it supports WiFi.`_ 

```
#ConnectbyIPaddress
#port=tcp://10.0.0.1
```

```
#Or,connectbyhostname
#port=tcp://rnodef3b9.local
```

```
#ItisalsopossibletouseBLEdevices
#insteadofwiredserialports.The
#targetRNodemustbepairedwiththe
#hostdevicebeforeconnecting.BLE
#devicescanbeconnectedbyname,
#BLEMACaddressorbyanyavailable.
```

```
#Connecttospecificdevicebyname
#port=ble://RNode3B87
#OrbyBLEMACaddress
#port=ble://F4:12:73:29:4E:89
```

(continues on next page) 

**8.8. RNode LoRa Interface** 

**103** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
#Orconnecttothefirstavailable,
#paireddevice
#port=ble://
```

```
#Setfrequencyto867.2MHz
frequency=867200000
```

```
#SetLoRabandwidthto125KHz
bandwidth=125000
```

```
#SetTXpowerto7dBm(5mW)
txpower=7
```

```
#Selectspreadingfactor8.Valid
#rangeis7through12,with7
#beingthefastestand12having
#thelongestrange.
spreadingfactor=8
```

```
#Selectcodingrate5.Validrange
#is5throough8,with5beingthe
#fastest,and8thelongestrange.
codingrate=5
```

```
#YoucanconfiguretheRNodetosend
#outidentificationonthechannelwith
#asetintervalbyconfiguringthe
#followingtwoparameters.
```

```
#id_callsign=MYCALL-0
#id_interval=600
```

```
#ForcertainhomebrewRNodeinterfaces
#withlowamountsofRAM,usingpacket
#flowcontrolcanbeuseful.Bydefault
#itisdisabled.
```

```
#flow_control=False
```

```
#Itispossibletolimittheairtime
#utilisationofanRNodebyusingthe
#followingtwoconfigurationoptions.
#Theshort-termlimitisappliedina
#windowofapproximately15seconds,
#andthelong-termlimitisenforced
#overarolling60minutewindow.Both
#optionsarespecifiedinpercent.
```

```
#airtime_limit_long=1.5
#airtime_limit_short=33
```

**Chapter 8. Configuring Interfaces** 

**104** 

**Reticulum Network Stack, Release 1.3.0** 

## **8.9 RNode Multi Interface** 

For RNodes that support multiple LoRa transceivers, the RNode Multi interface can be used to configure sub-interfaces individually. 

## **Warning** 

Radio frequency spectrum is a legally controlled resource, and legislation varies widely around the world. It is your responsibility to be aware of any relevant regulation for your location, and to make decisions accordingly. 

_`# Here` '_ _`s an example of how to add an RNode Multi interface # using the RNode LoRa transceiver.`_ `[[RNode Multi Interface]] type = RNodeMultiInterface` _`# Enable interface if you want to use it!`_ `enabled = yes` _`# Serial port for the device`_ `port = /dev/ttyACM0` _`# You can configure the RNode to send # out identification on the channel with # a set interval by configuring the # following two parameters. # id_callsign = MYCALL-0 # id_interval = 600 # A subinterface`_ `[[[High Datarate]]]` _`# Subinterfaces can be enabled and disabled in of themselves`_ `enabled = yes` _`# Set frequency to 2.4GHz`_ `frequency = 2400000000` _`# Set LoRa bandwidth to 1625 KHz`_ `bandwidth = 1625000` _`# Set TX power to 0 dBm (0.12 mW)`_ `txpower = 0` _`# The virtual port, only the manufacturer # or the person who wrote the board config # can tell you what it will be for which # physical hardware interface`_ `vport = 1` _`# Select spreading factor 5. Valid # range is 5 through 12, with 5`_ 

(continues on next page) 

**8.9. RNode Multi Interface** 

**105** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
#beingthefastestand12having
#thelongestrange.
spreadingfactor=5
#Selectcodingrate5.Validrange
#is5throough8,with5beingthe
#fastest,and8thelongestrange.
codingrate=5
```

```
#Itispossibletolimittheairtime
#utilisationofanRNodebyusingthe
#followingtwoconfigurationoptions.
#Theshort-termlimitisappliedina
#windowofapproximately15seconds,
#andthelong-termlimitisenforced
#overarolling60minutewindow.Both
#optionsarespecifiedinpercent.
#airtime_limit_long=100
#airtime_limit_short=100
```

## `[[[Low Datarate]]]` 

```
#Subinterfacescanbeenabledanddisabledinofthemselves
enabled=yes
#Setfrequencyto865.6MHz
frequency=865600000
```

```
#Thevirtualport,onlythemanufacturer
#orthepersonwhowrotetheboardconfig
#cantellyouwhatitwillbeforwhich
#physicalhardwareinterface
vport=0
#SetLoRabandwidthto125KHz
bandwidth=125000
#SetTXpowerto0dBm(0.12mW)
txpower=0
#Selectspreadingfactor7.Valid
#rangeis5through12,with5
#beingthefastestand12having
#thelongestrange.
spreadingfactor=7
```

```
#Selectcodingrate5.Validrange
#is5throough8,with5beingthe
#fastest,and8thelongestrange.
codingrate=5
#Itispossibletolimittheairtime
```

(continues on next page) 

**Chapter 8. Configuring Interfaces** 

**106** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
#utilisationofanRNodebyusingthe
#followingtwoconfigurationoptions.
#Theshort-termlimitisappliedina
#windowofapproximately15seconds,
#andthelong-termlimitisenforced
#overarolling60minutewindow.Both
#optionsarespecifiedinpercent.
#airtime_limit_long=100
#airtime_limit_short=100
```

## **8.10 Serial Interface** 

Reticulum can be used over serial ports directly, or over any device with a serial port, that will transparently pass data. Useful for communicating directly over a wire-pair, or for using devices such as data radios and lasers. 

```
[[SerialInterface]]
type=SerialInterface
enabled=yes
#Serialportforthedevice
port=/dev/ttyUSB0
#Settheserialbaud-rateandother
#configurationparameters.
speed=115200
databits=8
parity=none
stopbits=1
```

## **8.11 Pipe Interface** 

Using this interface, Reticulum can use any program as an interface via _stdin_ and _stdout_ . This can be used to easily create virtual interfaces, or to interface with custom hardware or other systems. 

```
[[PipeInterface]]
type=PipeInterface
enabled=yes
#Externalcommandtoexecute
command=netcat-l5757
#Optionalrespawndelay,inseconds
respawn_delay=5
```

Reticulum will write all packets to _stdin_ of the `command` option, and will continuously read and scan its _stdout_ for Reticulum packets. If `EOF` is reached, Reticulum will try to respawn the program after waiting for `respawn_interval` seconds. 

**8.10. Serial Interface** 

**107** 

**Reticulum Network Stack, Release 1.3.0** 

## **8.12 KISS Interface** 

With the KISS interface, you can use Reticulum over a variety of packet radio modems and TNCs, including OpenModem. KISS interfaces can also be configured to periodically send out beacons for station identification purposes. 

## **Warning** 

Radio frequency spectrum is a legally controlled resource, and legislation varies widely around the world. It is your responsibility to be aware of any relevant regulation for your location, and to make decisions accordingly. 

```
[[PacketRadioKISSInterface]]
type=KISSInterface
enabled=yes
#Serialportforthedevice
port=/dev/ttyUSB1
```

```
#Settheserialbaud-rateandother
#configurationparameters.
speed=115200
databits=8
parity=none
stopbits=1
#Setthemodempreamble.
preamble=150
#SetthemodemTXtail.
txtail=10
```

```
#ConfigureCDMAparameters.These
#settingsarereasonabledefaults.
persistence=200
slottime=20
```

_`# You can configure the interface to send # out identification on the channel with # a set interval by configuring the # following two parameters. The KISS # interface will only ID if the set # interval has elapsed since it` '_ _`s last # actual transmission. The interval is # configured in seconds. # This option is commented out and not # used by default. # id_callsign = MYCALL-0 # id_interval = 600`_ 

```
#WhethertouseKISSflow-control.
#Thisisusefulformodemsthathave
#asmallinternalpacketbuffer,but
#supportpacketflowcontrolinstead.
```

(continues on next page) 

**Chapter 8. Configuring Interfaces** 

**108** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
flow_control=false
```

## **8.13 AX.25 KISS Interface** 

If you’re using Reticulum on amateur radio spectrum, you might want to use the AX.25 KISS interface. This way, Reticulum will automatically encapsulate it’s traffic in AX.25 and also identify your stations transmissions with your callsign and SSID. 

Only do this if you really need to! Reticulum doesn’t need the AX.25 layer for anything, and it incurs extra overhead on every packet to encapsulate in AX.25. 

A more efficient way is to use the plain KISS interface with the beaconing functionality described above. 

## **Warning** 

Radio frequency spectrum is a legally controlled resource, and legislation varies widely around the world. It is your responsibility to be aware of any relevant regulation for your location, and to make decisions accordingly. 

```
[[PacketRadioAX.25KISSInterface]]
type=AX25KISSInterface
#SetthestationcallsignandSSID
callsign=NO1CLL
ssid=0
#Enableinterfaceifyouwantuseit!
enabled=yes
#Serialportforthedevice
port=/dev/ttyUSB2
#Settheserialbaud-rateandother
#configurationparameters.
speed=115200
databits=8
parity=none
stopbits=1
#Setthemodempreamble.A150ms
#preambleshouldbeareasonable
#default,butmayneedtobe
#increasedforradioswithslow-
#openingsquelchandlongTX/RX
#turnaround
preamble=150
#SetthemodemTXtail.Inmost
#casesthisshouldbekeptaslow
#aspossibletonotwasteairtime.
txtail=10
```

(continues on next page) 

**8.13. AX.25 KISS Interface** 

**109** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
#ConfigureCDMAparameters.These
#settingsarereasonabledefaults.
persistence=200
slottime=20
#WhethertouseKISSflow-control.
#Thisisusefulformodemswitha
#smallinternalpacketbuffer.
flow_control=false
```

## **8.14 Discoverable Interfaces** 

Reticulum includes a powerful system for publishing your local interfaces to the wider network, allowing other peers to _discover, validate, and automatically connect to them_ . This feature is particularly useful for creating decentralized networks where peers can dynamically find entrypoints, such as public Internet gateways or local radio access points, without relying on static configuration files or centralized directories. 

When an interface is made **discoverable** , your Reticulum instance will periodically broadcast an announce packet containing the connection details and parameters required for other peers to establish a connection. These announces are propagated over the network using the standard Reticulum announce mechanism using the `rnstransport. discovery.interface` destination type. 

## **Note** 

To use the interface discovery functionality, the `LXMF` module must be installed in your Python environment. You can install it using pip: 

```
pipinstalllxmf
```

## **8.14.1 Enabling Discovery** 

Interface discovery is enabled on a per-interface basis. To make a specific interface discoverable, you must add the `discoverable` option to that interface’s configuration block and set it to `yes` . 

```
[[MyPublicGateway]]
type=BackboneInterface
...
discoverable=yes
```

Once enabled, Reticulum will automatically handle the generation, signing, stamping, and broadcasting of the discovery announces. It is not _required_ to enable Transport to publish interface discovery information, but for most use cases where you want others to connect to you, you will likely want `enable_transport` set to `yes` in the `[reticulum]` section of your configuration. 

## **8.14.2 Discovery Parameters** 

When `discoverable` is enabled, a variety of additional options become available to control how the interface is presented to the network. These parameters allow you to fine-tune the metadata, security requirements, and visibility of your interface. 

## **Basic Metadata** 

**Chapter 8. Configuring Interfaces** 

**110** 

**Reticulum Network Stack, Release 1.3.0** 

## `discovery_name` 

A human-readable name for the interface. This name will be displayed to users on remote systems when they list discovered interfaces. If not specified, the interface name (the section header) will be used. 

## `announce_interval` 

The interval in minutes between successive discovery announces for this interface. Default is 360 minutes (6 hours). For stable, long-running infrastructure, higher intervals (12 to 22 hours) are usually sufficient and reduce network load. Minimum allowed value is 5 minutes (but expect to have your announces throttled if using intervals below one hour). 

## **Connectivity Specification** 

## `reachable_on` 

Specifies the address that remote peers should use to connect to this interface. 

- For TCP and Backbone interfaces, this is typically the public IP address or hostname. Do not include the port, this is fetched automatically from the interface. 

- For I2P interfaces, this is usually the I2P `b32` address. This value is fetched automatically from the `I2PInterface` once it is up and connected to the I2P network, so you should not set this manually, unless you absolutely know what you’re doing. 

**Dynamic Resolution:** This option also accepts a path to an external executable script or binary. If a path is provided, Reticulum will execute the script and use its `stdout` as the reachability address. This is useful for devices behind dynamic DNS, NATs, or complex cloud environments where the external IP is not known locally. The script must simply print the address to stdout and exit. 

## **Note** 

When using an executable script for `reachable_on` , Reticulum expects the script to output only the IP address or hostname to `stdout` , followed by a newline character. Any additional output or errors may cause the resolution to fail. Ensure the script has executable permissions and is robust against temporary network failures. 

A minimal example of a script that resolves the externally available, public IP of an internet-connected system could look like this: 

```
#!/bin/bash
curl-sip.me
exit$?
```

On a real system, you should make the script robust enough to deal with intermittent Internet or service failures, such that the script _always_ returns a sensible value, or if not possible at least exits with a non-zero exit return code, so Reticulum knows the output is invalid. 

## **Security & Cost** 

## `discovery_stamp_value` 

- Defines the proof-of-work difficulty for the cryptographic stamp included in the announce. This value acts as a cost barrier to prevent network flooding. The default value is `14` . Increasing this value makes it computationally more expensive to generate an announce, which can be useful to prevent spam on very large networks, but it also increases CPU load on your system when generating announces. Stamps are cached, and only generated if interface information changes, or at instance restart. If you have the computational resources, it is generally advisable to use as high a stamp value as possible. 

## **Privacy & Encryption** 

## `discovery_encrypt` 

If set to `yes` , the discovery announce payload will be encrypted. To decrypt the announce, remote peers must 

**8.14. Discoverable Interfaces** 

**111** 

**Reticulum Network Stack, Release 1.3.0** 

possess the _network identity_ configured for your instance (see `network_identity` in the `[reticulum]` section). This allows you to publish private interfaces that are only discoverable to specific trusted networks. 

## **Important** 

If you enable `discovery_encrypt` but do not configure a valid `network_identity` in the `[reticulum]` section of your configuration, Reticulum will abort the interface discovery announce. Encryption requires a valid network identity key to function. 

## `publish_ifac` 

If set to `yes` , the Interface Access Code (IFAC) name and passphrase for this interface will be included in the discovery announce. This allows peers to automatically configure the correct authentication parameters when connecting to the interface. 

## **Physical Location** 

## `latitude` **,** `longitude` **,** `height` 

Optional physical coordinates for the interface. These are useful for mapping discovered interfaces geographically or for clients to automatically select the nearest access point. Coordinates should be in decimal degrees, height in meters. 

## **Radio Parameters** 

For physical radio interfaces like `RNodeInterface` or `KISSInterface` , the following optional parameters allow you to broadcast the operating frequency and characteristics, allowing clients to verify compatibility before connecting: 

## `discovery_frequency` 

The operating frequency in Hz. Auto-configured on RNode interfaces. Necessary on KISS-based radio interfaces and `TCPClientInterfaces` connecting to radio modems. 

## `discovery_bandwidth` 

The signal bandwidth in Hz. Auto-configured on RNode interfaces. Useful on KISS-based radio interfaces and `TCPClientInterfaces` connecting to radio modems. 

## `discovery_modulation` 

The modulation type or scheme. Auto-configured on RNode interfaces, but highly advisable to include on other radio-based interfaces. 

## **8.14.3 Interface Modes** 

When you enable discovery on an interface, Reticulum enforces certain interface modes to ensure the interface is actually useful for remote peers. 

If an interface is configured as `discoverable` , but its mode is not explicitly set to `gateway` (for server-style interfaces like `BackboneInterface` or `TCPServerInterface` ) or `access_point` (for radio interfaces like `RNodeInterface` ), Reticulum will automatically configure the appropriate mode and log a notice. 

For example, if you enable discovery on a `RNodeInterface` without specifying the mode, Reticulum will automatically set it to `access_point` mode. 

## **8.14.4 Security Considerations** 

When making interfaces discoverable, you are effectively broadcasting an invitation to connect to your system. It is important to understand the security implications of the configuration options you choose. 

## **Publishing Credentials** 

If you enable `publish_ifac = yes` , your interface’s authentication passphrase will be included in the announce. If you are operating a public network and want anyone to connect, this is acceptable. However, if you wish to restrict access 

**Chapter 8. Configuring Interfaces** 

**112** 

**Reticulum Network Stack, Release 1.3.0** 

to a specific group of users, you **must** enable `discovery_encrypt = yes` . This ensures that only peers possessing the correct `network_identity` can decode the passphrase. 

## **Topology Exposure** 

A discoverable interface announces its presence, location (if configured), and capabilities to the network. Even if the connection details are encrypted, the _fact_ that a connectable node exists within a certain network becomes public information. In high-security or scenarios requiring operational secrecy, consider the implications of advertising your infrastructure’s existence. 

## **8.14.5 Example Configuration** 

Below is an example configuration for a public backbone gateway. This configuration publishes a high-value, publicly discoverable interface, that anyone can connect to. 

```
[[MyPublicGateway]]
type=BackboneInterface
mode=gateway
listen_on=0.0.0.0
port=4242
#EnableDiscovery
discoverable=yes
#InterfaceDetails
discovery_name=RegionAPublicEntrypoint
announce_interval=720
#UseexternalscripttoresolvedynamicIP
reachable_on=/usr/local/bin/get_external_ip.sh
```

```
#Generatehighstampvalue
discovery_stamp_value=24
#Optionallocationdata
latitude=51.99714
longitude=-0.74195
height=15
```

The next example create an encrypted discovery-enabled interface, requiring a specific network identity to decode, and includes IFAC credentials for seamless authentication. 

```
[[MyPrivateGateway]]
type=BackboneInterface
mode=gateway
listen_on=0.0.0.0
port=5858
network_name=internal_1
passphrase=Mevpekyafshak5Wr
```

```
#EnableDiscovery
discoverable=yes
#InterfaceDetails
discovery_name=RegionAPrivateBackbone
```

(continues on next page) 

**8.14. Discoverable Interfaces** 

**113** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
announce_interval=720
```

```
#UseexternalscripttoresolvedynamicIP
reachable_on=/usr/local/bin/get_external_ip.sh
```

```
#Targetstampvalue
discovery_stamp_value=22
#Encryptannouncesforournetworkonly
discovery_encrypt=yes
#Includecredentialssotrusted
#peerscanconnectautomatically
publish_ifac=yes
#Optionallocationdata
latitude=34.06915
longitude=-118.44318
height=15
```

In the `[reticulum]` section of your configuration, you would define the network identity used for encryption as follows: 

```
[reticulum]
...
#Theidentityusedtosign/encryptdiscoveryannounces
network_identity=~/.reticulum/storage/identities/my_network_identity
...
```

With these configuration options applied, your Reticulum instance will actively participate in the network’s discovery ecosystem. Other peers running Reticulum with discovery enabled will be able to see your interface, validate its cryptographic stamp, and (depending on their configuration) automatically connect to it. 

For information on how to use these discovered interfaces and configure your system to auto-connect to them, refer to the _Discovering Interfaces_ chapter. 

## **8.15 Common Interface Options** 

A number of general configuration options are available on most interfaces. These can be used to control various aspects of interface behaviour. 

- The `enabled` option tells Reticulum whether or not to bring up the interface. Defaults to `False` . For any interface to be brought up, the `enabled` option must be set to `True` or `Yes` . 

- The `mode` option allows selecting the high-level behaviour of the interface from a number of options. 

   - The default value is `full` . In this mode, all discovery, meshing and transport functionality is available. 

   - In the `access_point` (or shorthand `ap` ) mode, the interface will operate as a network access point. In this mode, announces will not be automatically broadcasted on the interface, and paths to destinations on the interface will have a much shorter expiry time. This mode is useful for creating interfaces that are mostly quiet, unless when someone is actually using them. An example of this could be a radio interface serving a wide area, where users are expected to connect momentarily, use the network, and then disappear again. 

- The `outgoing` option sets whether an interface is allowed to transmit. Defaults to `True` . If set to `False` or `No` the interface will only receive data, and never transmit. 

**Chapter 8. Configuring Interfaces** 

**114** 

**Reticulum Network Stack, Release 1.3.0** 

- The `network_name` option sets the virtual network name for the interface. This allows multiple separate network segments to exist on the same physical channel or medium. 

- The `passphrase` option sets an authentication passphrase on the interface. This option can be used in conjunction with the `network_name` option, or be used alone. 

- The `ifac_size` option allows customising the length of the Interface Authentication Codes carried by each packet on named and/or authenticated network segments. It is set by default to a size suitable for the interface in question, but can be set to a custom size between 8 and 512 bits by using this option. In normal usage, this option should not be changed from the default. 

- The `announce_cap` option lets you configure the maximum bandwidth to allocate, at any given time, to propagating announces and other network upkeep traffic. It is configured at 2% by default, and should normally not need to be changed. Can be set to any value between `1` and `100` . 

_If an interface exceeds its announce cap, it will queue announces for later transmission. Reticulum will always prioritise propagating announces from nearby nodes first. This ensures that the local topology is prioritised, and that slow networks are not overwhelmed by interconnected fast networks._ 

_Destinations that are rapidly re-announcing will be down-prioritised further. Trying to get “first-inline” by announce spamming will have the exact opposite effect: Getting moved to the back of the queue every time a new announce from the excessively announcing destination is received._ 

_This means that it is always beneficial to select a balanced announce rate, and not announce more often than is actually necesarry for your application to function._ 

- The `bitrate` option configures the interface bitrate. Reticulum will use interface speeds reported by hardware, or try to guess a suitable rate when the hardware doesn’t report any. In most cases, the automatically found rate should be sufficient, but it can be configured by using the `bitrate` option, to set the interface speed in _bits per second_ . 

- The `bootstrap_only` option designates an interface as a temporary bridge for initial connectivity. If this option is enabled, the interface will be monitored and automatically detached once the number of auto-connected interfaces reaches the limit configured by `autoconnect_discovered_interfaces` . This is particularly useful for using a slow or expensive connection (such as a single LoRa link or a remote TCP tunnel) solely to discover better local infrastructure, which then supersedes the bootstrap interface. 

## **8.16 Interface Modes** 

The optional `mode` setting is available on all interfaces, and allows selecting the high-level behaviour of the interface from a number of modes. These modes affect how Reticulum selects paths in the network, how announces are propagated, how long paths are valid and how paths are discovered. 

Configuring modes on interfaces is **not** strictly necessary, but can be useful when building or connecting to more complex networks. If your Reticulum instance is not running a Transport Node, it is rarely useful to configure interface modes, and in such cases interfaces should generally be left in the default mode. 

- The default mode is `full` . In this mode, all discovery, meshing and transport functionality is activated. 

- The `gateway` mode (or shorthand `gw` ) also has all discovery, meshing and transport functionality available, but will additionally try to discover unknown paths on behalf of other nodes residing on the `gateway` interface. If Reticulum receives a path request for an unknown destination, from a node on a `gateway` interface, it will try to discover this path via all other active interfaces, and forward the discovered path to the requestor if one is found. 

If you want to allow other nodes to widely resolve paths or connect to a network via an interface, it might be useful to put it in this mode. By creating a chain of `gateway` interfaces, other nodes will be able to immediately discover paths to any destination along the chain. 

**8.16. Interface Modes** 

**115** 

**Reticulum Network Stack, Release 1.3.0** 

_Please note!_ It is the interface _facing the clients_ that must be put into `gateway` mode for this to work, not the interface facing the wider network (for this, the `boundary` mode can be useful, though). 

- In the `access_point` (or shorthand `ap` ) mode, the interface will operate as a network access point. In this mode, announces will not be automatically broadcasted on the interface, and paths to destinations on the interface will have a much shorter expiry time. In addition, path requests from clients on the access point interface will be handled in the same way as the `gateway` interface. 

This mode is useful for creating interfaces that remain quiet, until someone actually starts using them. An example of this could be a radio interface serving a wide area, where users are expected to connect momentarily, use the network, and then disappear again. 

- The `roaming` mode should be used on interfaces that are roaming (physically mobile), seen from the perspective of other nodes in the network. As an example, if a vehicle is equipped with an external LoRa interface, and an internal, WiFi-based interface, that serves devices that are moving _with_ the vehicle, the external LoRa interface should be configured as `roaming` , and the internal interface can be left in the default mode. With transport enabled, such a setup will allow all internal devices to reach each other, and all other devices that are available on the LoRa side of the network, when they are in range. Devices on the LoRa side of the network will also be able to reach devices internal to the vehicle, when it is in range. Paths via `roaming` interfaces also expire faster. 

- The purpose of the `boundary` mode is to specify interfaces that establish connectivity with network segments that are significantly different than the one this node exists on. As an example, if a Reticulum instance is part of a LoRa-based network, but also has a high-speed connection to a public Transport Node available on the Internet, the interface connecting over the Internet should be set to `boundary` mode. 

For a table describing the impact of all modes on announce propagation, please see the _Announce Propagation Rules_ section. 

## **8.17 Announce Rate Control** 

The built-in announce control mechanisms and the default `announce_cap` option described above are sufficient most of the time, but in some cases, especially on fast interfaces, or when connecting to large public networks, it may be useful to control the target announce rate. 

Using the `announce_rate_target` , `announce_rate_grace` and `announce_rate_penalty` options, this can be done on a per-interface basis, or by setting instance-wide defaults. When configured, this moderates the _rate at which received announces are re-broadcasted to other interfaces_ . 

- The `announce_rate_target` option sets the minimum amount of time, in seconds, that should pass between received announces, for any one destination. As an example, setting this value to `3600` means that announces _received_ on this interface will only be re-transmitted and propagated to other interfaces once every hour, no matter how often they are received. 

- The optional `announce_rate_grace` defines the number of times a destination can violate the announce rate before the target rate is enforced. 

- The optional `announce_rate_penalty` configures an extra amount of time that is added to the normal rate target. As an example, if a penalty of `7200` seconds is defined, once the rate target is enforced, the destination in question will only have its announces propagated every 3 hours, until it lowers its actual announce rate to within the target. 

You can also configure default announce rate parameters for all interfaces that do not have these parameters set explicitly by setting the `default_ar_target default_ar_penalty` and `default_ar_grace` options in the `[reticulum]` 

**Chapter 8. Configuring Interfaces** 

**116** 

**Reticulum Network Stack, Release 1.3.0** 

section of the configuration file. If any of these options are set, they will automatically be applied to any interface if transport is enabled, and the interface does not have the parameters set explicitly. 

For auto-connected interfaces, sensible default announce rate control parameters will **always** be set, even if the defaults are not configured explicitly, but if you set the defaults, auto-connected interfaces will adhere to these as well. 

These mechanisms, in conjunction with the `annouce_cap` mechanisms mentioned above means that it is essential to select a balanced announce strategy for your destinations. The more balanced you can make this decision, the easier it will be for your destinations to make it into slower networks, or networks that are many hops away. 

Statistics and information about announce rates can be viewed using the `rnpath -r` and `rnstatus -A` commands. 

It is important to note, that while there is no one right or wrong way to set up announce rates, it should generally not be necessary to announce any kind of destination. more often than once every few hours. Most applications can announce simply when the application starts, and then only once every 6 hours or so. 

If you’re designing an application where you think you need to annonuce more often than once an hour, you’re most likely doing something wrong. 

Slower networks will naturally tend towards using less frequent announces to conserve bandwidth, while very fast networks can support applications that need more frequent announces. Reticulum implements these mechanisms to ensure that a large span of network types can seamlessly _co-exist_ and interconnect. 

## **8.18 New Destination Rate Limiting** 

On public interfaces, where anyone may connect and announce new destinations, it can be useful to control the rate at which announces for _new_ destinations are processed. 

If a large influx of announces for newly created or previously unknown destinations occur within a short amount of time, Reticulum will place these announces on hold, so that announce traffic for known and previously established destinations can continue to be processed without interruptions. 

After the burst subsides, and an additional waiting period has passed, the held announces will be released at a slow rate, until the hold queue is cleared. This also means, that should a node decide to connect to a public interface, announce a large amount of bogus destinations, and then disconnect, these destination will never make it into path tables and waste network bandwidth on retransmitted announces. 

## **Note** 

It’s important to remember that the ingress control works at the level of _individual sub-interfaces_ . As an example, this means that one client on a _TCP Server Interface_ cannot disrupt processing of incoming announces for other connected clients on the same _TCP Server Interface_ . All other clients on the same interface will still have new announces processed without interruption. 

By default, Reticulum will handle this automatically, and ingress announce control will be enabled on interface where it is sensible to do so. It should generally not be neccessary to modify the ingress control configuration, but all the parameters are exposed for configuration if needed. 

- The `ingress_control` option tells Reticulum whether or not to enable ingress control on the interface. Defaults to `True` . 

- The `ic_new_time` option configures how long (in seconds) an interface is considered newly spawned. Defaults to `2*60*60` seconds. This option is useful on publicly accessible interfaces that spawn new sub-interfaces when a new client connects. 

- The `ic_burst_freq_new` option sets the maximum announce ingress frequency for newly spawned interfaces. Defaults to `3.5` announces per second. 

**8.18. New Destination Rate Limiting** 

**117** 

**Reticulum Network Stack, Release 1.3.0** 

- The `ic_burst_freq` option sets the maximum announce ingress frequency for other interfaces. Defaults to `12` announces per second. 

   - _If an interface exceeds its burst frequency, incoming announces for unknown destinations will be temporarily held in a queue, and not processed until later._ 

- The `ic_max_held_announces` option sets the maximum amount of unique announces that will be held in the queue. Any additional unique announces will be dropped. Defaults to `256` announces. 

- The `ic_burst_hold` option sets how much time (in seconds) must pass after the burst frequency drops below its threshold, for the announce burst to be considered cleared. Defaults to `60` seconds. 

- The `ic_burst_penalty` option sets how much time (in seconds) must pass after the burst is considered cleared, before held announces can start being released from the queue. Defaults to `5*60` seconds. 

- The `ic_held_release_interval` option sets how much time (in seconds) must pass between releasing each held announce from the queue. Defaults to `30` seconds. 

All of the above settings can be configured both as instance-wide defaults under the `[reticulum]` section of the configuration file, or on a per- interface basis under the relevant interface configuration section. 

## **8.19 Path Request Burst Control** 

In addition the announce controls for newly created destination, Reticulum will also monitor incoming path request activity, and enforce burst controls if per-client rates exceed configured limits. Once path request burst control is activated on an interface, path requests will no longer be propagated further on the network. As with announce burst control, this happens on a per sub-interface basis. One client connecting to a public gateway will not be able to disrupt path request processing for other clients. 

## **Warning** 

Applications that send large amounts of unnecessary path requests will very quickly get rate limited by transport nodes, and the entire system they are running on will not be able to resolve any paths on the network, until the burst subsides and hold period expires. **Do not** write applications like this. Only request paths for destinations you need to communicate with. 

By default, Reticulum will handle this automatically, and ingress path request control will be enabled on interface where it is sensible to do so. It should generally not be neccessary to modify the ingress control configuration, but all the parameters are exposed for configuration if needed. 

- The `ingress_control` option tells Reticulum whether or not to enable ingress control on the interface. Defaults to `True` . 

- The `ic_new_time` option configures how long (in seconds) an interface is considered newly spawned. Defaults to `2*60*60` seconds. This option is useful on publicly accessible interfaces that spawn new sub-interfaces when a new client connects. 

- The `ic_pr_burst_freq_new` option sets the maximum path request ingress frequency for newly spawned interfaces. Defaults to `3` path requests per second. 

- The `ic_pr_burst_freq` option sets the maximum path request ingress frequency for other interfaces. Defaults to `8` path requests per second. 

_If an interface exceeds its burst frequency, incoming path requests from that system will not traverse the network further._ 

- The `egress_control` option enables hard-limiting path request egress control per-interface. Defaults to `False` 

**Chapter 8. Configuring Interfaces** 

**118** 

**Reticulum Network Stack, Release 1.3.0** 

- The `ec_pr_freq` option sets the hard limit for outbound path requests per second on a given interface. 

All of the above settings can be configured both as instance-wide defaults under the `[reticulum]` section of the configuration file, or on a per- interface basis under the relevant interface configuration section. 

**8.19. Path Request Burst Control** 

**119** 

**Reticulum Network Stack, Release 1.3.0** 

**Chapter 8. Configuring Interfaces** 

**120** 

**CHAPTER NINE** 

## **BUILDING NETWORKS** 

This chapter will provide you with the high-level knowledge needed to build networks with Reticulum. It will not, however tell you all you need to know to succesfully design and configure every kind of network you can imagine. For this, you will most likely need to read this manual in its entirity, invest significant time into experimenting with the stack, and learning functionality intuitively. 

Still, after reading this chapter, you should be well equipped to _start_ that journey. While Reticulum is **fundamentally different** compared to other networking technologies, it can often be easier than using traditional stacks. If you’ve built networks before, you will probably have to forget, or at least temporarily ignore, a lot of things at this point. It will all makes sense in the end though. Hopefully. 

If you’re used to protocols like IP, let’s at least start with some relief: You don’t have to worry about coordinating addresses, subnets and routing for an entire network that you might not know how will evolve in the future. With Reticulum, you can simply add more segments to your network when it becomes necessary, and Reticulum will handle the convergence of the entire network automatically. There’s plenty more neat aspects like that to Reticulum, but we’re getting ahead of ourselves. Let’s cover the basics first. 

## **9.1 Concepts & Overview** 

Before you start building your own networks, it’s important to understand the fundamental principles that distinguish Reticulum networks from traditional networking approaches. These principles shape how you design your network, what trade-offs you encounter, and what capabilities you can rely on. 

Reticulum is not a single network you “join”, it is a toolkit for _creating_ networks. You decide what mediums to use, how nodes connect, what trust boundaries exist, and what the network’s purpose is. Reticulum provides the cryptographic foundation, the transport mechanisms, and the convergence algorithms that make your design workable. You provide the intent and the structure. 

This approach offers tremendous flexibility, but it requires thinking in terms of different abstractions than those used in conventional networking. 

## **9.1.1 Introductory Considerations** 

There are important points that need to be kept in mind when building networks with Reticulum: 

- In a Reticulum network, any node can autonomously generate as many addresses (called _destinations_ in Reticulum terminology) as it needs, which become globally reachable to the rest of the network. There is no central point of control over the address space. 

- Reticulum was designed to handle both very small, and very large networks. While the address space can support billions of endpoints, Reticulum is also very useful when just a few devices needs to communicate. 

- Low-bandwidth networks, like LoRa and packet radio, can interoperate and interconnect with much larger and higher bandwidth networks without issue. Reticulum automatically manages the flow of information to and from various network segments, and when bandwidth is limited, local traffic is prioritised. You will, however, 

**121** 

**Reticulum Network Stack, Release 1.3.0** 

need to configure your interfaces correctly. If you tell Reticulum to pass all announce traffic from a gigabit link to a LoRa interfaces, it will try as best as possible to comply with this, while still respecting bandwidth limits, but you _will_ waste a lot of precious bandwidth and airtime, and your LoRa network will not work very well. 

- Reticulum provides sender/initiator anonymity by default. There is no way to filter traffic or discriminate it based on the source of the traffic. 

- All traffic is encrypted using ephemeral keys generated by an Elliptic Curve Diffie-Hellman key exchange on Curve25519. There is no way to inspect traffic contents, and no way to prioritise or throttle certain kinds of traffic. All transport and routing layers are thus completely agnostic to traffic type, and will pass all traffic equally. 

- Reticulum can function both with and without infrastructure. When _transport nodes_ are available, they can route traffic over multiple hops for other nodes, and will function as a distributed cryptographic keystore. When there is no transport nodes available, all nodes that are within communication range can still communicate. 

- Every node can become a transport node, simply by enabling it in it’s configuration, but there is no need for every node on the network to be a transport node. Letting every node be a transport node will in most cases degrade the performance and reliability of the network. 

_In general terms, if a node is stationary, well-connected and kept running most of the time, it is a good candidate to be a transport node. For optimal performance, a network should contain the amount of transport nodes that provides connectivity to the intended area / topography, and not many more than that._ 

- Reticulum is designed to work reliably in open, trustless environments. This means you can use it to create open-access networks, where participants can join and leave in a free and unorganised manner. This property allows an entirely new, and so far, mostly unexplored class of networked applications, where networks, and the information flow within them can form and dissolve organically. 

- You can just as easily create closed networks, since Reticulum allows you to add authentication to any interface. This means you can restrict access on any interface type, even when using legacy devices, such as modems. You can also mix authenticated and open interfaces on the same system. See the _Common Interface Options_ section of the _Interfaces_ chapter of this manual for information on how to set up interface authentication. 

Reticulum allows you to mix very different kinds of networking mediums into a unified mesh, or to keep everything within one medium. You could build a “virtual network” running entirely over the Internet, where all nodes communicate over TCP and UDP “channels”. You could also build such a network using other already-established communications channels as the underlying carrier for Reticulum. 

However, most real-world networks will probably involve either some form of wireless or direct hardline communications. To allow Reticulum to communicate over any type of medium, you must specify it in the configuration file, by default located at `~/.reticulum/config` . See the _Supported Interfaces_ chapter of this manual for interface configuration examples. 

Any number of interfaces can be configured, and Reticulum will automatically decide which are suitable to use in any given situation, depending on where traffic needs to flow. 

## **9.1.2 Destinations, Not Addresses** 

In traditional networking, addresses are allocated from a managed space. If you want to communicate with another node, you need to know its address, and that address must be unique within the network segment. This requires coordination, either through manual assignment, DHCP servers, or other allocation mechanisms. 

Reticulum replaces addresses with **destinations** . A destination is identified by a 16-byte hash (128 bits) derived from a SHA-256 hash of the destination’s identifying characteristics. This hash serves as the address on the network. On the network, it is represented in binary, but when displayed to human users, it will usually look something like this `<13425ec15b621c1d928589718000d814>` . 

**Chapter 9. Building Networks** 

**122** 

**Reticulum Network Stack, Release 1.3.0** 

The critical difference is that _any node can generate as many destinations as it needs, without coordination_ . A destination’s uniqueness is guaranteed by the collision resistance of SHA-256 and the inclusion of the node’s public key in the hash calculation. Two nodes can both use the destination name `messenger.user.inbox` , but they will have different destination hashes because their public keys differ. Both can coexist on the same network without conflict. 

This has profound implications for network design: 

- **No address allocation planning:** You never need to reserve address ranges, plan subnets, or coordinate with other network operators. Nodes simply generate destinations and announce them. 

- **Global portability:** A destination is not tied to a physical location or network segment. A node can move its destinations across interfaces, mediums, or even between entirely separate Reticulum networks simply by sending an announce on the new medium. 

- **Implicit authentication:** Because destinations are bound to public keys, communication to a destination is inherently cryptographically authenticated. Only the holder of the corresponding private key can decrypt and respond to traffic addressed to that destination. This also makes application-level authentication _much_ simpler, since it can directly use the foundational identity verification built into the core networking layer. 

- **Identity abstraction:** A single Reticulum Identity can create multiple destinations. This allows a single entity (a person, a device, a service) to present multiple endpoints without needing multiple cryptographic keypairs. 

## **9.1.3 Transport Nodes and Instances** 

Reticulum distinguishes between two types of nodes: **Instances** and **Transport Nodes** . Every node running Reticulum is an Instance, but not every Instance is a Transport Node. 

A **Reticulum Instance** is any system running the Reticulum stack. It can create destinations, send and receive packets, establish links, and communicate with other nodes. It can also host destinations that are connectable for _anyone_ else in the network. This means you can easily host globally available services from any location, including your home or office. Network-wide, global connectivity for all destinations is guaranteed, as long as there is _some_ physical way to actually transport the packets. Instances are the default state and are appropriate for most end-user devices, such as phones, laptops, sensors, or any device that primarily consumes network services. 

A **Transport Node** is an Instance that has been explicitly configured to participate in network-wide transport. Transport nodes forward packets across hops, propagate announces, maintain path tables, and serve path requests on behalf of other nodes. When a destination sends an announce, Transport Nodes receive it, remember the path, and rebroadcast it to other interfaces. When a node needs to reach a destination it doesn’t have a path for, Transport Nodes help resolve the path through the network. 

Even devices hosting services or serving content should probably just be configured as instances, and themselves connect to wider networks via a Transport Node. In some situations, this may not be practical though, and as an example, it is entirely viable to host a personal Transport Node on a Raspberry Pi, while it is at the same time running an LXMF propagation node, and hosting your personal site or files over Reticulum. 

The distinction is important. **Not** every node should be a Transport Node: 

- **Resource consumption:** Transport nodes maintain path tables, process announces, and forward traffic. This requires memory and CPU resources that may be limited on low-powered devices. 

- **Stability requirements:** Transport nodes contribute to network convergence. If Transport Nodes frequently go offline, path tables become stale and convergence suffers. Stable, always-on nodes make better Transport Nodes. 

- **Bandwidth considerations:** Transport nodes process and rebroadcast network maintenance traffic. On very low-bandwidth mediums, having too many Transport Nodes will consume capacity that should be used for actual data. 

In practice, a network typically has a relatively small number of Transport Nodes strategically placed to provide coverage and connectivity. End-user devices run as Instances, connecting through nearby Transport Nodes to reach the 

**9.1. Concepts & Overview** 

**123** 

**Reticulum Network Stack, Release 1.3.0** 

wider network. This pattern mirrors traditional networking where routers forward traffic while end hosts simply consume connectivity, but with the crucial difference that any node _can_ become a router if needed, and the decision is yours to make based on your network’s requirements. 

Transport nodes also function as distributed cryptographic keystores. When a destination announces itself, Transport Nodes cache the public key and destination information. Other nodes can request unknown public keys from the network, and Transport Nodes respond with the cached information. This eliminates the need for a central directory service while ensuring that public keys remain available throughout the network. 

## **9.1.4 Trustless Networking** 

Traditional network security models assume high levels of trust at specific layers. You might trust your ISP to deliver packets without inspection, or trust your VPN provider to handle your traffic, or trust the network administrator to configure firewalls appropriately. These trust relationships create vulnerabilities and dependencies. 

Reticulum is designed to function in **open, trustless environments** . This means the protocol makes no assumptions about the trustworthiness of the network infrastructure, the other participants, or the transport mediums. Every aspect of communication is secured cryptographically: 

- **Traffic encryption:** All traffic to single destinations is encrypted using ephemeral keys. 

- **Source anonymity:** Reticulum packets do not include source addresses. An observer intercepting a packet cannot determine who sent it, only who it is addressed to (unless IFAC is enabled, in which case nothing can be determined). This provides initiator anonymity by default. 

- **Path verification:** The announce mechanism includes cryptographic signatures that prove the authenticity of destination announcements. 

- **Unforgeable delivery confirmations:** When a destination proves receipt of a packet, the proof is signed with the destination’s identity key. This prevents false acknowledgments and ensures reliable delivery verification. 

- **Interface authentication:** When using Interface Access Codes (IFAC), packets on authenticated interfaces carry signatures derived from a shared secret. Only nodes with the correct network name and passphrase can generate valid packets, allowing creation of virtual private networks on shared mediums. 

The trustless design has important consequences for network design: 

- **Open-access networks are viable:** You can build networks that anyone can join without pre-approval. Because traffic is encrypted and authenticated end- to-end, participants cannot interfere with each other’s private communication, even if they share the same transport infrastructure. 

- **No traffic inspection or prioritization:** Because traffic contents and sources are opaque to intermediate nodes, there is no mechanism for filtering, prioritizing, or throttling traffic based on its type or origin. All traffic is treated equally. From a neutrality perspective, this is a feature. 

- **Adversarial resilience:** The network can operate even if some nodes are malicious or controlled by adversaries. While a malicious Transport Node could refuse to forward certain traffic or drop packets, it cannot decrypt, modify, or impersonate legitimate traffic. Redundant paths and multiple Transport Nodes mitigate the impact of malicious nodes. 

Of course, you can also create closed networks. Interface Access Codes allow you to restrict participation on specific interfaces. Network Identities enable you to verify that discovered interfaces belong to trusted operators. Blackhole management lets you block malicious identities. Reticulum provides both the tools for open networks and the controls for closed ones. The choice is yours based on your requirements. 

**Chapter 9. Building Networks** 

**124** 

**Reticulum Network Stack, Release 1.3.0** 

## **9.1.5 Heterogeneous Connectivity** 

In conventional networking, mixing different transport mediums typically requires gateways, translation layers, and careful configuration. A WiFi network doesn’t natively interoperate with a packet radio network without additional infrastructure, and you can’t just download a car over a serial port, or send an encrypted message in a QR code. 

Reticulum treats **heterogeneity as a core premise** . The protocol is designed to seamlessly mix mediums with vastly different characteristics: 

- **Bandwidth:** LoRa links operating at a few hundred bits per second can interconnect with gigabit Ethernet backbones. Reticulum automatically manages the flow of information, prioritizing local traffic on slow segments while allowing global convergence. 

- **Latency:** Satellite links with multi-second latency can coexist with local links measured in milliseconds. The transport system handles timing, asynchronous delivery and retransmissions transparently. 

- **Topology:** Point-to-point microwave links, broadcast radio networks, switched Ethernet fabrics, and virtual tunnels over the Internet can all be part of the same Reticulum network. 

- **Reliability:** Intermittent connections that come and go (such as mobile devices or opportunistic radio contacts) can participate alongside always-on infrastructure. Reticulum gracefully handles link loss and reconnection. 

This heterogeneity is achieved through several design elements: 

- **Expandable, medium-agnostic interface system:** Reticulum communicates with the physical world through interface modules. Adding support for a new medium is a matter of implementing an interface class. The protocol itself remains unchanged. 

- **Interface modes:** Different modes ( `full` , `gateway` , `access_point` , `roaming` , `boundary` ) allow you to configure how interfaces interact with the wider network based on their characteristics and role. 

- **Announce propagation rules:** Announces are forwarded between interfaces according to rules that account for bandwidth limitations and interface modes. Slow segments are not overwhelmed by traffic from fast segments. 

- **Local traffic prioritization:** When bandwidth is constrained, Reticulum prioritizes announces for nearby destinations. This ensures that local connectivity remains functional even when global convergence is incomplete. 

For network designers, this means you are free to use whatever mediums are available, affordable, or appropriate for your situation. You might use LoRa for wide-area low-bandwidth coverage, WiFi for local high-capacity links, I2P for anonymous Internet connectivity, and Ethernet for infrastructure backhauls, all within the same network. Reticulum handles the translation and coordination automatically. 

The key design consideration is not whether different mediums can work together (they can), but **how** they should work together based on your goals. A node with multiple interfaces spanning heterogeneous mediums needs to be configured with appropriate interface modes so that traffic flows efficiently. A gateway connecting a slow LoRa segment to a fast Internet backbone should be configured differently than a mobile device roaming between radio cells. 

**9.1. Concepts & Overview** 

**125** 

**Reticulum Network Stack, Release 1.3.0** 

**Chapter 9. Building Networks** 

**126** 

**CHAPTER TEN** 

## **DISTRIBUTED DEVELOPMENT** 

This chapter of the manual provides the conceptual basis for understanding _why_ `rngit` exists, what it aims to achieve, and the kinds of spaces it seeks to reestablish. For the practical details of operating the system, refer to the _Git Over Reticulum_ chapter. 

## **10.1 The Original Architecture** 

When Torvalds created Git in 2005, he designed a tool that reflected a specific philosophy of collaboration. Every copy of a repository would be a complete, sovereign instance. There was no central server, no single point of failure, no gatekeeper. Developers would be able to work independently, exchange patches directly, and maintain their own branches indefinitely. This concept was - and is - both beautiful and revolutionary. It’s execution is peer-to-peer not as a marketing term, but in the most foundational sense: As fundamental, structural reality. 

Such a design emerged from necessity. The Linux kernel development process operated across geographical boundaries, time zones, and organizational affiliations. Contributors did not “log in” to a shared server to do their work; they maintained their own trees, and the flow of code between these trees was negotiated through patches, reviews, and merge decisions. The architecture of Git mirrored the social architecture of the community: Autonomous, competent, and fundamentally distributed in its technical operation. 

_The result of that work is, in the most direct sense, what makes it possible for you to read this today._ 

There’s something very important to take note of here: With Git, developers could collaborate effectively and perfectly well without any central server being present, without platform-mediated visibility into each other’s work, and without a centralized authority validating their contributions. They needed _only_ a protocol for exchanging differences and a mechanism for verification of authorship. Everything else - social organization, quality control, release management - was handled by careful _human judgment_ operating on top of the technical substrate. 

What Git provided was not a development environment, but a **language for versioning** . It specified how to represent history, how to compute differences, how to merge divergent branches. It did not specify who could participate, how they should communicate, or what workflows they should follow. These were left to the competence and discretion of the creators using the system. 

## **10.2 The Platform Interregnum** 

What followed represents a very familiar pattern: Tools designed to distribute power were re-centralized by platforms that offered convenience in exchange for control. GitHub, GitLab, and similar services reintroduced the centralization that Git had eliminated architecturally. The activity feed replaced durable artifacts with ephemeral notifications. The social graph and open interaction became as important as the code itself, if not more. 

This re-centralization was not technical, as such. It was **ontological** . When every developer pushes to the same server, when every merge is in theory controllable by a platform, when every issue is tracked in a database controlled by a corporation, the nature of collaboration changes. The platform, and its social dynamics, becomes the ground of reality. 

**127** 

**Reticulum Network Stack, Release 1.3.0** 

The platform mediates not just the technical exchange of information and the programmatics, but the social recognition and codices of contribution, the future archival prospects of the work, and the very identity of the project itself. 

The consequences extend beyond individual inconvenience. Centralized platforms create single points of failure for entire ecosystem. When a platform changes its terms of service, suspends accounts, removes repositories or ceases operation, entire project histories and community relationships can be disrupted or destroyed. The extractive economics of platform capitalism mean that value created by open-source communities is captured by corporations, while communities remain dependent on infrastructure they do not control. And the surveillance inherent in platform operation means that every action - every commit, every comment, every page view - is logged, analyzed, and potentially monetized or weaponized. 

More insidiously, platforms have completely reshaped the culture of development itself. They have created what we could call the **Teahouse Developer** : A participant who treats engineering projects as social venues for opinion-sharing rather than sites of disciplined and careful production. These personages have no actual stakes in the projects they act as leeches upon, and only a very base consciousness of the damage they are incurring in order to feed their attention and external validation dependencies. 

When platforms optimize for engagement, when growth is the only metric, when every user with an opinion must have their voice heard, when a random social process is elevated to higher importance than results, the signal-to-noise ratio collapses catastrophically. Competent engineers find themselves drowning in feedback from the incompetent, managing the emotional needs and dysregulations of drive-by commentators rather than solving technical problems. 

The platform model is predicated on **unsaturable expansion** . Like almost any industrial system, it cannot function without growth. It pursues no particular aims; it is growth for the sake of growing. There is no saturation point, no concept of “enough”. Every barrier to entry must be put down to the very lowest common denominator, every voice must be amplified, every interaction must be converted into content that feeds the machine. This is fundamentally incompatible with the nature of social beings itself. It is also incompatible with serious engineering, which requires focus, discernment, and the right of people who know better to say “no”. 

## **10.3 Restoration** 

The `rngit` system represents a return to Git’s original architectural principles, fortified with cryptographic networking capabilities that were not available in 2005. The `rngit` system _is_ Git - but running over Reticulum. Welcome back to a world where your work is your own, but where everyone can still reach you - if you want them to. 

Just as Git eliminated the need for a central version control server, `rngit` eliminates the need for a central hosting platform, “servers” or any kinds of middle-men between the people actually doing the work. By operating over Reticulum, it eliminates the visibility of development activity to platform operators, network observers, state actors and other malicious third-parties. 

In this model, the repository node is a **sovereign entity** . It is reachable from anywhere in the Reticulum network but owned, operated, and controlled by the developer or community that runs it. It is an actual home for creative output, not an extraction mechanism to which dues are paid. The node operator decides who may contribute, what standards must be met, and which voices are worth listening to. This is not exclusion; it is **discernment** . It is the necessary exercise of judgment that separates engineering from theatrics. 

I did not create this in a fit of nostalgia. I created it because it is a necessary response to the failures of the centralized model. Git’s technical architecture was - and _is_ - correct. It was the social and economic superstructure built atop it that introduced fragility, exploitation, and environments toxic to actual creativity. By returning to first principles - distributed version control on distributed infrastructure - we recover not just a technical capability, but a mode of collaboration that respects the autonomy of individual developers and the sovereignty of actual communities. 

**Chapter 10. Distributed Development** 

**128** 

**Reticulum Network Stack, Release 1.3.0** 

## **10.4 Protocols Over Platforms** 

The distinction between platforms and protocols is fundamental to understanding the architecture of sovereignty in networked systems. A platform is a service you access; a protocol is a grammar you speak; actions you live. A platform requires permission to enter, a protocol requires only _comprehension_ to employ. A platform can change its rules, suspend your account, or cease operation entirely, a protocol persists as long as there are participants who _understand_ and _use_ it. A protocol is an _idea_ , a platform is a machine that turns its users into products. 

Platforms operate on a client-server model that inherently creates power asymmetry. Even when platforms are built atop open-source software, the operational instance remains a black box of corporate control. You _may_ be able to download _some_ of your data, but you cannot download the connections to the people that are the true value-base of the platform, or take them with you if you want to leave. 

Protocols, by contrast, are agreements. They specify how systems should communicate, but not who may communicate or on what terms. Email is a protocol; Gmail is a platform. HTTP is a protocol; Facebook is a platform. Git is a protocol; GitHub is a platform. The protocol persists regardless of any particular implementation’s success or failure. 

The power of protocols lies in their **permissionlessness** . Anyone can implement a protocol without approval. Anyone can extend it, fork it, or use it for purposes unforeseen by its creators. This creates resilience: protocols cannot be easily censored, monopolized, or shut down because they exist as shared understanding rather than centralized infrastructure. 

Reticulum is a protocol in this strict sense. It specifies how packets should be formatted, how paths should be discovered, how encryption should be applied. The `rngit` system extends this protocol approach to development workflows. It is not an external platform that hosts your repositories; it is a protocol for exchanging repository data, release artifacts, and work documents over Reticulum’s encrypted transport. But with a few commands and an old computer, it creates your own infrastructure for hosting repositories, or sharing them with who you choose. _That_ is how tools should function, in case we had forgotten. 

Unlike platforms, which extract value by creating dependency, there is no entity that can grant or deny you the privilege of running `rngit` . Your Reticulum identity is not endowed by any platform; it is generated locally and certified by its own cryptographic properties. Your repositories are hosted on nodes you control or nodes operated by communities you trust. Your relationships with other developers are peer-to-peer connections established through cryptographic addressing, not social graph connections managed by recommendation algorithms. 

On a platform, exit means abandonment: you lose your history, your relationships, your visibility. With protocols, exit is just migration. When you change your infrastructure, your identity and your work travel with you. There are no middlemen between you and your collaborators. If push comes to shove, you can write your entire life’s work and connections to an SD card, swim across the lake, and set up camp on the other side. 

## **10.5 Sovereignty Through Infrastructure** 

The concept of sovereignty - supreme authority within a territory - has traditionally been applied to nation-states. But in an age where creative work is conducted through digital infrastructure, sovereignty is essential for individuals and communities. **Creative sovereignty** means having supreme authority over the artifacts you produce, the processes by which you produce them, and the terms under which they are distributed. It means not merely legal ownership of copyright, but operational control of the infrastructure that mediates creation, collaboration, and dissemination. 

Centralized development platforms strip away most layers of sovereignty. When you host code on a corporate platform, you retain _some_ legal ownership of copyright, but you surrender complete operational control. The platform decides what content is acceptable, who can access it, and how it is presented. They can delete your repository, suspend your account, or change the visibility of your work without consent. In reality, legal ownership becomes meaningless as operational control is ceded. 

Running your own `rngit` node restores this sovereignty. You control the hardware, the network configuration, the backup strategies, and the access permissions. You decide what constitutes acceptable use, who may contribute, and how contributions are evaluated. Taking this responsibility on yourself is an assertion that your creative work is not a product to be harvested by platform economics, but an autonomous activity to be conducted on your own terms. 

**10.4. Protocols Over Platforms** 

**129** 

**Reticulum Network Stack, Release 1.3.0** 

This sovereignty and responsibility extends to the entry barriers you establish. The `rngit` system allows you to configure access controls that filter participants based on cryptographic identity and demonstrated competence. If, for example, someone cannot navigate a command line, or use Reticulum to submit a patch, they most likely lack the required competence to modify your code. In a world that apparently labels this as “exclusion”, I would simply refer to it as a minimally acceptable level of quality control. 

Such a stance protects projects from the noise that so often overwhelms and completely dilutes platform-based development, where every user with an opinion believes themselves entitled to attention and access to the decision process. 

## **10.6 Artifact-Centered Workflows** 

Contemporary platform-based development has shifted focus from durable artifacts to ephemeral _activity_ . It does not matter what constitutes this activity, as long as it’s there. The primary interface is not the repository itself, not the produced artifacts, but the activity feed: _Notifications_ of commits, comments, pull requests, and social interactions. Work is measured by velocity, throughput, and the constant stream of updates. This activity-centric model creates constant urgency, discourages discernment, encourages reactive rather than reflective work patterns, and produces vast quantities of ephemeral and useless communication that obscures actual project state and productivity. 

The `rngit` system enables a return to **artifact-centered workflows** , where the focus is on durable, attributable, versioned outputs rather than the stream of notifications surrounding them. The fundamental unit of work is the commit - signed, immutable records of change. The fundamental unit of production is the signed artifact - a self-verifying package of functionality. The fundamental unit of discussion is the work document - a structured, threaded conversation attached to repositories. 

Artifacts can persist independently of any platform’s continued operation. A commit signed with your Reticulum identity is attributable to you regardless of where it is stored. A release signed with your private key is verifiable as authentic regardless of which network it traverses, and can be verified offline on any system running Reticulum. The work exists as **cryptographic fact** , distributed over the planet, not as database entries in a corporate cloud. 

Such a shift has real psychological consequences. When work is measured in artifacts rather than activity, the pace changes. There is no need for constant visibility, no pressure to perform busyness. Developers can work deeply, reflectively, and submit complete solutions rather than incremental updates designed to maintain presence in an activity feed. The work becomes **substantial** , in the physical sense of the word, rather than performative. 

## **10.7 Composable Primitives** 

The `rngit` system is not a monolithic application prescribing a specific workflow; it is a collection of **composable primitives** that can be arranged to support diverse creative processes. Understanding these primitives as separate, orthogonal capabilities enables users to construct workflows suited to their specific needs and to recombine these primitives in ways unforeseen by the system’s designers. 

The core primitives include: 

- **Repository Hosting** : Bare Git repositories served over Reticulum links, accessible via standard Git commands through the `rns://` URL scheme. 

- **Identity-Based Access Control** : Fine-grained permissions managed through cryptographically verifiable identity hashes, configurable at the group, repository, or document level. 

- **Release Distribution** : Cryptographically signed release artifacts with embedded provenance information, verifiable offline and distributable through any Reticulum or physical path. 

- **Work Document Tracking** : Structured, threaded work management attached to repositories, with precise permission controls, and the ability to contain updates or discussions. 

- **Forking and Mirroring** : Automated replication of repositories from any accessible Git URL, with metadata tracking upstream relationships for synchronization. 

**Chapter 10. Distributed Development** 

**130** 

**Reticulum Network Stack, Release 1.3.0** 

- **Nomad Network Integration** : Page node functionality for browsing repository contents, commit history, and release information through the Nomad Network protocol. 

These primitives can be composed into workflows ranging from single-developer projects to complex multiorganizational collaborations. A solo developer might use only repository hosting and release distribution. A research group might add work document tracking for structured peer review. A software distribution network might combine mirroring with cryptographic release verification to create resilient update channels. 

The entire system is incredibly light-weight, and can host hundreds of repositories on a Raspberry Pi. 

Composability is essential because **creative work is diverse** . Software development, academic research, technical writing, hardware design, music production and data analysis all have different requirements for collaboration, review, and distribution. A platform prescribes a single workflow and forces all users to conform. A protocol provides primitives and allows users to construct workflows appropriate to their domain. 

With `rngit` , you can re-build the system into anything you can imagine. Everything can be modified, extended and hooked into. Adding functionality or automation is never further away than a shell script, a cron-job, or a Python modification of the source. 

## **10.8 Distribution Without Intermediaries** 

Creating software is only part of the work. Then comes actually getting it to the people needing to use it. Centralized platforms handle distribution through their own infrastructure: Content delivery networks, central package registries, and download servers accessed through platform-controlled interfaces. This convenience masks a fundamental dependency: Your ability to distribute depends on the platform’s continued operation, their policies regarding your content, and their technical infrastructure’s reach. 

The `rngit` release system enables distribution strategies **decoupled from any single infrastructure provider** . Releases are cryptographically signed using Ed25519 signatures and packaged in signed release manifests ( `.rsm` files). These manifests contain embedded signatures for each artifact. The manifest provides full verifiability of all release information, and contains embedded release artifact lists, per-file `.rsg` signatures, origin information, and the creator’s Reticulum Identity. It can also be used to fetch verified updates of the software package over the network, and can always be verified completely offline. 

Because releases are self-verifying, they can traverse any network or physical path that Reticulum can establish. A release can travel over LoRa radio, be carried on USB drives through areas without internet connectivity, disseminated over a mirror network, or be distributed through store-and-forward mechanisms on intermittent infrastructure. Recipients can verify authenticity regardless of how they obtained the files. This is particularly valuable in low-connectivity environments where Reticulum may be the only available communication channel. 

The `rngit release` command provides tools for creating, publishing, fetching, and verifying releases. When fetching a release using an `.rsm` manifest, the system validates the manifest signature against the required Reticulum Identity, extracts the origin node and repository path, connects to the origin over Reticulum, retrieves the latest release manifest, and verifies each downloaded artifact against the signatures embedded in the manifest. If any verification fails, the fetch aborts, preventing installation of corrupted or tampered files. 

This cryptographic verification replaces the trust model of platform distribution. Instead of trusting that a platform has not been compromised, users verify that artifacts match the signatures created by the developer’s identity. It doesn’t matter _how_ they obtained the artifacts, they can **always** be verified. This security model shifts from **institutional trust** (just believe in the goodness of the platform) to **cryptographic proof** (verify the signatures). 

## **10.9 Long Archive** 

Software development is often conceived as an activity of the present only: Solving today’s problems, meeting current deadlines, responding to immediate feedback. But the artifacts produced - code, documentation, releases - have lifespans extending _far_ beyond their creation. They may be used for decades, studied by future developers, depended upon by systems not yet imagined, or preserved as historical records of technological development. 

**10.8. Distribution Without Intermediaries** 

**131** 

**Reticulum Network Stack, Release 1.3.0** 

The `rngit` system is designed with this **extended timeframe** in mind, supporting the creation of archives that are durable, portable, and intelligible across generational timescales. Git repositories are always internally complete; they contain full history and can be migrated to new infrastructure without loss of information. Everything that `rngit` adds on top of this is stored in normal files in standard formats right next to the Git repository folders, not an esoteric database-cluster two thousand kilometers away. Because releases are cryptographically signed, they remain verifiable as authentic regardless of when or where they are retrieved. Because the system operates over Reticulum, it can function over communication mediums that may outlast the internet as we know it. 

This long-term perspective influences technical decisions. The use of well-established cryptographic primitives ensures that signatures will remain verifiable for centuries. The use of standard formats ensures that repositories will remain readable by future tools. The protocol-based architecture ensures that the system can evolve without losing compatibility with existing data. 

For critical infrastructure, this archival durability is not optional; it is essential. Communication systems, cryptographic libraries, and safety-critical code must remain available and verifiable for the lifespans of the systems that depend on them. The `rngit` system provides the tools to create such archives: distributed across multiple nodes, cryptographically verified, and independent of any corporate or governmental infrastructure, which as history has shown repeatedly, does _not_ persist. 

## **10.10 Start Of The Road** 

Distributed development and production over Reticulum is a _different mode of existence_ for creative work. It restores the autonomy originally created by Git. It provides local sovereignty over production infrastructure, composability of workflow, and durability of artifact. It lets you filter participation through competence and cryptography rather than incentives of platform operators, raising the quality and enjoyment of work, and protecting the focus of real engineering and creative expression. 

This is not a system for everyone, and that is the point. It requires investment - in understanding Reticulum, in configuring infrastructure, in establishing workflows. It requires accepting responsibility for your own tools rather than delegating them to platform operators. It requires the discipline to maintain your own node, manage your own backups, and nurture your own community. 

But for those who make this investment, the returns are substantial. You gain **immunity from platform failure** ; your work persists regardless of corporate decisions or service outages. You gain **shelter from surveillance** ; your development activity is visible only to those that _you_ choose to involve. You gain **control over process** ; you decide how work is conducted, reviewed, and released, unmediated by terms of service, algorithmic feeds and thousands of uninformed and irrelevant opinions. 

Most importantly, though, you regain the **dignity of craft** . Development becomes an activity conducted among peers, equals among equals, mediated by skill and cryptographic proof rather than corporate permission, producing artifacts that stand as independent testimony to competence, functionality or beauty rather than as content feeding engagement metrics. The _work_ becomes the point. The artifacts become durable. And the network becomes _one_ of the tools you wield in this endeavor. 

**Chapter 10. Distributed Development** 

**132** 

**CHAPTER ELEVEN** 

## **GIT OVER RETICULUM** 

This chapter of the manual serves as the technical reference for the distributed software development and project collaboration tools included in RNS. For a conceptual overview, see the _Distributed Development_ chapter. 

A set of utilities for distributed collaborative software development and publishing are included in RNS. 

The system consists of two parts: The `rngit` node that hosts repositories, and the `git-remote-rns` helper that enables Git to communicate with rngit nodes. As soon as you have RNS installed on your system, you can transparently use Git with Reticulum-hosted repositories just like any other type of remote. Git over Reticulum uses URLs in the following format: `rns://DESTINATION_HASH/group/repo` . 

If you set a branch to track a Reticulum remote as the default upstream, you can simply use `git` as you normally would; all commands work transparently and as expected. 

## **Important** 

**The rngit program is a new addition to RNS!** This functionality was introduced in RNS 1.2.0. While great care has been taken to design a secure, but highly configurable and flexible _permission system_ for allowing many users to interact with many different repositories on a single node, `rngit` has not been tested extensively in the wild! Be careful when hosting repositories, especially if they are public or semi-public. 

## **11.1 The rngit Utility** 

The `rngit` utility provides full Git repository hosting and interaction over Reticulum. It allows you to host and manage Git repositories and releases on Reticulum nodes, and to interact with remote repositories using standard Git commands through the `rns://` URL scheme. 

## **Usage Examples** 

Run `rngit` to start a repository node: 

```
$rngit
```

```
[Notice]StartingReticulumGitNode...
```

```
[Notice]ReticulumGitNodelisteningon<0d7334d411d00120cbad24edf355fdd2>
```

On the first run, `rngit` will create a default configuration file. You will then need to edit this, to point to your repository locations, configure access permissions, and perform any other necessary configuration. 

Them, view your identity and destination hashes: 

```
$rngit--print-identity
```

(continues on next page) 

**133** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
GitPeerIdentity:<959e10e5efc1bd9d97a4083babe51dea>
RepositoryNodeIdentity:<153cb870b4665b8c1c348896292b0bad>
RepositoriesDestination:<0d7334d411d00120cbad24edf355fdd2>
```

If the page node is enabled, the output will also include the Nomad Network destination hash. 

You can run `rngit` in service mode with logging to file: 

```
$rngit-s
```

Clone a repository from a remote `rngit` node: 

```
$gitclonerns://50824b711717f97c2fb1166ceddd5ea9/public/myrepo
```

Add a Reticulum remote to an existing repository: 

```
$gitremoteaddsome_remoterns://50824b711717f97c2fb1166ceddd5ea9/public/myrepo
```

Push changes to the Reticulum remote: 

```
$gitpushsome_remotemaster
```

Get changes from a remote repository: 

```
$gitpullrns_remotemaster
```

Fork an existing repository from a remote to your `rngit` node: 

`$ rngit fork rns://8a37cdd16938ce79861561adbd59023a/reticulum/lxmf rns://` _˓→_ `50824b711717f97c2fb1166ceddd5ea9/public/myfork` 

## **All Command-Line Options (rngit)** 

```
usage:rngit.py[-h][--configCONFIG][--rnsconfigRNSCONFIG][-s][-i][-v]
[-q][--version]
```

```
ReticulumGitRepositoryNode
```

```
options:
-h,--helpshowthishelpmessageandexit
--configCONFIGpathtoalternativeconfigdirectory
--rnsconfigRNSCONFIG
pathtoalternativeReticulumconfigdirectory
-p,--print-identityprintidentityanddestinationinfoandexit
-s,--servicerngitisrunningasaserviceandshouldlogtofile
-i,--interactivedropintointeractiveshellafterinitialisation
-v,--verboseincreaseverbosity
-q,--quietdecreaseverbosity
--versionshowprogram'sversionnumberandexit
```

## **All Command-Line Options (git-remote-rns)** 

The `git-remote-rns` helper is automatically invoked by Git when interacting with `rns://` URLs. It is not typically run directly by users, but accepts the following environment variables for configuration: 

- `RNGIT_CONFIG` - Path to alternative client configuration directory 

**Chapter 11. Git Over Reticulum** 

**134** 

**Reticulum Network Stack, Release 1.3.0** 

- `RNS_CONFIG` - Path to alternative Reticulum configuration directory 

The client configuration file is located at `~/.rngit/client_config` and allows adjusting parameters such as the reference batch size for transfers. 

## **11.2 Repository Creation & Management** 

The `rngit` utility provides several ways to create and manage repositories on a node: creating empty repositories, forking from existing repositories, and mirroring remote repositories. 

## **11.2.1 Creating Empty Repositories** 

To create a new empty repository on a remote node: 

```
$rngitcreaterns://50824b711717f97c2fb1166ceddd5ea9/public/myrepo
```

```
Repositorypublic/myrepocreated
```

This creates a bare Git repository at the specified path. You must have `create` permission for the target group. When a repository is created, the creator automatically receives `adm` (admin) permissions on the repository through an autogenerated `.allowed` file. 

## **All Command-Line Options (rngit create)** 

```
usage:rngitcreate[-h][--configCONFIG][--rnsconfigRNSCONFIG]
[-iPATH][-v][-q][--version]
repository
ReticulumGitRepositoryCreation
positionalarguments:
repositoryURLofrepositorytocreate
options:
-h,--helpshowthishelpmessageandexit
--configCONFIGpathtoalternativeconfigdirectory
--rnsconfigRNSCONFIG
pathtoalternativeReticulumconfigdirectory
-i,--identityPATHpathtoidentity
-v,--verbose
-q,--quiet
--versionshowprogram'sversionnumberandexit
```

## **11.2.2 Forking Repositories** 

Forking creates a copy of an existing repository (from any accessible Git URL) on your `rngit` node. Forks maintain a reference to their upstream source for later synchronization. 

To fork a repository: 

`$ rngit fork https://github.com/user/original rns://50824b711717f97c2fb1166ceddd5ea9/` _˓→_ `public/myfork` 

```
Repositoryforkedtopublic/myfork
```

**11.2. Repository Creation & Management** 

**135** 

**Reticulum Network Stack, Release 1.3.0** 

The source can be any valid Git URL, including: 

- HTTPS URLs: `https://github.com/user/repo.git` 

- SSH URLs: `ssh://git@host.com/repo.git` 

- Reticulum URLs: `rns://DESTINATION_HASH/group/repo` 

Forks are created as bare repositories with metadata tracking their origin. The fork process: 

1. Creates a new bare repository 

2. Fetches all refs ( `+refs/*:refs/*` ) from the source 

3. Sets `repository.rngit.type` to `fork` 

4. Sets `repository.rngit.upstream.source` to the source URL 

5. Grants creator admin permissions 

## **All Command-Line Options (rngit fork)** 

```
usage:rngitfork[-h][--configCONFIG][--rnsconfigRNSCONFIG]
[-iPATH][-v][-q][--version]
sourcetarget
ReticulumGitRepositoryForker
positionalarguments:
sourceURLofsourcerepository
targetURLoftargetrepository
options:
-h,--helpshowthishelpmessageandexit
--configCONFIGpathtoalternativeconfigdirectory
--rnsconfigRNSCONFIG
pathtoalternativeReticulumconfigdirectory
-i,--identityPATHpathtoidentity
-v,--verbose
-q,--quiet
--versionshowprogram'sversionnumberandexit
```

## **11.2.3 Mirroring Repositories** 

Mirrors are similar to forks but are designed for keeping a local copy synchronized with an upstream repository. Mirrors can be automatically updated on a configurable schedule. 

To create a mirror: 

`$ rngit mirror https://github.com/user/upstream rns://50824b711717f97c2fb1166ceddd5ea9/` _˓→_ `public/mymirror` 

```
Repositorymirroredtopublic/mymirror
```

Mirrors are created with the same process as forks, but with `repository.rngit.type` set to `mirror` and an additional `repository.rngit.upstream.sync` timestamp tracking the last successful synchronization. 

## **All Command-Line Options (rngit mirror)** 

**Chapter 11. Git Over Reticulum** 

**136** 

**Reticulum Network Stack, Release 1.3.0** 

```
usage:rngitmirror[-h][--configCONFIG][--rnsconfigRNSCONFIG]
[-iPATH][-v][-q][--version]
sourcetarget
ReticulumGitMirrorManagement
positionalarguments:
sourceURLofsourcerepository
targetURLoftargetrepository
options:
-h,--helpshowthishelpmessageandexit
--configCONFIGpathtoalternativeconfigdirectory
--rnsconfigRNSCONFIG
pathtoalternativeReticulumconfigdirectory
-i,--identityPATHpathtoidentity
-v,--verbose
-q,--quiet
--versionshowprogram'sversionnumberandexit
```

## **11.2.4 Automatic Mirror Synchronization** 

The `rngit` node can automatically keep mirrors synchronized with their upstream sources. This is configured in the main configuration file: 

```
[rngit]
mirror_interval=24
```

The `mirror_interval` specifies the synchronization interval in hours (default: 24). The node checks for mirrors needing sync every 15 minutes, and fetches updates from upstream if the configured interval has elapsed since the last sync. 

For automatic sync to happen, the repository must have been created with `rngit mirror` . Sync failures are logged but do not prevent future retry attempts. The sync timestamp is only updated on successful completion. 

## **11.2.5 Manual Synchronization** 

Both forks and mirrors can be manually synchronized on demand using the `sync` command: 

```
$rngitsyncrns://50824b711717f97c2fb1166ceddd5ea9/public/myfork
Repositorysynced
```

This fetches all refs from the upstream source configured when the repository was created. You must have `read` and `write` permissions for the repository to perform a manual sync. 

For mirrors, manual sync also updates the sync timestamp, effectively resetting the automatic sync timer. 

## **All Command-Line Options (rngit sync)** 

```
usage:rngitsync[-h][--configCONFIG][--rnsconfigRNSCONFIG]
[-iPATH][-v][-q][--version]
repository
```

(continues on next page) 

**11.2. Repository Creation & Management** 

**137** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
ReticulumGitRepositorySyncer
positionalarguments:
repositoryURLofrepository
options:
-h,--helpshowthishelpmessageandexit
--configCONFIGpathtoalternativeconfigdirectory
--rnsconfigRNSCONFIG
pathtoalternativeReticulumconfigdirectory
-i,--identityPATHpathtoidentity
-v,--verbose
-q,--quiet
--versionshowprogram'sversionnumberandexit
```

## **11.2.6 Git Configuration Parameters** 

Repositories created through `rngit` store metadata in Git configuration: 

- `repository.rngit.type` - Either `fork` or `mirror` 

- `repository.rngit.upstream.source` - The source URL used during creation 

- `repository.rngit.upstream.sync` - Unix timestamp of last successful sync for mirrors 

These parameters are used by the sync system and can be queried using standard Git commands: 

```
$gitconfig--getrepository.rngit.type
mirror
$gitconfig--getrepository.rngit.upstream.source
https://github.com/user/upstream
$gitconfig--getrepository.rngit.upstream.sync
1716230400
```

## **11.3 Repository Structure** 

The `rngit` node organizes repositories into groups. Each group is a directory containing bare Git repositories. The repository path format is `group_name/repo_name` . For example, a repository at `/var/git/public/myrepo` would be accessible as `public/myrepo` via the URL `rns://DESTINATION_HASH/public/myrepo` . 

## **11.3.1 Configuration** 

The `rngit` node configuration file is located at `~/.rngit/config` (or `/etc/rngit/config` for system-wide installations). The default configuration includes: 

- Repository group paths defining where to find bare repositories 

- Access permissions for groups and individual repositories 

- Announce intervals for network visibility 

- Optional statistics recording for repository activity 

**Chapter 11. Git Over Reticulum** 

**138** 

**Reticulum Network Stack, Release 1.3.0** 

## **11.4 Permissions** 

The `rngit` permission system provides fine-grained access control at multiple levels: group-level, repository-level, and document-level. Permissions can be statically configured in files or dynamically generated via executable scripts. 

Access permissions can be configured at the group level in the config file or per-group `.allowed` files, or per-repository `.allowed` files. The `s` (stats) permission allows viewing repository activity statistics, including views, fetches and pushes over time. To enable statistics recording, set `record_stats = yes` in the `[rngit]` section of the configuration file. You can also exclude specific identities from statistics by adding their hashes to `stats_ignore_identities` . 

By default, **no** permissions are granted for anything! You will have to enable the permissions you require to be able to actually _do_ something with `rngit` . 

Permissions can be modified by editing the `rngit` config file, individual `.allowed` files on disk, or remotely using the `rngit perms` command. 

## **11.4.1 Permission Types** 

The following permissions are supported: 

- `r` (read) - Clone, fetch, and view repositories and work documents 

- `w` (write) - Push changes and manage work documents 

- `rw` (read/write) - Combined read and write access 

- `c` (create) - Create, fork or mirror new repositories within a group 

- `s` (stats) - View repository activity statistics 

- `rel` (release) - Create and manage releases 

- `i` (interact) - Comment on and interact with work documents 

- `p` (propose) - Propose new work documents (without full write access) 

- `adm` (admin) - Full access 

Permission targets can be: 

- `all` or `a` - Everyone 

- `none` or `n` - Nobody 

- A specific Reticulum identity hash 

## **11.4.2 Permission Hierarchy** 

Permissions are resolved in the following hierarchy: 

1. **Repository-level permissions** - Checked first, if none exists group permissions are checked 

2. **Group-level permissions** - Used as fallback if no repository-level permissions are set 

3. **Admin override** - Finally, potential admin rights are checked 

For work documents, work document specific permissions are always checked first, and work documents have additional specific checks such as modifications only being possible by the document author. 

**11.4. Permissions** 

**139** 

**Reticulum Network Stack, Release 1.3.0** 

## **11.4.3 Configuration Methods** 

## **Group-Level Configuration** 

Group permissions can be configured in the `[access]` section of the main config file: 

```
[access]
public=r:all,w:9710b86ba12c42d1d8f30f74fe509286
internal=rw:9710b86ba12c42d1d8f30f74fe509286
collaborative=r:all,i:all,p:all,w:9710b86ba12c42d1d8f30f74fe509286
```

Additionally, they can be configured in a group `group_name.allowed` file, placed next to the `group_name` group directory. 

## **Repository-Level Configuration** 

Repository-specific permissions are set in `.allowed` files placed next to the repository directory (for example, `myrepo. allowed` for `myrepo` ): 

```
#myrepo.allowed
r:all
w:9710b86ba12c42d1d8f30f74fe509286
rel:9710b86ba12c42d1d8f30f74fe509286
```

## **Dynamic Permissions** 

Permission files can be made executable to generate permissions dynamically: 

```
$chmod+xmyrepo.allowed
```

When executable, the script is run and its stdout is parsed as permission rules. This allows integration with external authentication systems. 

## **11.4.4 Work Document Permissions** 

Work documents support additional permission granularity through `.allowed` files in the work directory (e.g., `42. allowed` for document #42). These files use the same permission syntax but only support: 

- `r` (read) - View the document 

- `w` (write) - Edit the document 

- `i` (interact) - Comment on the document 

- `p` (propose) - Propose changes (future use) 

- `adm` (admin) - Full control over the document 

Document permissions override repository permissions for that specific document. Work document permissions can be updated simply by editing the `.allowed` file, or remotely by using the `rngit work` command. 

## **11.4.5 Creator Permissions** 

When a user creates a repository (via `create` , `fork` , or `mirror` ), they are automatically granted `adm` (admin) permissions on that repository. 

When a user creates a work document, they automatically receive `interact` and `write` permissions on that document. 

**Chapter 11. Git Over Reticulum** 

**140** 

**Reticulum Network Stack, Release 1.3.0** 

## **11.4.6 Permission Examples** 

## **Example 1: Public Read, Restricted Write** 

```
r:all
w:9710b86ba12c42d1d8f30f74fe509286
```

Everyone can read, only the specified identity can write. 

## **Example 2: Collaborative Development** 

```
r:all
i:all
p:all
w:9710b86ba12c42d1d8f30f74fe509286
rel:9710b86ba12c42d1d8f30f74fe509286
```

Everyone can read, interact (comment), and propose work documents. Only the specified identity can write, create releases, and manage work documents fully. 

## **Example 3: Private Repository** 

```
rw:9710b86ba12c42d1d8f30f74fe509286
rw:a1b2c3d4e5f686ba12c42d1ba12ef1aa
```

Only the two specified identities have any access (read or write). 

## **Example 4: Mirror with Stats** 

```
r:all
s:all
w:none
```

Everyone can read and view stats, but nobody can push (mirror is read-only from upstream). 

## **11.4.7 Permission Short Forms** 

Permissions can be specified using short or long forms: 

- `r` = `read` 

- `w` = `write` 

- `rw` = `readwrite` 

- `c` = `create` 

- `s` = `stats` 

- `rel` = `release` 

- `i` = `interact` 

- `p` = `propose` 

- `adm` = `admin` 

Targets can also use short forms: 

- `a` = `all` = `everyone` 

- `n` = `none` = `nobody` 

**11.4. Permissions** 

**141** 

**Reticulum Network Stack, Release 1.3.0** 

## **11.4.8 Permission Configuration Locations** 

- User install: `~/.rngit/config` 

- System install: `/etc/rngit/config` 

- Group permissions: `<group_root>/<group_name>.allowed` 

- Repository permissions: `<group_root>/<group_name>/<repo_name>.allowed` 

- Document permissions: `<group_root>/<group_name>.work/<doc_id>.allowed` 

## **11.5 Remote Permission Management** 

While permissions can be configured directly on the node by editing configuration files and `.allowed` files, `rngit` also supports remote permission management through the `rngit perms` command. This allows administrators to modify access controls for groups and repositories over Reticulum, without requiring shell access to the hosting node. 

To use remote permission management, you must have `admin` permission on the target group or repository. The command opens your configured `$EDITOR` to modify permissions, using the same syntax and format as local `.allowed` files. When you save and exit the editor, the modified permissions are transmitted to the remote node and applied immediately. 

## **11.5.1 Managing Group Permissions** 

To view or modify permissions for an entire repository group, specify the group URL (ending with the group name): 

```
$rngitpermsrns://50824b711717f97c2fb1166ceddd5ea9/public
```

This retrieves the current permission configuration from the `public.allowed` file and opens it in your editor. Any changes you make are validated for syntax correctness. Invalid permission rules will be rejected with an error message indicating the problematic line. 

## **11.5.2 Managing Repository Permissions** 

To manage permissions for a specific repository, include the repository name in the URL: 

```
$rngitpermsrns://50824b711717f97c2fb1166ceddd5ea9/public/myrepo
```

This operates on the `myrepo.allowed` file next to the repository. Repository-level permissions take precedence over group-level permissions, allowing fine-grained access control for individual repositories within a group. 

## **11.5.3 Permission Validation** 

When modifying permissions remotely, `rngit` validates that: 

- Each permission line follows the correct `permission:target` syntax 

- Permission types are valid (r, w, rw, c, s, rel, i, p, adm) 

- Target specifications are valid (identity hashes, `all` , or `none` ) 

- Identity hashes, when specified, are the correct length (32 hexadecimal characters) 

If validation fails, the editor will reopen with an error message describing the issue, allowing you to correct the problem before resubmitting. 

**Chapter 11. Git Over Reticulum** 

**142** 

**Reticulum Network Stack, Release 1.3.0** 

## **Caution** 

Remote permission modification requires administrative access (the `adm` permission), which grants full control over the repository or group. The permission change request is transmitted over the encrypted Reticulum link, and the remote node verifies your identity cryptographically before applying changes. However, be aware that granting `adm` permissions to remote identities effectively delegates full control, including the ability to revoke your own access or modify permissions in ways you may not anticipate. 

## **All Command-Line Options (rngit perms)** 

```
usage:rngitperms[-h][--configCONFIG][--rnsconfigRNSCONFIG]
[-iPATH][-v][-q][--version]
remote
```

```
ReticulumGitPermissionManager
positionalarguments:
remoteURLofremotegrouporrepository
options:
-h,--helpshowthishelpmessageandexit
--configCONFIGpathtoalternativeconfigdirectory
--rnsconfigRNSCONFIG
pathtoalternativeReticulumconfigdirectory
-i,--identityPATHpathtoidentity
-v,--verbose
-q,--quiet
--versionshowprogram'sversionnumberandexit
```

## **11.6 Identity & Destination Aliases** 

To make permission and remote destination management easier, you can locally define aliases for commonly used identity and destination hashes. Identity aliases used in permissions resolution can be defined in the `[aliases]` section of the `~/.rngit/config` file, while destination aliases are defined in the `[aliases]` section of the `~/.rngit/ client_config` file. 

All alias definitions take the form of `aliased_name = HASH` : 

```
[aliases]
alice=d09285e660cfe27cee6d9a0beb58b7e0
bob=ffcffb4e255e156e77f79b82c13086a6
```

**Aliases are always resolved locally!** If for example you fork a repository with `rngit fork rns://bobs_node/ public/repo_name rns://my_node/forks/repo_name` , the forked repository will of course still reference the full, original destination hash, and use this for subsequent upstream syncs. 

## **11.7 Serving Pages Over Nomad Network** 

In addition to providing Git repository access via the Git remote helper protocol and command-line tools, `rngit` can also run a Nomad Network compatible page node. This allows users to browse repository information, view file contents, inspect commit history and access repository statistics through any Nomad Network client. 

**11.6. Identity & Destination Aliases** 

**143** 

**Reticulum Network Stack, Release 1.3.0** 

When enabled, the page node provides a complete interface to your repositories, with automatic Markdown to Micron conversion, syntax-highlighted code browsing, and detailed commit, diff and statistics views. 

## **11.7.1 Enabling the Git Page Node** 

To enable the page node, add the following to your `~/.rngit/config` file: 

```
[pages]
serve_nomadnet=yes
```

When the page node is enabled, `rngit` will listen on a Nomad Network node destination in addition to the Git repository destination. You can view the destination hash by running: 

```
$rngit--print-identity
GitPeerIdentity:<959e10e5efc1bd9d97a4083babe51dea>
RepositoryNodeIdentity:<153cb870b4665b8c1c348896292b0bad>
RepositoriesDestination:<0d7334d411d00120cbad24edf355fdd2>
NomadNetworkDestination:<50824b711717f97c2fb1166ceddd5ea9>
```

## **11.7.2 Accessing Repository Pages** 

Once the page node is running, you can access it from any Nomad Network client by connecting to the Nomad Network destination. The page node provides the following views: 

- **Front Page** - Lists all repository groups accessible to your identity 

- **Group Page** - Shows all repositories within a group 

- **Repository Page** - Displays repository overview, description and README 

- **Releases** - List of releases for the repository, with information and downloads 

- **File Browser** - Browse directory trees and view and download file contents 

- **Commits View** - View commit history with pagination 

- **Commit Details** - Detailed commit information with file changes and diffs 

- **Refs View** - List branches and tags 

- **Statistics** - Activity charts showing views, fetches and pushes over time 

All pages respect the same permission system used for Git access. If an identity does not have read access to a repository, they will not be able to view its pages. 

## **11.7.3 Formatting & Syntax Highlighting** 

If the `pygments` Python module is installed on your system, the page node will automatically apply syntax highlighting to code files. The highlighting supports a wide range of programming languages and uses a color theme optimized for terminal display. 

To enable syntax highlighting, install pygments: 

```
pipinstallpygments
```

## **Markdown & Micron Support** 

README files and other Markdown documents are automatically converted to Micron markup for display in Nomad Network clients. You can also write your README files directly in Micron, in which case they will display and render 

**Chapter 11. Git Over Reticulum** 

**144** 

**Reticulum Network Stack, Release 1.3.0** 

as such in any Nomad Network client. The file browser also supports viewing both rendered and raw Markdown and Micron documents. 

Code blocks in Markdown can include language hints for syntax highlighting: 

```
���python
defhello_world():
print("Hello,Reticulum!")
���
```

You can use `rawmu` code blocks to render raw Micron inside Markdown files. If you create a code block with the language hint `rawmu` , everything inside it will be treated as Micron directly. 

## **11.7.4 Customizing Templates** 

The page node uses a template system that allows complete customization of the generated pages. Templates are stored in the `~/.rngit/templates/` directory as Micron files. 

The following template files are supported: 

- `base.mu` - Base template wrapping all pages 

- `front.mu` - Front page listing all groups 

- `group.mu` - Group page listing repositories 

- `repo.mu` - Repository overview page 

- `releases.mu` - Release list page 

- `release.mu` - Release details page 

- `tree.mu` - File browser pages 

- `blob.mu` - File content display 

- `commits.mu` - Commit history listing 

- `commit.mu` - Individual commit detail page 

- `refs.mu` - Branches and tags listing 

- `stats.mu` - Statistics page 

Templates can include the following variables: 

- `{PAGE_CONTENT}` - The main content of the page (required) 

- `{NODE_NAME}` - The configured node name 

- `{NAVIGATION}` - Breadcrumb navigation links 

- `{VERSION}` - The rngit version number 

- `{GEN_TIME}` - Page generation time 

## **Dynamic Templates** 

Templates can be made executable to generate dynamic content. If a template file has the executable bit set, it will be executed and its stdout used as the template content. 

## **Icon Sets** 

By default, the page node uses Nerd Font icons. If you prefer simpler icons or your terminal does not support Nerd Fonts, you can enable Unicode icons instead: 

**11.7. Serving Pages Over Nomad Network** 

**145** 

**Reticulum Network Stack, Release 1.3.0** 

```
[pages]
serve_nomadnet=yes
unicode_icons=yes
```

## **11.7.5 Repository Statistics** 

When statistics recording is enabled (see the `record_stats` configuration option), the page node can display activity charts for each repository. The statistics page shows: 

- Total and peak views, downloads, fetches and pushes 

- Daily activity charts over a 90-day period 

- Combined activity visualization 

To view statistics, a user must have the `s` (stats) permission for the repository. See the Access Configuration section for details on setting permissions. 

## **Repository Thanks** 

The page node includes a “Thanks” feature that allows users to express appreciation for a repository. On each repository page, a “Thanks” link is displayed showing the current thanks count. Clicking this link registers a thank you for the repository. 

## **11.7.6 Configuration Example** 

A complete node configuration might look like this: 

```
[rngit]
node_name=MyGitNode
announce_interval=360
record_stats=yes
[repositories]
public=/var/git/public
internal=/var/git/internal
[access]
public=r:all
internal=rw:9710b86ba12c42d1d8f30f74fe509286
[pages]
serve_nomadnet=yes
unicode_icons=no
```

## **11.8 Verified Releases** 

The `rngit` release system provides cryptographic provenance and integrity guarantees through automatic signing of release artifacts and signed release manifests. When you create a release, `rngit` generates an Ed25519 signature for each artifact and embeds these signatures in a cryptographically signed release manifest ( `.rsm` file). This allows anyone who obtains the release to verify its authenticity and integrity, regardless of how the files were distributed. 

**Chapter 11. Git Over Reticulum** 

**146** 

**Reticulum Network Stack, Release 1.3.0** 

## **11.8.1 Obtaining Verified Releases** 

The `rngit` system lets you obtain releases securely and in a verified manner, by validating cryptographically signed release manifests in the `.rsm` format during the retrieval process. Once a release has been published with `rngit` , anyone that has read access to it can obtain the release with the `rngit release` command, for example: 

```
$rngitreleaserns://remote_node/group/some_programfetchlatest:all
```

This command will connect to the remote, retrieve the latest release manifest, verify it’s signature and integrity (you can optionally specify a required signer identity with `--signer` ), and then download and sequentially verify all artifacts included in the release. 

If verification succeeds, the retrieved artifact files, along with the release manifest will be saved in the current working directory. From the above example, you would end up with a number of downloaded files, and a version- and package specific release manifest, such as `some_program_1.5.2.rsm` . 

## **Important** 

Keeping the retrieved release manifest is a **very** good idea! It allows you to easily obtain future releases and updates to the software directly, while verifying they came from the same publisher. 

## **Obtaining & Updating Releases Using RSM Manifests** 

One of the key features of the `rngit` release system is the ability to fetch and verify new releases using only a signed release manifest. This is particularly valuable for distributing software over Reticulum. Once someone has an `.rsm` manifest of your package, they can use it to continually retrieve and update the software. 

To fetch a release using a manifest: 

```
$rngitreleasesome_program_1.5.2.rsmfetchlatest:all
```

This command: 

1. Validates the manifest signature to confirm authenticity 

2. Extracts the origin node and repository path from the signed manifest 

3. Connects to the origin node over Reticulum 

4. Gets the _latest_ release manifest from the developer 

5. Verifies it against the existing manifest 

6. Fetches each artifact listed in the manifest 

7. Verifies each downloaded file against the signature embedded in the manifest 

If any artifact fails signature verification, the fetch aborts with an error, preventing the installation of corrupted or tampered files. 

## **Specifying Required Signers** 

You can require that releases be signed by specific identities. When fetching a release, use the `--signer` option to specify the identity hash of the required signer: 

`$ rngit release rns://remote_node/public/myrepo fetch latest:all --signer␣` _˓→_ `21a8daa6d9c3d3b8aab6e94b6bcb0e33` 

If the release was not signed by the specified identity, the fetch will abort before any files are downloaded. Likewise, if any downloaded artifacts were not signed by the required identity, the process will abort at the first invalid signature. This provides strong guarantees about the provenance of the software you are installing. 

**11.8. Verified Releases** 

**147** 

**Reticulum Network Stack, Release 1.3.0** 

The signer check also works when fetching from a local manifest: 

```
$rngitreleasemanifest.rsmfetchlatest:all--signer21a8daa6d9c3d3b8aab6e94b6bcb0e33
```

## **Selective & Partial Fetches** 

You can fetch individual artifacts from a release by specifying the artifact name instead of `all` : 

```
$rngitreleaserns://remote_node/public/myrepofetch1.2.0:myapp-1.2.0.tar.gz
```

This downloads only the specified artifact and verifies its signature against the manifest. If a file already exists locally, `rngit` verifies it against the manifest signature and skips the download if valid, making it safe to run the command multiple times. When fetching releases, `rngit release` will only download files that are missing or invalid according to the manifest. This means that partially completed release fetches can be continued later, if interrupted. 

## **Pattern Matching for Artifacts** 

When fetching selective artifacts, you are not limited to exact names or the `all` keyword. You can use shell-style wildcard patterns to match multiple artifacts flexibly. This is particularly useful for selecting platform-specific builds, version ranges, or file types without specifying each file individually. 

## **Tip** 

When using pattern matching, make sure to enclose the target specification in quotes. Otherwise, your shell will probably interpret it as a shell expansion pattern _before_ it is passed as an argument to `rngit` ! 

The pattern matching supports standard Unix wildcards: 

- `*` matches any sequence of characters (including empty) 

- `?` matches any single character 

- `[seq]` matches any character in _seq_ (for example `[0-9]` or `[abc]` ) 

- `[!seq]` matches any character not in _seq_ 

For example, to fetch all wheel files for Python 3 across any platform: 

```
$rngitreleaserns://remote_node/public/myrepofetch"1.2.0:*-py3-*.whl"
```

To fetch a specific patch version when you know the major and minor version: 

`$ rngit release rns://remote_node/public/myrepo fetch "1.2.0:myapp-1.2.?-linux-x86_64.` _˓→_ `tar.gz"` 

Or to retrieve all source archives: 

```
$rngitreleaserns://remote_node/public/myrepofetch"1.2.0:source_*.tgz"
```

If your pattern contains no wildcard characters, it must match an artifact name exactly, which is useful for fetching single, specific artifacts. When a pattern matches multiple artifacts, all matched files are fetched and verified. If no artifacts match the pattern, the fetch aborts with an error indicating no matches were found. 

## **Offline Verification** 

Because the release manifest contains embedded signatures, you can verify the integrity of release artifacts offline, without connecting to the repository node. The `rnid` and `rngit` utilities can validate artifact signatures against `.rsg` and manifest files. 

**Chapter 11. Git Over Reticulum** 

**148** 

**Reticulum Network Stack, Release 1.3.0** 

## **For individual files:** 

Ensure the `.rsg` signature is located in the same directory as the release artifact, then run: 

```
$rnid-Vmyapp-1.2.0.tar.gz
```

This validates that the artifact file matches the signature created during the release process. Combined with the manifest’s own signature, this provides end-to-end verification from the original release creation to the final installation. 

## **For a complete release:** 

Ensure the release manifest is located in the same directory as the release artifacts, then run: 

```
$rngitreleasemyapp-1.2.0.rsm--offline
```

This will load the manifest, and verify all files currently on-disk, but will not attempt to fetch the latest release manifest from the origin, or update local files to match it. 

## **11.8.2 Creating Signed Releases** 

Reticulum and the `rngit` system makes it easy to create signed releases that your users can verify and update securely. When you create a release using `rngit` , the program automatically: 

1. Generates an Ed25519 signature for each artifact file using your identity’s signing key 

2. Creates `.rsg` signature files alongside each artifact in your distribution directory 

3. Constructs a signed release manifest ( `manifest.rsm` ) containing metadata, an artifact list, and embedded signatures 

4. Transmits both artifacts, signatures and manifest to the remote node specified as release origin 

As an example, to create and publish a release from all files in the folder named `dist` , simply run: 

```
$rngitreleaserns://my_node/group/myrepocreate1.2.0:./dist
```

Everything is automatically signed and uploaded to your node, and the release manifest will now include the following signed attestation information: 

- Package name and version 

- The release notes for this release 

- Release timestamp and commit hash 

- Origin node identity and repository path 

- Complete list of artifacts 

- Embedded signatures for each artifact 

That’s it, there’s nothing more to it than one command. Users can now securely obtain your release using `rngit release fetch` . 

## **Release Manifest Format** 

Release manifests use the `.rsm` format (a general-purpose, structured signed message format) and are themselves cryptographically signed documents. The manifest format embeds the signing identity’s public key and a detached signature that covers the entire manifest content. This creates a chain of trust: the manifest signature proves the manifest’s authenticity, and the embedded artifact signatures prove each file’s integrity. 

When a release is created, the manifest is stored as `manifest.rsm` in the release artifacts directory. You can also generate a local release manifest without uploading by using the `--local` flag: 

**11.8. Verified Releases** 

**149** 

**Reticulum Network Stack, Release 1.3.0** 

`$ rngit release rns://f2d31b2e080e5d4e358d32822ee4a3b7/public/myrepo create 1.2.0:./dist␣` _˓→_ `--local` 

This creates the `.rsg` signature files and `manifest.rsm` in your local distribution directory without connecting to the remote node, allowing you to inspect or distribute the signed release through alternative channels. 

## **Signature File Format** 

Individual artifact signatures use the Reticulum Signature ( `.rsg` ) format and contain: 

- The Ed25519 signature of the file 

- The signing identity’s public key 

- Optional metadata, such as timestamps or notes 

These signature files are created automatically during the release process and can be used independently of the manifest for verification purposes. The `rnid` utility can create and validate RSG signatures for any file, making this signature format useful beyond the `rngit` release system. 

## **Good Practices for Signature Distribution** 

While release manifests in the `.rsm` format _include_ embedded `.rsg` signatures for every listed artifact, it is dependent on the situation and requirements whether individual `.rsg` signatures are distributed as well. It is generally a good idea to do so, since they are very light-weight, and provide an easy and convenient way to validate and authenticate _individual_ files, as opposed to entire releases. 

When distributing software through multiple channels (direct download, mirror networks, physical media), including the `.rsm` manifest allows recipients to verify authenticity regardless of how they obtained the files. This is particularly valuable in low-connectivity environments where Reticulum may be the only available communication channel, as the manifest ensures that software updates can be verified even when received via store-and-forward mechanisms or physical media transport. 

## **Integration with Package Management** 

While this functionality is still under development, the signed release manifest format is designed to be consumed by package management systems and automated deployment tools. Because the manifest is cryptographically signed and contains all necessary metadata and integrity checks, it can serve as a trusted source of truth for software distribution, even when fetched over untrusted channels or stored for long periods. 

## **Release Encryption** 

While API primitives and command-line tools are currently not implemented for this, the release, distribution and verification system has been designed to also support _encrypted_ releases, which can be distributed securely to authorized recipients. 

## **Verified Package Format** 

The current system is being expanded to also include an `.rvp` package format, which can contain packaged releases including all relevant artifacts, metadata, manifest and signatures. 

## **Automated Mirror Discovery** 

The `rngit` release system is designed to support automated mirror discovery and distribution package retrieval over Reticulum networks. Since everything is cryptographically signed and verified, it is possible to create automated mirror and distribution networks, where users can obtain software and information from local sources, without risking malicious modifications to the software they rely on. This functionality is currently in development. 

**Chapter 11. Git Over Reticulum** 

**150** 

**Reticulum Network Stack, Release 1.3.0** 

## **11.9 Release Management** 

In addition to hosting Git repositories, `rngit` provides a complete release management system. This allows you to publish versioned releases with associated artifacts, release notes and metadata. Releases are managed through the `rngit release` subcommand, and are also viewable through the Nomad Network page interface. 

## **11.9.1 The Release Workflow** 

Creating a release involves specifying a Git tag and a directory containing build artifacts or other files to distribute. The `rngit` client will open your configured `$EDITOR` to compose release notes, then upload all artifacts to the remote repository node. 

To create a release, specify the tag name and path to artifacts: 

```
$rngitreleaserns://50824b711717f97c2fb1166ceddd5ea9/public/myrepocreate1.2.0:./dist
```

This will: 

1. Verify that the tag `1.2.0` exists in the repository 

2. Open your editor to write release notes 

3. Upload all files from the `./dist` directory 

4. Publish the release 

If no `$EDITOR` environment variable is set, `rngit` will try to use `nano` , `vim` or `vi` . The editor will show a template with instructions. Lines starting with `#` will be ignored, and if the remaining content is empty after stripping comments, the release creation will be cancelled. 

## **11.9.2 Release Storage & Structure** 

Releases are stored on the node in a directory named `repo_name.releases` next to the bare repository. Each release is a subdirectory containing: 

- `META` - Release metadata in ConfigObj format 

- `RELEASE.md` or `RELEASE.mu` - Release notes 

- `artifacts/` - All uploaded files 

- `THANKS` - Appreciation count from users 

## **11.9.3 Command-Line Interaction** 

## **Listing Releases** 

To view all releases for a repository: 

```
$rngitreleaserns://50824b711717f97c2fb1166ceddd5ea9/public/myrepolist
```

**==> picture [346 x 58] intentionally omitted <==**

**----- Start of picture text -----**<br>
|||||||||
|---|---|---|---|---|---|---|---|
|Tag|Status|Created|Objs|Notes|
|------------------------------------------------------------------|
|1.2.0|published|2025-01-15|14:32|3|Another|release|
|1.1.0|published|2024-12-03|09:15|2|Bug|fix|release|
|1.0.0|published|2024-10-20|16:45|2|Initial|release|

**----- End of picture text -----**<br>


## **Viewing Release Details** 

To see full information about a specific release: 

**11.9. Release Management** 

**151** 

**Reticulum Network Stack, Release 1.3.0** 

```
$rngitreleaserns://50824b711717f97c2fb1166ceddd5ea9/public/myrepoview1.2.0
Release:1.2.0
Status:published
Created:2026-05-0423:53:09
Thanks:5
ReleaseNotes
=============
Version1.2.0releasenotes...
Artifacts(4)
=============
-
myapp-1.2.0.tar.gz(1.5MB)
-
myapp-1.2.0.zip(1.6MB)
-checksums.txt(256B)
```

## **Fetching Releases** 

To fetch a release, specify the remote URL, version and artifacts: 

```
$rngitreleaserns://50824b711717f97c2fb1166ceddd5ea9/public/myrepofetchlatest:all
```

This process is described in greater detail in the _Obtaining Verified Releases_ section. 

## **Creating Releases** 

To fetch a release, specify the remote URL, version and artifacts: 

`$ rngit release rns://50824b711717f97c2fb1166ceddd5ea9/public/myrepo create 1.3.` _˓→_ `9:artifacts_dir` 

This process is described in greater detail in the _Creating Signed Releases_ section. 

## **Deleting Releases** 

To remove a release: 

```
$rngitreleaserns://50824b711717f97c2fb1166ceddd5ea9/public/myrepodelete1.2.0
Areyousureyouwanttodeleterelease'1.2.0'?[y/N]:y
Release1.2.0deleted
```

## **Requirements & Validation** 

- The specified tag must exist in the remote repository 

- You must have `release` permission for the repository 

- The target artifacts directory must exist and contain at least one file 

- Release notes cannot be empty 

## **Permissions** 

Release management requires the `release` permission, configured the same way as other repository permissions. In the config file or `.allowed` files, use `rel:target` to grant release management rights: 

**Chapter 11. Git Over Reticulum** 

**152** 

**Reticulum Network Stack, Release 1.3.0** 

```
#In.allowedfileorconfig
rel:all#Alloweveryone
rel:9710b86...#Allowspecificidentity
rel:none#Denyeveryone
```

## **Nomad Network Interface** 

When the Nomad Network page node is enabled, releases are displayed on a dedicated releases page for each repository. Each release is listed with its tag, creation date, artifact count and a preview of the release notes. Clicking a release shows the full details including formatted release notes and a listing of all artifacts with their sizes. 

## **All Command-Line Options (rngit release)** 

`usage: python -m RNS.Utilities.rngit.server [-h] [--config CONFIG] [--rnsconfig␣` _˓→_ `RNSCONFIG]` 

```
[-iPATH][-sPATH][-nname][-L]
[-o][-v][-q][--version]
[repository][operation][target]
```

```
ReticulumGitReleaseManager
```

```
positionalarguments:
repositoryURLofremoterepository,orpathtoRSMmanifest
operationlist,view,fetch,create,latestordelete
targettagandpathtoreleaseartifactsdirectory
options:
-h,--helpshowthishelpmessageandexit
--configCONFIGpathtoalternativeconfigdirectory
--rnsconfigRNSCONFIG
pathtoalternativeReticulumconfigdirectory
-i,--identityPATHpathtoreleaseidentity
-s,--signerPATHpathtosigningidentity,ifdifferentfromreleaseidentity
-n,--namenamepackagenameifdifferentfromreponame
-L,--localgeneratereleaselocally,butdon'tupload
-o,--offlineverifymanifestlocally,butdon'tfetchupdates
-v,--verbose
-q,--quiet
--versionshowprogram'sversionnumberandexit
```

**11.9. Release Management** 

**153** 

**Reticulum Network Stack, Release 1.3.0** 

## **11.10 Work Documents** 

In addition to releases, `rngit` provides a work document management system for tracking tasks, investigations, issues and progress related to repositories. Work documents are stored as structured msgpack data and support threaded updates and comments. 

## **11.10.1 Working With Work Documents** 

## **Listing Work Documents** 

To view work documents for a repository: 

```
$rngitworkrns://50824b711717f97c2fb1166ceddd5ea9/public/myrepolist
```

```
Activedocuments
```

```
=================
```

**==> picture [403 x 45] intentionally omitted <==**

**----- Start of picture text -----**<br>
||||||||||
|---|---|---|---|---|---|---|---|---|
|ID|Title|Author|Created|Comments|
|---------------------------------------------------------------------------|
|1|Implemented|new|feature|9710b86ba12c4f2e...|2025-01-15|14:32|3|
|2|Fixed|bug|in|parser|8f3a21c9d84e927b...|2025-01-14|09:15|1|

**----- End of picture text -----**<br>


Use `--scope completed` to view completed work documents, `--scope proposed` to view proposed documents, or `--scope all` to see all scopes. 

## **Viewing a Work Document** 

To view a specific work document with all its comments: 

```
$rngitworkrns://50824b711717f97c2fb1166ceddd5ea9/public/myrepoview-d1
```

```
Implementnewfeature(active#1)
=================================
Author:9710b86ba12c42d1d8f30f74fe509286
Status:active
Created:2026-05-0515:11:11
Edited:2026-05-0518:22:11
Format:markdown
Updates:0
```

```
Thisworkdocumenttrackstheimplementationofthenewfeature...
```

```
Updates
=======
#1by9710b86ba12c42d1d8f30f74fe509286at2026-05-0515:38:37
-------------------------------------------------------------
Initialanalysiscomplete
```

## **Creating Work Documents** 

To create a new work document: 

`$ rngit work rns://50824b711717f97c2fb1166ceddd5ea9/public/myrepo create --title` _˓→_ `"Investigate performance issue"` 

**Chapter 11. Git Over Reticulum** 

**154** 

**Reticulum Network Stack, Release 1.3.0** 

This will open your configured `$EDITOR` to compose the document content. Save and exit to create the document, or save an empty document to cancel. 

## **Editing Work Documents** 

To edit an existing work document: 

```
$rngitworkrns://50824b711717f97c2fb1166ceddd5ea9/public/myrepoedit-d1
```

This fetches the current content, opens it in your editor, and sends any changes back to the node. 

## **Adding Comments** 

To add an update to a work document: 

```
$rngitworkrns://50824b711717f97c2fb1166ceddd5ea9/public/myrepoupdate-d1
```

This opens your editor to compose the update. 

## **11.10.2 Proposing Work Documents** 

Users with `propose` permission can create work document proposals without full `write` access. Proposals are created in a “proposed” state and must be activated by a user with appropriate permissions before becoming active. 

To propose a work document: 

`$ rngit work rns://50824b711717f97c2fb1166ceddd5ea9/public/myrepo propose --title` _˓→_ `"Feature proposal"` 

This opens your editor to compose the proposal content. When saved, the document is created in the “proposed” scope. The creator automatically receives `interact` and `write` permissions on the proposed document. 

Proposed documents are visible through `--scope proposed` or `--scope all` : 

```
$rngitworkrns://50824b711717f97c2fb1166ceddd5ea9/public/myrepolist--scopeproposed
```

## **Permissions for Proposals** 

- Creating proposals requires `propose` permission on the repository 

- The creator automatically gets `interact` and `write` on their proposed document 

- Activating a proposal requires `write` and `interact` permissions 

## **11.10.3 State Management** 

## **Completing Work Documents** 

To mark a work document as completed (moving it from `active` to `completed` ): 

```
$rngitworkrns://50824b711717f97c2fb1166ceddd5ea9/public/myrepocomplete-d1
```

```
Workdocument#1completed
```

## **Activating Work Documents** 

To mark a work document as active (moving it from `completed` to `active` ): 

```
$rngitworkrns://50824b711717f97c2fb1166ceddd5ea9/public/myrepoactivate-d1
```

```
Workdocument#1activated
```

**11.10. Work Documents** 

**155** 

**Reticulum Network Stack, Release 1.3.0** 

## **Deleting Work Documents** 

To delete a work document and all its comments: 

```
$rngitworkrns://50824b711717f97c2fb1166ceddd5ea9/public/myrepodelete-id1
```

```
Areyousureyouwanttodeleteactiveworkdocument#1?[y/N]:y
Workdocument#1deleted
```

## **11.10.4 Managing Work Document Permissions** 

Users with administrative access to a work document can manage its specific permissions. This allows fine-grained control over who can read, write, comment on, or administer individual work documents. 

To view or edit permissions for a work document: 

```
$rngitworkrns://50824b711717f97c2fb1166ceddd5ea9/public/myrepoperms-d1
```

This opens your editor with the current permission configuration: 

```
r:all
i:9710b86ba12c42d1d8f30f74fe509286
adm:9710b86ba12c42d1d8f30f74fe509286
```

Permission rules follow the same format as repository permissions: 

- `r:target` - Grant read access 

- `w:target` - Grant write access 

- `i:target` - Grant interact (comment) access 

- `adm:target` - Grant admin access 

Targets can be `all` , `none` , or a specific identity hash. 

## **Who Can Edit Permissions** 

Document permissions can be edited by: 

- The original author (if they also have `interact` and `write` on the repository) 

- Any user with `admin` permission on the document 

- Repository admins (through inherited permissions) 

## **Permission Precedence** 

Document-specific permissions override repository-level permissions for that document. If document permissions exist, they are checked first; if access is not granted there, repository permissions are checked. 

## **Author Rights:** 

- Users can only edit or delete work documents they created 

- The author is cryptographically verified from the interacting link’s `remote_identity` 

- Document creators automatically receive `interact` and `write` on their documents 

## **Storage Format** 

Work documents are stored in a `repo_name.work` directory next to the repository, containing: 

- `active/` - Active work documents 

**Chapter 11. Git Over Reticulum** 

**156** 

**Reticulum Network Stack, Release 1.3.0** 

- `completed/` - Completed work documents 

- `proposed/` - Proposed work documents 

Each document is a numbered directory containing: 

- `root` - The work document content and metadata (msgpack format) 

- `N` - Numbered comment files (msgpack format) 

## **Nomad Network Interface** 

When the Nomad Network page node is enabled, work documents are viewable through the web interface. The work page lists all documents with their status, and clicking a document shows its full content and updates. 

## **11.10.5 Cryptographic Attribution** 

Every work document is cryptographically signed by its creator using their Reticulum identity. When you create or edit a document, `rngit` generates an Ed25519 signature of the content, which is stored alongside the document contents and verified by the remote node, or locally when viewing the work document through the command-line interface. This provides two essential guarantees: 

- **Attribution:** Every document and comment can be cryptographically attributed to its actual author 

- **Integrity:** Any modification to the content after creation would invalidate the signature 

When viewing a work document, the signature validation status is displayed: 

```
Author:9710b86ba12c42d1d8f30f74fe509286(notlocallyvalidated)
Signature:Documentnotsigned
```

Or, for valid signatures: 

```
Author:<9710b86ba12c42d1d8f30f74fe509286>
Signature:Valid
```

The “Valid” status indicates that the document content matches the author’s signature, and that the signing identity corresponds to the stated author. This can be used to create tamper-proof records of project decisions, investigations, and discussions that cannot be repudiated, or modified by third parties without detection. 

This cryptographic provenance is particularly valuable for distributed teams operating across trust boundaries. Because signatures are verified using the author’s Reticulum identity public keys - which can be recalled from any transport node on the network - work documents provide authoritative records of who said what, and when, without requiring a central authority to notarize or validate the communication. Even if the repository node hosting the documents becomes unavailable, the signed document files themselves retain validity and can be verified independently using standard Reticulum identity tools. 

## **All Command-Line Options (rngit work)** 

```
usage:rngitwork[-h][--configCONFIG][--rnsconfigRNSCONFIG]
[-iPATH][--scopeSCOPE][-tTITLE][-dID][-v]
[-q][--version]
[repository][operation]
ReticulumGitWorkDocumentManager
positionalarguments:
repositoryURLofremoterepository
operationlist,view,create,propose,edit,delete,
```

(continues on next page) 

**11.10. Work Documents** 

**157** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

**==> picture [476 x 174] intentionally omitted <==**

**----- Start of picture text -----**<br>
update, complete, activate or perms<br>options:<br>-h, --help show this help message and exit<br>--config CONFIG path to alternative config directory<br>--rnsconfig RNSCONFIG<br>path to alternative Reticulum config directory<br>-i, --identity PATH path to identity<br>--scope SCOPE document scope: active, completed, proposed or all<br>-t, --title TITLE document title for create/propose<br>-d, --id ID document ID<br>-v, --verbose<br>-q, --quiet<br>--version show program's version number and exit<br>**----- End of picture text -----**<br>


**Chapter 11. Git Over Reticulum** 

**158** 

**CHAPTER TWELVE** 

## **SUPPORT RETICULUM** 

You can help support the continued development of open, free and private communications systems by donating, providing feedback and contributing code and learning resources. 

## **12.1 Donations** 

Donations are gratefully accepted via the following channels: 

```
Monero:
```

```
84FpY1QbxHcgdseePYNmhTHcrgMX4nFfBYtz2GKYToqHVVhJp8Eaw1Z1EedRnKD19b3B8NiLCGVxzKV17UMmmeEsCrPyA5w
```

```
Bitcoin:
bc1pgqgu8h8xvj4jtafslq396v7ju7hkgymyrzyqft4llfslz5vp99psqfk3a6
```

```
Ethereum:
0x91C421DdfB8a30a49A71d63447ddb54cEBe3465E
Liberapay:
https://liberapay.com/Reticulum/
Ko-Fi:
https://ko-fi.com/markqvist
```

Are certain features in the development roadmap are important to you or your organisation? Make them a reality quickly by sponsoring their implementation. 

**159** 

**Reticulum Network Stack, Release 1.3.0** 

## **12.2 Provide Feedback** 

Feedback on the usage, functioning and potential dysfunctioning of any and all components of the system is very valuable to the continued development and improvement of Reticulum. But... 

## **Warning** 

**Think before you speak** . As time has shown, over 80% of the “feedback”, “bug reports” and “advice” the Reticulum project has received has been irrelevant noise, stemming from erroneous assumptions, misunderstanding the foundational functionality or philosophy behind the system, or simply the malinformed (but overly opinionated) personal preferences of individual drive-by architects. This wastes the time of everyone involved. 

The Reticulum project is not a public teahouse for serving the attention needs of random bypassers, but a highly complex system engineered and refined over more than a decade, designed to provide communication and connectivity guarantees in highly adversarial environments. 

If you want to voice your opinion, it better be well-informed, and we expect you to have a comprehensive and solid foundation for your points of view. Everything else will be ignored. 

Absolutely no automated analytics, telemetry, error reporting or statistics is collected and reported by Reticulum under any circumstances, so we rely on old-fashioned human feedback. 

**Chapter 12. Support Reticulum** 

**160** 

**CHAPTER THIRTEEN** 

## **CODE EXAMPLES** 

A number of examples are included in the source distribution of Reticulum. You can use these examples to learn how to write your own programs. 

## **13.1 Minimal** 

The _Minimal_ example demonstrates the bare-minimum setup required to connect to a Reticulum network from your program. In about five lines of code, you will have the Reticulum Network Stack initialised, and ready to pass traffic in your program. 

```
##########################################################
#ThisRNSexampledemonstratesaminimalsetup,that#
#willstartuptheReticulumNetworkStack,generatea#
#newdestination,andlettheusersendanannounce.#
##########################################################
```

```
importargparse
importsys
importRNS
```

_`# Let` '_ _`s define an app name. We` '_ _`ll use this for all # destinations we create. Since this basic example # is part of a range of example utilities, we` '_ _`ll put # them all within the app namespace "example_utilities"`_ `APP_NAME = "example_utilities"` 

```
#Thisinitialisationisexecutedwhentheprogramisstarted
defprogram_setup(configpath):
```

```
#WemustfirstinitialiseReticulum
reticulum=RNS.Reticulum(configpath)
```

```
#Randomlycreateanewidentityforourexample
identity=RNS.Identity()
```

```
#Usingtheidentitywejustcreated,wecreateadestination.
#DestinationsareendpointsinReticulum,thatcanbeaddressed
#andcommunicatedwith.Destinationscanalsoannouncetheir
#existence,whichwillletthenetworkknowtheyarereachable
#andautomaticallycreatepathstothem,fromanywhereelse
#inthenetwork.
destination=RNS.Destination(
```

(continues on next page) 

**161** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
identity,
RNS.Destination.IN,
RNS.Destination.SINGLE,
APP_NAME,
"minimalsample"
)
```

_`# We configure the destination to automatically prove all # packets addressed to it. By doing this, RNS will automatically # generate a proof for each incoming packet and transmit it # back to the sender of that packet. This will let anyone that # tries to communicate with the destination know whether their # communication was received correctly.`_ `destination.set_proof_strategy(RNS.Destination.PROVE_ALL)` _`# Everything` '_ _`s ready! # Let` '_ _`s hand over control to the announce loop`_ `announceLoop(destination) def announceLoop(destination):` _`# Let the user know that everything is ready`_ `RNS.log( "Minimal example "+ RNS.prettyhexrep(destination.hash)+ " running, hit enter to manually send an announce (Ctrl-C to quit)" )` _`# We enter a loop that runs until the users exits. # If the user hits enter, we will announce our server # destination on the network, which will let clients # know how to create messages directed towards it.`_ `while True: entered = input() destination.announce() RNS.log("Sent announce from "+RNS.prettyhexrep(destination.hash))` _`########################################################## #### Program Startup ##################################### ########################################################## # This part of the program gets run at startup, # and parses input from the user, and then starts # the desired program mode.`_ `if __name__ == "__main__": try: parser = argparse.ArgumentParser( description="Minimal example to start Reticulum and create a destination" ) parser.add_argument(` 

(continues on next page) 

**Chapter 13. Code Examples** 

**162** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
"--config",
action="store",
default=None,
help="pathtoalternativeReticulumconfigdirectory",
type=str
)
args=parser.parse_args()
ifargs.config:
configarg=args.config
else:
configarg=None
program_setup(configarg)
exceptKeyboardInterrupt:
print("")
sys.exit(0)
```

This example can also be found at https://github.com/markqvist/Reticulum/blob/master/Examples/Minimal.py. 

## **13.2 Announce** 

The _Announce_ example builds upon the previous example by exploring how to announce a destination on the network, and how to let your program receive notifications about announces from relevant destinations. 

_`########################################################## # This RNS example demonstrates setting up announce # # callbacks, which will let an application receive a # # notification when an announce relevant for it arrives # ##########################################################`_ `import argparse import random import sys import RNS` _`# Let` '_ _`s define an app name. We` '_ _`ll use this for all # destinations we create. Since this basic example # is part of a range of example utilities, we` '_ _`ll put # them all within the app namespace "example_utilities"`_ `APP_NAME = "example_utilities"` _`# We initialise two lists of strings to use as app_data`_ `fruits = ["Peach", "Quince", "Date", "Tangerine", "Pomelo", "Carambola", "Grape"] noble_gases = ["Helium", "Neon", "Argon", "Krypton", "Xenon", "Radon", "Oganesson"]` _`# This initialisation is executed when the program is started`_ `def program_setup(configpath):` _`# We must first initialise Reticulum`_ `reticulum = RNS.Reticulum(configpath)` 

(continues on next page) 

**13.2. Announce** 

**163** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
#Randomlycreateanewidentityforourexample
identity=RNS.Identity()
```

```
#Usingtheidentitywejustcreated,wecreatetwodestinations
#inthe"example_utilities.announcesample"applicationspace.
#
#DestinationsareendpointsinReticulum,thatcanbeaddressed
#andcommunicatedwith.Destinationscanalsoannouncetheir
#existence,whichwillletthenetworkknowtheyarereachable
#andautomaticallycreatepathstothem,fromanywhereelse
#inthenetwork.
destination_1=RNS.Destination(
identity,
RNS.Destination.IN,
RNS.Destination.SINGLE,
APP_NAME,
"announcesample",
"fruits"
)
destination_2=RNS.Destination(
identity,
RNS.Destination.IN,
RNS.Destination.SINGLE,
APP_NAME,
"announcesample",
"noble_gases"
)
```

```
#Weconfigurethedestinationstoautomaticallyproveall
#packetsaddressedtoit.Bydoingthis,RNSwillautomatically
#generateaproofforeachincomingpacketandtransmitit
#backtothesenderofthatpacket.Thiswillletanyonethat
#triestocommunicatewiththedestinationknowwhethertheir
#communicationwasreceivedcorrectly.
destination_1.set_proof_strategy(RNS.Destination.PROVE_ALL)
destination_2.set_proof_strategy(RNS.Destination.PROVE_ALL)
```

```
#Wecreateanannouncehandlerandconfigureittoonlyaskfor
#announcesfrom"example_utilities.announcesample.fruits".
#Trychangingthefilterandseewhathappens.
announce_handler=ExampleAnnounceHandler(
aspect_filter="example_utilities.announcesample.fruits"
)
```

```
#WeregistertheannouncehandlerwithReticulum
RNS.Transport.register_announce_handler(announce_handler)
```

_`# Everything` '_ _`s ready! # Let` '_ _`s hand over control to the announce loop`_ `announceLoop(destination_1, destination_2)` 

(continues on next page) 

**Chapter 13. Code Examples** 

**164** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

`def announceLoop(destination_1, destination_2):` _`# Let the user know that everything is ready`_ `RNS.log("Announce example running, hit enter to manually send an announce (Ctrl-C to␣` _˓→_ `quit)")` _`# We enter a loop that runs until the users exits. # If the user hits enter, we will announce our server # destination on the network, which will let clients # know how to create messages directed towards it.`_ `while True: entered = input()` _`# Randomly select a fruit`_ `fruit = fruits[random.randint(0,len(fruits)-1)]` _`# Send the announce including the app data`_ `destination_1.announce(app_data=fruit.encode("utf-8")) RNS.log( "Sent announce from "+ RNS.prettyhexrep(destination_1.hash)+ " ("+destination_1.name+")" )` _`# Randomly select a noble gas`_ `noble_gas = noble_gases[random.randint(0,len(noble_gases)-1)]` _`# Send the announce including the app data`_ `destination_2.announce(app_data=noble_gas.encode("utf-8")) RNS.log( "Sent announce from "+ RNS.prettyhexrep(destination_2.hash)+ " ("+destination_2.name+")" )` 

```
#Wewillneedtodefineanannouncehandlerclassthat
#Reticulumcanmessagewhenanannouncearrives.
classExampleAnnounceHandler:
#Theinitialisationmethodtakestheoptional
#aspect_filterargument.Ifaspect_filterissetto
#None,allannounceswillbepassedtotheinstance.
#Ifonlysomeannouncesarewanted,itcanbesetto
#anaspectstring.
def__init__(self,aspect_filter=None):
self.aspect_filter=aspect_filter
```

```
#ThismethodwillbecalledbyReticulumsTransport
#systemwhenanannouncearrivesthatmatchesthe
#configuredaspectfilter.Filtersmustbespecific,
#andcannotusewildcards.
defreceived_announce(self,destination_hash,announced_identity,app_data):
```

(continues on next page) 

**13.2. Announce** 

**165** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

`RNS.log( "Received an announce from "+ RNS.prettyhexrep(destination_hash) ) if app_data: RNS.log( "The announce contained the following app data: "+ app_data.decode("utf-8") )` _`########################################################## #### Program Startup ##################################### ########################################################## # This part of the program gets run at startup, # and parses input from the user, and then starts # the desired program mode.`_ `if __name__ == "__main__": try: parser = argparse.ArgumentParser( description="Reticulum example that demonstrates announces and announce␣` _˓→_ `handlers" ) parser.add_argument( "--config", action="store", default=None, help="path to alternative Reticulum config directory", type=str ) args = parser.parse_args() if args.config: configarg = args.config else: configarg = None program_setup(configarg) except KeyboardInterrupt: print("") sys.exit(0)` 

This example can also be found at https://github.com/markqvist/Reticulum/blob/master/Examples/Announce.py. 

**Chapter 13. Code Examples** 

**166** 

**Reticulum Network Stack, Release 1.3.0** 

## **13.3 Broadcast** 

The _Broadcast_ example explores how to transmit plaintext broadcast messages over the network. 

```
##########################################################
#ThisRNSexampledemonstratesbroadcastingunencrypted#
#informationtoanylisteningdestinations.#
##########################################################
```

`import sys import argparse import RNS` _`# Let` '_ _`s define an app name. We` '_ _`ll use this for all # destinations we create. Since this basic example # is part of a range of example utilities, we` '_ _`ll put # them all within the app namespace "example_utilities"`_ `APP_NAME = "example_utilities"` 

```
#Thisinitialisationisexecutedwhentheprogramisstarted
defprogram_setup(configpath,channel=None):
#WemustfirstinitialiseReticulum
reticulum=RNS.Reticulum(configpath)
#Iftheuserdidnotselecta"channel"weuse
#adefaultonecalled"public_information".
#This"channel"isaddedtothedestinationname-
#space,sotheusercanselectdifferentbroadcast
#channels.
ifchannel==None:
channel="public_information"
#WecreateaPLAINdestination.Thisisanuncencryptedendpoint
#thatanyonecanlistentoandsendinformationto.
broadcast_destination=RNS.Destination(
None,
RNS.Destination.IN,
RNS.Destination.PLAIN,
APP_NAME,
"broadcast",
channel
)
```

```
#Wespecifyacallbackthatwillgetcalledeverytime
#thedestinationreceivesdata.
broadcast_destination.set_packet_callback(packet_callback)
```

_`# Everything` '_ _`s ready! # Let` '_ _`s hand over control to the main loop`_ `broadcastLoop(broadcast_destination) def packet_callback(data, packet):` _`# Simply print out the received data`_ 

(continues on next page) 

**13.3. Broadcast** 

**167** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

`print("") print("Received data: "+data.decode("utf-8")+"\r\n> ", end="") sys.stdout.flush() def broadcastLoop(destination):` _`# Let the user know that everything is ready`_ `RNS.log( "Broadcast example "+ RNS.prettyhexrep(destination.hash)+ " running, enter text and hit enter to broadcast (Ctrl-C to quit)" )` _`# We enter a loop that runs until the users exits. # If the user hits enter, we will send the information # that the user entered into the prompt.`_ `while True: print("> ", end="") entered = input() if entered != "": data = entered.encode("utf-8") packet = RNS.Packet(destination, data) packet.send()` _`########################################################## #### Program Startup ##################################### ########################################################## # This part of the program gets run at startup, # and parses input from the user, and then starts # the program.`_ `if __name__ == "__main__": try: parser = argparse.ArgumentParser( description="Reticulum example demonstrating sending and receiving broadcasts "` _˓→_ `) parser.add_argument( "--config", action="store", default=None, help="path to alternative Reticulum config directory", type=str ) parser.add_argument( "--channel", action="store", default=None,` 

(continues on next page) 

**Chapter 13. Code Examples** 

**168** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
help="broadcastchannelname",
type=str
)
args=parser.parse_args()
ifargs.config:
configarg=args.config
else:
configarg=None
ifargs.channel:
channelarg=args.channel
else:
channelarg=None
program_setup(configarg,channelarg)
exceptKeyboardInterrupt:
print("")
sys.exit(0)
```

This example can also be found at https://github.com/markqvist/Reticulum/blob/master/Examples/Broadcast.py. 

## **13.4 Echo** 

The _Echo_ example demonstrates communication between two destinations using the Packet interface. 

_`########################################################## # This RNS example demonstrates a simple client/server # # echo utility. A client can send an echo request to the # # server, and the server will respond by proving receipt # # of the packet. # ##########################################################`_ `import argparse import sys import RNS` _`# Let` '_ _`s define an app name. We` '_ _`ll use this for all # destinations we create. Since this echo example # is part of a range of example utilities, we` '_ _`ll put # them all within the app namespace "example_utilities"`_ `APP_NAME = "example_utilities"` _`########################################################## #### Server Part ######################################### ########################################################## # This initialisation is executed when the users chooses # to run as a server`_ 

(continues on next page) 

**13.4. Echo** 

**169** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
defserver(configpath):
globalreticulum
```

```
#WemustfirstinitialiseReticulum
reticulum=RNS.Reticulum(configpath)
```

```
#Randomlycreateanewidentityforourechoserver
server_identity=RNS.Identity()
```

```
#Wecreateadestinationthatclientscanquery.Wewant
#tobeabletoverifyechorepliestoourclients,sowe
#createa"single"destinationthatcanreceiveencrypted
#messages.Thiswaytheclientcansendarequestandbe
#certainthatno-oneelsethanthisdestinationwasable
#toreadit.
echo_destination=RNS.Destination(
server_identity,
RNS.Destination.IN,
RNS.Destination.SINGLE,
APP_NAME,
"echo",
"request"
)
```

```
#Weconfigurethedestinationtoautomaticallyproveall
#packetsaddressedtoit.Bydoingthis,RNSwillautomatically
#generateaproofforeachincomingpacketandtransmitit
#backtothesenderofthatpacket.
echo_destination.set_proof_strategy(RNS.Destination.PROVE_ALL)
```

```
#Tellthedestinationwhichfunctioninourprogramto
#runwhenapacketisreceived.Wedothissowecan
#printalogmessagewhentheserverreceivesarequest
echo_destination.set_packet_callback(server_callback)
```

_`# Everything` '_ _`s ready! # Let` '_ _`s Wait for client requests or user input`_ `announceLoop(echo_destination)` 

```
defannounceLoop(destination):
#Lettheuserknowthateverythingisready
RNS.log(
"Echoserver"+
RNS.prettyhexrep(destination.hash)+
"running,hitentertomanuallysendanannounce(Ctrl-Ctoquit)"
)
```

```
#Weenteraloopthatrunsuntiltheusersexits.
#Iftheuserhitsenter,wewillannounceourserver
#destinationonthenetwork,whichwillletclients
#knowhowtocreatemessagesdirectedtowardsit.
```

(continues on next page) 

**Chapter 13. Code Examples** 

**170** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

`while True: entered = input() destination.announce() RNS.log("Sent announce from "+RNS.prettyhexrep(destination.hash)) def server_callback(message, packet): global reticulum` _`# Tell the user that we received an echo request, and # that we are going to send a reply to the requester. # Sending the proof is handled automatically, since we # set up the destination to prove all incoming packets.`_ `reception_stats = "" if reticulum.is_connected_to_shared_instance: reception_rssi = reticulum.get_packet_rssi(packet.packet_hash) reception_snr = reticulum.get_packet_snr(packet.packet_hash) if reception_rssi != None: reception_stats += " [RSSI "+str(reception_rssi)+" dBm]" if reception_snr != None: reception_stats += " [SNR "+str(reception_snr)+" dBm]" else: if packet.rssi != None: reception_stats += " [RSSI "+str(packet.rssi)+" dBm]" if packet.snr != None: reception_stats += " [SNR "+str(packet.snr)+" dB]" RNS.log("Received packet from echo client, proof sent"+reception_stats)` _`########################################################## #### Client Part ######################################### ########################################################## # This initialisation is executed when the users chooses # to run as a client`_ `def client(destination_hexhash, configpath, timeout=None): global reticulum` _`# We need a binary representation of the destination # hash that was entered on the command line`_ `try: dest_len = (RNS.Reticulum.TRUNCATED_HASHLENGTH//8)*2 if len(destination_hexhash) != dest_len: raise ValueError( "Destination length is invalid, must be` _`{hex}`_ `hexadecimal characters (` _˓→_ _`{byte}`_ `bytes).".format(hex=dest_len, byte=dest_len//2)` 

(continues on next page) 

**13.4. Echo** 

**171** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
)
```

`destination_hash = bytes.fromhex(destination_hexhash) except Exception as e: RNS.log("Invalid destination entered. Check your input!") RNS.log(str(e)+"\n") sys.exit(0)` _`# We must first initialise Reticulum`_ `reticulum = RNS.Reticulum(configpath)` _`# We override the loglevel to provide feedback when # an announce is received`_ `if RNS.loglevel < RNS.LOG_INFO: RNS.loglevel = RNS.LOG_INFO` _`# Tell the user that the client is ready!`_ `RNS.log( "Echo client ready, hit enter to send echo request to "+ destination_hexhash+ " (Ctrl-C to quit)" )` _`# We enter a loop that runs until the user exits. # If the user hits enter, we will try to send an # echo request to the destination specified on the # command line.`_ `while True: input()` _`# Let` '_ _`s first check if RNS knows a path to the destination. # If it does, we` '_ _`ll load the server identity and create a packet`_ `if RNS.Transport.has_path(destination_hash):` 

_`# To address the server, we need to know it` '_ _`s public # key, so we check if Reticulum knows this destination. # This is done by calling the "recall" method of the # Identity module. If the destination is known, it will # return an Identity instance that can be used in # outgoing destinations.`_ `server_identity = RNS.Identity.recall(destination_hash)` _`# We got the correct identity instance from the # recall method, so let` '_ _`s create an outgoing # destination. We use the naming convention: # example_utilities.echo.request # This matches the naming we specified in the # server part of the code.`_ `request_destination = RNS.Destination( server_identity, RNS.Destination.OUT, RNS.Destination.SINGLE,` 

(continues on next page) 

**Chapter 13. Code Examples** 

**172** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

`APP_NAME, "echo", "request" )` _`# The destination is ready, so let` '_ _`s create a packet. # We set the destination to the request_destination # that was just created, and the only data we add # is a random hash.`_ `echo_request = RNS.Packet(request_destination, RNS.Identity.get_random_` _˓→_ `hash())` 

```
#Sendthepacket!Ifthepacketissuccessfully
#sent,itwillreturnaPacketReceiptinstance.
packet_receipt=echo_request.send()
```

```
#Iftheuserspecifiedatimeout,wesetthis
#timeoutonthepacketreceipt,andconfigure
#acallbackfunction,thatwillgetcalledif
#thepackettimesout.
iftimeout!=None:
packet_receipt.set_timeout(timeout)
packet_receipt.set_timeout_callback(packet_timed_out)
```

```
#Wecanthensetadeliverycallbackonthereceipt.
#Thiswillgetautomaticallycalledwhenaprooffor
#thisspecificpacketisreceivedfromthedestination.
packet_receipt.set_delivery_callback(packet_delivered)
#Telltheuserthattheechorequestwassent
RNS.log("Sentechorequestto"+RNS.prettyhexrep(request_destination.hash))
else:
#Ifwedonotknowthisdestination,tellthe
#usertowaitforanannouncetoarrive.
RNS.log("Destinationisnotyetknown.Requestingpath...")
RNS.log("Hitentertomanuallyretryonceanannounceisreceived.")
RNS.Transport.request_path(destination_hash)
#Thisfunctioniscalledwhenourreplydestination
#receivesaproofpacket.
defpacket_delivered(receipt):
globalreticulum
ifreceipt.status==RNS.PacketReceipt.DELIVERED:
rtt=receipt.get_rtt()
if(rtt>=1):
rtt=round(rtt,3)
rttstring=str(rtt)+"seconds"
else:
rtt=round(rtt*1000,3)
rttstring=str(rtt)+"milliseconds"
```

(continues on next page) 

**13.4. Echo** 

**173** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

`reception_stats = "" if reticulum.is_connected_to_shared_instance: reception_rssi = reticulum.get_packet_rssi(receipt.proof_packet.packet_hash) reception_snr = reticulum.get_packet_snr(receipt.proof_packet.packet_hash) if reception_rssi != None: reception_stats += " [RSSI "+str(reception_rssi)+" dBm]" if reception_snr != None: reception_stats += " [SNR "+str(reception_snr)+" dB]" else: if receipt.proof_packet != None: if receipt.proof_packet.rssi != None: reception_stats += " [RSSI "+str(receipt.proof_packet.rssi)+" dBm]" if receipt.proof_packet.snr != None: reception_stats += " [SNR "+str(receipt.proof_packet.snr)+" dB]" RNS.log( "Valid reply received from "+ RNS.prettyhexrep(receipt.destination.hash)+ ", round-trip time is "+rttstring+ reception_stats )` _`# This function is called if a packet times out.`_ `def packet_timed_out(receipt): if receipt.status == RNS.PacketReceipt.FAILED: RNS.log("Packet "+RNS.prettyhexrep(receipt.hash)+" timed out")` _`########################################################## #### Program Startup ##################################### ########################################################## # This part of the program gets run at startup, # and parses input from the user, and then starts # the desired program mode.`_ `if __name__ == "__main__": try: parser = argparse.ArgumentParser(description="Simple echo server and client␣` _˓→_ `utility") parser.add_argument( "-s", "--server", action="store_true", help="wait for incoming packets from clients" ) parser.add_argument(` 

(continues on next page) 

**Chapter 13. Code Examples** 

**174** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
"-t",
"--timeout",
action="store",
metavar="s",
default=None,
help="setareplytimeoutinseconds",
type=float
)
parser.add_argument("--config",
action="store",
default=None,
help="pathtoalternativeReticulumconfigdirectory",
type=str
)
parser.add_argument(
"destination",
nargs="?",
default=None,
help="hexadecimalhashoftheserverdestination",
type=str
)
args=parser.parse_args()
ifargs.server:
configarg=None
ifargs.config:
configarg=args.config
server(configarg)
else:
ifargs.config:
configarg=args.config
else:
configarg=None
ifargs.timeout:
timeoutarg=float(args.timeout)
else:
timeoutarg=None
if(args.destination==None):
print("")
parser.print_help()
print("")
else:
client(args.destination,configarg,timeout=timeoutarg)
exceptKeyboardInterrupt:
print("")
sys.exit(0)
```

This example can also be found at https://github.com/markqvist/Reticulum/blob/master/Examples/Echo.py. 

**13.4. Echo** 

**175** 

**Reticulum Network Stack, Release 1.3.0** 

## **13.5 Link** 

The _Link_ example explores establishing an encrypted link to a remote destination, and passing traffic back and forth over the link. 

```
##########################################################
#ThisRNSexampledemonstrateshowtosetupalinkto#
#adestination,andpassdatabackandforthoverit.#
##########################################################
```

```
importos
importsys
importtime
importargparse
importRNS
```

_`# Let` '_ _`s define an app name. We` '_ _`ll use this for all # destinations we create. Since this echo example # is part of a range of example utilities, we` '_ _`ll put # them all within the app namespace "example_utilities"`_ `APP_NAME = "example_utilities"` 

```
##########################################################
####ServerPart#########################################
##########################################################
```

```
#Areferencetothelatestclientlinkthatconnected
latest_client_link=None
```

```
#Thisinitialisationisexecutedwhentheuserschooses
#torunasaserver
defserver(configpath):
```

```
#WemustfirstinitialiseReticulum
reticulum=RNS.Reticulum(configpath)
```

```
#Randomlycreateanewidentityforourlinkexample
server_identity=RNS.Identity()
```

```
#Wecreateadestinationthatclientscanconnectto.We
#wantclientstocreatelinkstothisdestination,sowe
#needtocreatea"single"destinationtype.
server_destination=RNS.Destination(
server_identity,
RNS.Destination.IN,
RNS.Destination.SINGLE,
APP_NAME,
"linkexample"
```

```
)
```

```
#Weconfigureafunctionthatwillgetcalledeverytime
#anewclientcreatesalinktothisdestination.
server_destination.set_link_established_callback(client_connected)
```

(continues on next page) 

**Chapter 13. Code Examples** 

**176** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

_`# Everything` '_ _`s ready! # Let` '_ _`s Wait for client requests or user input`_ `server_loop(server_destination) def server_loop(destination):` _`# Let the user know that everything is ready`_ `RNS.log( "Link example "+ RNS.prettyhexrep(destination.hash)+ " running, waiting for a connection." ) RNS.log("Hit enter to manually send an announce (Ctrl-C to quit)")` _`# We enter a loop that runs until the users exits. # If the user hits enter, we will announce our server # destination on the network, which will let clients # know how to create messages directed towards it.`_ `while True: entered = input() destination.announce() RNS.log("Sent announce from "+RNS.prettyhexrep(destination.hash))` _`# When a client establishes a link to our server # destination, this function will be called with # a reference to the link.`_ `def client_connected(link): global latest_client_link RNS.log("Client connected") link.set_link_closed_callback(client_disconnected) link.set_packet_callback(server_packet_received) latest_client_link = link def client_disconnected(link): RNS.log("Client disconnected") def server_packet_received(message, packet): global latest_client_link` _`# When data is received over any active link, # it will all be directed to the last client # that connected.`_ `text = message.decode("utf-8") RNS.log("Received data on the link: "+text)` 

```
reply_text="Ireceived\""+text+"\"overthelink"
reply_data=reply_text.encode("utf-8")
RNS.Packet(latest_client_link,reply_data).send()
```

```
##########################################################
```

(continues on next page) 

**13.5. Link** 

**177** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

_`#### Client Part ######################################### ########################################################## # A reference to the server link`_ `server_link = None` _`# This initialisation is executed when the users chooses # to run as a client`_ `def client(destination_hexhash, configpath):` _`# We need a binary representation of the destination # hash that was entered on the command line`_ `try: dest_len = (RNS.Reticulum.TRUNCATED_HASHLENGTH//8)*2 if len(destination_hexhash) != dest_len: raise ValueError( "Destination length is invalid, must be` _`{hex}`_ `hexadecimal characters (` _˓→_ _`{byte}`_ `bytes).".format(hex=dest_len, byte=dest_len//2) ) destination_hash = bytes.fromhex(destination_hexhash) except: " RNS.log("Invalid destination entered. Check your input!\n ) sys.exit(0)` _`# We must first initialise Reticulum`_ `reticulum = RNS.Reticulum(configpath)` _`# Check if we know a path to the destination`_ `if not RNS.Transport.has_path(destination_hash): RNS.log("Destination is not yet known. Requesting path and waiting for announce␣` _˓→_ `to arrive...") RNS.Transport.request_path(destination_hash) while not RNS.Transport.has_path(destination_hash): time.sleep(0.1)` _`# Recall the server identity`_ `server_identity = RNS.Identity.recall(destination_hash)` _`# Inform the user that we` '_ _`ll begin connecting`_ `RNS.log("Establishing link with server...")` _`# When the server identity is known, we set # up a destination`_ `server_destination = RNS.Destination( server_identity, RNS.Destination.OUT, RNS.Destination.SINGLE, APP_NAME, "linkexample" )` _`# And create a link`_ 

(continues on next page) 

**Chapter 13. Code Examples** 

**178** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
link=RNS.Link(server_destination)
```

```
#Wesetacallbackthatwillgetexecuted
#everytimeapacketisreceivedoverthe
#link
link.set_packet_callback(client_packet_received)
```

_`# We` '_ _`ll also set up functions to inform the # user when the link is established or closed`_ `link.set_link_established_callback(link_established) link.set_link_closed_callback(link_closed)` _`# Everything is set up, so let` '_ _`s enter a loop # for the user to interact with the example`_ `client_loop() def client_loop(): global server_link` _`# Wait for the link to become active`_ `while not server_link: time.sleep(0.1) should_quit = False while not should_quit: try: print("> ", end=" ") text = input()` _`# Check if we should quit the example`_ `if text == "quit" or text == "q" or text == "exit": should_quit = True server_link.teardown()` _`# If not, send the entered text over the link`_ `if text != "": data = text.encode("utf-8") if len(data) <= RNS.Link.MDU: RNS.Packet(server_link, data).send() else: RNS.log( "Cannot send this packet, the data size of "+ str(len(data))+" bytes exceeds the link packet MDU of "+ str(RNS.Link.MDU)+" bytes", RNS.LOG_ERROR ) except Exception as e: RNS.log("Error while sending data over the link: "+str(e)) should_quit = True server_link.teardown()` 

(continues on next page) 

**13.5. Link** 

**179** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

_`# This function is called when a link # has been established with the server`_ `def link_established(link):` _`# We store a reference to the link # instance for later use`_ `global server_link server_link = link` _`# Inform the user that the server is # connected`_ `RNS.log("Link established with server, enter some text to send, or \"quit\" to quit")` _`# When a link is closed, we` '_ _`ll inform the # user, and exit the program`_ `def link_closed(link): if link.teardown_reason == RNS.Link.TIMEOUT: RNS.log("The link timed out, exiting now") elif link.teardown_reason == RNS.Link.DESTINATION_CLOSED: RNS.log("The link was closed by the server, exiting now") else: RNS.log("Link closed, exiting now") time.sleep(1.5) sys.exit(0)` _`# When a packet is received over the link, we # simply print out the data.`_ `def client_packet_received(message, packet): text = message.decode("utf-8") RNS.log("Received data on the link: "+text) print("> ", end=" ") sys.stdout.flush()` 

```
##########################################################
####ProgramStartup#####################################
##########################################################
#Thispartoftheprogramrunsatstartup,
#andparsesinputoffromtheuser,andthen
#startsupthedesiredprogrammode.
if__name__=="__main__":
try:
parser=argparse.ArgumentParser(description="Simplelinkexample")
parser.add_argument(
"-s",
"--server",
action="store_true",
help="waitforincominglinkrequestsfromclients"
)
```

(continues on next page) 

**Chapter 13. Code Examples** 

**180** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
parser.add_argument(
"--config",
action="store",
default=None,
help="pathtoalternativeReticulumconfigdirectory",
type=str
)
parser.add_argument(
"destination",
nargs="?",
default=None,
help="hexadecimalhashoftheserverdestination",
type=str
)
args=parser.parse_args()
ifargs.config:
configarg=args.config
else:
configarg=None
ifargs.server:
server(configarg)
else:
if(args.destination==None):
print("")
parser.print_help()
print("")
else:
client(args.destination,configarg)
exceptKeyboardInterrupt:
print("")
sys.exit(0)
```

This example can also be found at https://github.com/markqvist/Reticulum/blob/master/Examples/Link.py. 

## **13.6 Identification** 

The _Identify_ example explores identifying an intiator of a link, once the link has been established. 

_`########################################################## # This RNS example demonstrates how to set up a link to # # a destination, and identify the initiator to it` '_ _`s peer # ##########################################################`_ `import os import sys import time import argparse` 

(continues on next page) 

**13.6. Identification** 

**181** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

## `import RNS` 

_`# Let` '_ _`s define an app name. We` '_ _`ll use this for all # destinations we create. Since this echo example # is part of a range of example utilities, we` '_ _`ll put # them all within the app namespace "example_utilities"`_ `APP_NAME = "example_utilities"` 

```
##########################################################
####ServerPart#########################################
##########################################################
```

```
#Areferencetothelatestclientlinkthatconnected
latest_client_link=None
```

```
#Thisinitialisationisexecutedwhentheuserschooses
#torunasaserver
defserver(configpath):
#WemustfirstinitialiseReticulum
reticulum=RNS.Reticulum(configpath)
```

```
#Randomlycreateanewidentityforourlinkexample
server_identity=RNS.Identity()
```

```
#Wecreateadestinationthatclientscanconnectto.We
#wantclientstocreatelinkstothisdestination,sowe
#needtocreatea"single"destinationtype.
server_destination=RNS.Destination(
server_identity,
RNS.Destination.IN,
RNS.Destination.SINGLE,
APP_NAME,
"identifyexample"
)
```

```
#Weconfigureafunctionthatwillgetcalledeverytime
#anewclientcreatesalinktothisdestination.
server_destination.set_link_established_callback(client_connected)
```

_`# Everything` '_ _`s ready! # Let` '_ _`s Wait for client requests or user input`_ `server_loop(server_destination)` 

```
defserver_loop(destination):
#Lettheuserknowthateverythingisready
RNS.log(
"Linkidentificationexample"+
RNS.prettyhexrep(destination.hash)+
"running,waitingforaconnection."
)
RNS.log("Hitentertomanuallysendanannounce(Ctrl-Ctoquit)")
```

(continues on next page) 

**Chapter 13. Code Examples** 

**182** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
#Weenteraloopthatrunsuntiltheusersexits.
#Iftheuserhitsenter,wewillannounceourserver
#destinationonthenetwork,whichwillletclients
#knowhowtocreatemessagesdirectedtowardsit.
whileTrue:
entered=input()
destination.announce()
RNS.log("Sentannouncefrom"+RNS.prettyhexrep(destination.hash))
```

```
#Whenaclientestablishesalinktoourserver
#destination,thisfunctionwillbecalledwith
#areferencetothelink.
defclient_connected(link):
globallatest_client_link
RNS.log("Clientconnected")
link.set_link_closed_callback(client_disconnected)
link.set_packet_callback(server_packet_received)
link.set_remote_identified_callback(remote_identified)
latest_client_link=link
defclient_disconnected(link):
RNS.log("Clientdisconnected")
```

```
defremote_identified(link,identity):
RNS.log("Remoteidentifiedas:"+str(identity))
```

```
defserver_packet_received(message,packet):
globallatest_client_link
```

```
#Gettheoriginatingidentityfordisplay
remote_peer="unidentifiedpeer"
ifpacket.link.get_remote_identity()!=None:
remote_peer=str(packet.link.get_remote_identity())
```

```
#Whendataisreceivedoveranyactivelink,
#itwillallbedirectedtothelastclient
#thatconnected.
text=message.decode("utf-8")
RNS.log("Receiveddatafrom"+remote_peer+":"+text)
reply_text="Ireceived\""+text+"\"overthelinkfrom"+remote_peer
reply_data=reply_text.encode("utf-8")
RNS.Packet(latest_client_link,reply_data).send()
```

```
##########################################################
####ClientPart#########################################
##########################################################
```

(continues on next page) 

**13.6. Identification** 

**183** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

_`# A reference to the server link`_ `server_link = None` _`# A reference to the client identity`_ `client_identity = None` _`# This initialisation is executed when the users chooses # to run as a client`_ `def client(destination_hexhash, configpath): global client_identity` _`# We need a binary representation of the destination # hash that was entered on the command line`_ `try: dest_len = (RNS.Reticulum.TRUNCATED_HASHLENGTH//8)*2 if len(destination_hexhash) != dest_len: raise ValueError( "Destination length is invalid, must be` _`{hex}`_ `hexadecimal characters (` _˓→_ _`{byte}`_ `bytes).".format(hex=dest_len, byte=dest_len//2) ) destination_hash = bytes.fromhex(destination_hexhash) except: " RNS.log("Invalid destination entered. Check your input!\n ) sys.exit(0)` _`# We must first initialise Reticulum`_ `reticulum = RNS.Reticulum(configpath)` _`# Create a new client identity`_ `client_identity = RNS.Identity() RNS.log( "Client created new identity "+ str(client_identity) )` _`# Check if we know a path to the destination`_ `if not RNS.Transport.has_path(destination_hash): RNS.log("Destination is not yet known. Requesting path and waiting for announce␣` _˓→_ `to arrive...") RNS.Transport.request_path(destination_hash) while not RNS.Transport.has_path(destination_hash): time.sleep(0.1)` _`# Recall the server identity`_ `server_identity = RNS.Identity.recall(destination_hash)` _`# Inform the user that we` '_ _`ll begin connecting`_ `RNS.log("Establishing link with server...")` _`# When the server identity is known, we set # up a destination`_ `server_destination = RNS.Destination(` 

(continues on next page) 

**Chapter 13. Code Examples** 

**184** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
server_identity,
RNS.Destination.OUT,
RNS.Destination.SINGLE,
APP_NAME,
"identifyexample"
)
#Andcreatealink
link=RNS.Link(server_destination)
#Wesetacallbackthatwillgetexecuted
#everytimeapacketisreceivedoverthe
#link
link.set_packet_callback(client_packet_received)
```

_`# We` '_ _`ll also set up functions to inform the # user when the link is established or closed`_ `link.set_link_established_callback(link_established) link.set_link_closed_callback(link_closed)` 

_`# Everything is set up, so let` '_ _`s enter a loop # for the user to interact with the example`_ `client_loop() def client_loop(): global server_link` _`# Wait for the link to become active`_ `while not server_link: time.sleep(0.1) should_quit = False while not should_quit: try: print("> ", end=" ") text = input()` _`# Check if we should quit the example`_ `if text == "quit" or text == "q" or text == "exit": should_quit = True server_link.teardown()` _`# If not, send the entered text over the link`_ `if text != "": data = text.encode("utf-8") if len(data) <= RNS.Link.MDU: RNS.Packet(server_link, data).send() else: RNS.log( "Cannot send this packet, the data size of "+ str(len(data))+" bytes exceeds the link packet MDU of "+ str(RNS.Link.MDU)+" bytes",` 

(continues on next page) 

**13.6. Identification** 

**185** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
RNS.LOG_ERROR
)
exceptExceptionase:
RNS.log("Errorwhilesendingdataoverthelink:"+str(e))
should_quit=True
server_link.teardown()
#Thisfunctioniscalledwhenalink
#hasbeenestablishedwiththeserver
deflink_established(link):
#Westoreareferencetothelink
#instanceforlateruse
globalserver_link,client_identity
server_link=link
#Informtheuserthattheserveris
#connected
RNS.log("Linkestablishedwithserver,identifyingtoremotepeer...")
link.identify(client_identity)
```

_`# When a link is closed, we` '_ _`ll inform the # user, and exit the program`_ `def link_closed(link): if link.teardown_reason == RNS.Link.TIMEOUT: RNS.log("The link timed out, exiting now") elif link.teardown_reason == RNS.Link.DESTINATION_CLOSED: RNS.log("The link was closed by the server, exiting now") else: RNS.log("Link closed, exiting now") time.sleep(1.5) sys.exit(0)` _`# When a packet is received over the link, we # simply print out the data.`_ `def client_packet_received(message, packet): text = message.decode("utf-8") RNS.log("Received data on the link: "+text) print("> ", end=" ") sys.stdout.flush()` 

```
##########################################################
####ProgramStartup#####################################
##########################################################
#Thispartoftheprogramrunsatstartup,
#andparsesinputoffromtheuser,andthen
#startsupthedesiredprogrammode.
if__name__=="__main__":
```

(continues on next page) 

**Chapter 13. Code Examples** 

**186** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
try:
parser=argparse.ArgumentParser(description="Simplelinkexample")
parser.add_argument(
"-s",
"--server",
action="store_true",
help="waitforincominglinkrequestsfromclients"
)
parser.add_argument(
"--config",
action="store",
default=None,
help="pathtoalternativeReticulumconfigdirectory",
type=str
)
parser.add_argument(
"destination",
nargs="?",
default=None,
help="hexadecimalhashoftheserverdestination",
type=str
)
args=parser.parse_args()
ifargs.config:
configarg=args.config
else:
configarg=None
ifargs.server:
server(configarg)
else:
if(args.destination==None):
print("")
parser.print_help()
print("")
else:
client(args.destination,configarg)
exceptKeyboardInterrupt:
print("")
sys.exit(0)
```

This example can also be found at https://github.com/markqvist/Reticulum/blob/master/Examples/Identify.py. 

**13.6. Identification** 

**187** 

**Reticulum Network Stack, Release 1.3.0** 

## **13.7 Requests & Responses** 

The _Request_ example explores sending requests and receiving responses. 

```
##########################################################
#ThisRNSexampledemonstrateshowtoperformrequests#
#andreceiveresponsesoveralink.#
##########################################################
```

`import os import sys import time import random import argparse import RNS` _`# Let` '_ _`s define an app name. We` '_ _`ll use this for all # destinations we create. Since this echo example # is part of a range of example utilities, we` '_ _`ll put # them all within the app namespace "example_utilities"`_ `APP_NAME = "example_utilities"` _`########################################################## #### Server Part ######################################### ########################################################## # A reference to the latest client link that connected`_ `latest_client_link = None` 

`def random_text_generator(path, data, request_id, link_id, remote_identity, requested_` _˓→_ `at): RNS.log("Generating response to request "+RNS.prettyhexrep(request_id)+" on link "` _˓→_ `+RNS.prettyhexrep(link_id)) texts = ["They looked up", "On each full moon", "Becky was upset", "I’ll stay away␣` _˓→_ `from it", "The pet shop stocks everything"] return texts[random.randint(0, len(texts)-1)]` 

```
#Thisinitialisationisexecutedwhentheuserschooses
#torunasaserver
defserver(configpath):
#WemustfirstinitialiseReticulum
reticulum=RNS.Reticulum(configpath)
```

```
#Randomlycreateanewidentityforourlinkexample
server_identity=RNS.Identity()
```

```
#Wecreateadestinationthatclientscanconnectto.We
#wantclientstocreatelinkstothisdestination,sowe
#needtocreatea"single"destinationtype.
server_destination=RNS.Destination(
server_identity,
RNS.Destination.IN,
RNS.Destination.SINGLE,
```

(continues on next page) 

**Chapter 13. Code Examples** 

**188** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
APP_NAME,
"requestexample"
)
```

```
#Weconfigureafunctionthatwillgetcalledeverytime
#anewclientcreatesalinktothisdestination.
server_destination.set_link_established_callback(client_connected)
```

_`# We register a request handler for handling incoming # requests over any established links.`_ `server_destination.register_request_handler( "/random/text", response_generator = random_text_generator, allow = RNS.Destination.ALLOW_ALL )` _`# Everything` '_ _`s ready! # Let` '_ _`s Wait for client requests or user input`_ `server_loop(server_destination) def server_loop(destination):` _`# Let the user know that everything is ready`_ `RNS.log( "Request example "+ RNS.prettyhexrep(destination.hash)+ " running, waiting for a connection." )` 

```
RNS.log("Hitentertomanuallysendanannounce(Ctrl-Ctoquit)")
#Weenteraloopthatrunsuntiltheusersexits.
#Iftheuserhitsenter,wewillannounceourserver
#destinationonthenetwork,whichwillletclients
#knowhowtocreatemessagesdirectedtowardsit.
whileTrue:
entered=input()
destination.announce()
RNS.log("Sentannouncefrom"+RNS.prettyhexrep(destination.hash))
#Whenaclientestablishesalinktoourserver
#destination,thisfunctionwillbecalledwith
#areferencetothelink.
defclient_connected(link):
globallatest_client_link
RNS.log("Clientconnected")
link.set_link_closed_callback(client_disconnected)
latest_client_link=link
defclient_disconnected(link):
RNS.log("Clientdisconnected")
```

(continues on next page) 

**13.7. Requests & Responses** 

**189** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

_`########################################################## #### Client Part ######################################### ########################################################## # A reference to the server link`_ `server_link = None` _`# This initialisation is executed when the users chooses # to run as a client`_ `def client(destination_hexhash, configpath):` _`# We need a binary representation of the destination # hash that was entered on the command line`_ `try: dest_len = (RNS.Reticulum.TRUNCATED_HASHLENGTH//8)*2 if len(destination_hexhash) != dest_len: raise ValueError( "Destination length is invalid, must be` _`{hex}`_ `hexadecimal characters (` _˓→_ _`{byte}`_ `bytes).".format(hex=dest_len, byte=dest_len//2) ) destination_hash = bytes.fromhex(destination_hexhash) except: " RNS.log("Invalid destination entered. Check your input!\n ) sys.exit(0)` _`# We must first initialise Reticulum`_ `reticulum = RNS.Reticulum(configpath)` _`# Check if we know a path to the destination`_ `if not RNS.Transport.has_path(destination_hash): RNS.log("Destination is not yet known. Requesting path and waiting for announce␣` _˓→_ `to arrive...") RNS.Transport.request_path(destination_hash) while not RNS.Transport.has_path(destination_hash): time.sleep(0.1)` 

_`# Recall the server identity`_ `server_identity = RNS.Identity.recall(destination_hash)` _`# Inform the user that we` '_ _`ll begin connecting`_ `RNS.log("Establishing link with server...")` _`# When the server identity is known, we set # up a destination`_ `server_destination = RNS.Destination( server_identity, RNS.Destination.OUT, RNS.Destination.SINGLE, APP_NAME, "requestexample" )` 

(continues on next page) 

**Chapter 13. Code Examples** 

**190** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

_`# And create a link`_ `link = RNS.Link(server_destination)` _`# We` '_ _`ll set up functions to inform the # user when the link is established or closed`_ `link.set_link_established_callback(link_established) link.set_link_closed_callback(link_closed)` 

_`# Everything is set up, so let` '_ _`s enter a loop # for the user to interact with the example`_ `client_loop() def client_loop(): global server_link` _`# Wait for the link to become active`_ `while not server_link: time.sleep(0.1) should_quit = False while not should_quit: try: print("> ", end=" ") text = input()` _`# Check if we should quit the example`_ `if text == "quit" or text == "q" or text == "exit": should_quit = True server_link.teardown() else: server_link.request( "/random/text", data = None, response_callback = got_response, failed_callback = request_failed ) except Exception as e: RNS.log("Error while sending request over the link: "+str(e)) should_quit = True server_link.teardown() def got_response(request_receipt): request_id = request_receipt.request_id response = request_receipt.response RNS.log("Got response for request "+RNS.prettyhexrep(request_id)+": "+str(response)) def request_received(request_receipt):` 

(continues on next page) 

**13.7. Requests & Responses** 

**191** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

`RNS.log("The request "+RNS.prettyhexrep(request_receipt.request_id)+" was received␣` _˓→_ `by the remote peer.")` 

`def request_failed(request_receipt): RNS.log("The request "+RNS.prettyhexrep(request_receipt.request_id)+" failed.")` _`# This function is called when a link # has been established with the server`_ `def link_established(link):` _`# We store a reference to the link # instance for later use`_ `global server_link server_link = link` _`# Inform the user that the server is # connected`_ `RNS.log("Link established with server, hit enter to perform a request, or type in \ "` _˓→_ `quit\" to quit")` _`# When a link is closed, we` '_ _`ll inform the # user, and exit the program`_ `def link_closed(link): if link.teardown_reason == RNS.Link.TIMEOUT: RNS.log("The link timed out, exiting now") elif link.teardown_reason == RNS.Link.DESTINATION_CLOSED: RNS.log("The link was closed by the server, exiting now") else: RNS.log("Link closed, exiting now") time.sleep(1.5) sys.exit(0)` 

```
##########################################################
####ProgramStartup#####################################
##########################################################
#Thispartoftheprogramrunsatstartup,
#andparsesinputoffromtheuser,andthen
#startsupthedesiredprogrammode.
if__name__=="__main__":
try:
parser=argparse.ArgumentParser(description="Simplerequest/responseexample")
parser.add_argument(
"-s",
"--server",
action="store_true",
help="waitforincomingrequestsfromclients"
)
```

(continues on next page) 

**Chapter 13. Code Examples** 

**192** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
parser.add_argument(
"--config",
action="store",
default=None,
help="pathtoalternativeReticulumconfigdirectory",
type=str
)
parser.add_argument(
"destination",
nargs="?",
default=None,
help="hexadecimalhashoftheserverdestination",
type=str
)
args=parser.parse_args()
ifargs.config:
configarg=args.config
else:
configarg=None
ifargs.server:
server(configarg)
else:
if(args.destination==None):
print("")
parser.print_help()
print("")
else:
client(args.destination,configarg)
exceptKeyboardInterrupt:
print("")
sys.exit(0)
```

This example can also be found at https://github.com/markqvist/Reticulum/blob/master/Examples/Request.py. 

## **13.8 Channel** 

The _Channel_ example explores using a `Channel` to send structured data between peers of a `Link` . 

```
##########################################################
#ThisRNSexampledemonstrateshowtosetupalinkto#
#adestination,andpassstructuredmessagesoverit#
#usingachannel.#
##########################################################
importos
importsys
importtime
```

(continues on next page) 

**13.8. Channel** 

**193** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
importargparse
fromdatetimeimportdatetime
```

```
importRNS
fromRNS.vendorimportumsgpack
```

_`# Let` '_ _`s define an app name. We` '_ _`ll use this for all # destinations we create. Since this echo example # is part of a range of example utilities, we` '_ _`ll put # them all within the app namespace "example_utilities"`_ `APP_NAME = "example_utilities"` 

```
##########################################################
####SharedObjects######################################
##########################################################
```

```
#Channeldatamustbestructuredinasubclassof
#MessageBase.Thisensuresthatthechannelwillbeable
#toserializeanddeserializetheobjectandmultiplexit
#withotherobjects.Bothendsofalinkwillneedthe
#sameobjectdefinitionstobeabletocommunicateover
#achannel.
#
```

```
#Note:Theobjectswewishtouseoverthechannelmust
#beregisteredwiththechannel,andeachlinkhasa
#differentchannelinstance.Seetheclient_connected
#andlink_establishedfunctionsinthisexampletosee
#howmessagetypesareregistered.
```

_`# Let` '_ _`s make a simple message class called StringMessage # that will convey a string with a timestamp.`_ 

## `class StringMessage(RNS.MessageBase):` 

_`# The MSGTYPE class variable needs to be assigned a # 2 byte integer value. This identifier allows the # channel to look up your message` '_ _`s constructor when a # message arrives over the channel. # # MSGTYPE must be unique across all message types we # register with the channel. MSGTYPEs >= 0xf000 are # reserved for the system.`_ `MSGTYPE = 0x0101` _`# The constructor of our object must be callable with # no arguments. We can have parameters, but they must # have a default assignment. # # This is needed so the channel can create an empty # version of our message into which the incoming # message can be unpacked.`_ `def __init__(self, data=None): self.data = data` 

(continues on next page) 

**Chapter 13. Code Examples** 

**194** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

## `self.timestamp = datetime.now()` 

_`# Finally, our message needs to implement functions # the channel can call to pack and unpack our message # to/from the raw packet payload. We` '_ _`ll use the # umsgpack package bundled with RNS. We could also use # the struct package bundled with Python if we wanted # more control over the structure of the packed bytes. # # Also note that packed message objects must fit # entirely in one packet. The number of bytes # available for message payloads can be queried from # the channel using the Channel.MDU property. The # channel MDU is slightly less than the link MDU due # to encoding the message header.`_ 

```
#Thepackfunctionencodesthemessagecontentsinto
#abytestream.
defpack(self)->bytes:
returnumsgpack.packb((self.data,self.timestamp))
```

```
#Andtheunpackfunctiondecodesabytestreaminto
#themessagecontents.
defunpack(self,raw):
self.data,self.timestamp=umsgpack.unpackb(raw)
```

```
##########################################################
####ServerPart#########################################
##########################################################
```

```
#Areferencetothelatestclientlinkthatconnected
latest_client_link=None
```

```
#Thisinitialisationisexecutedwhentheuserschooses
#torunasaserver
defserver(configpath):
#WemustfirstinitialiseReticulum
reticulum=RNS.Reticulum(configpath)
#Randomlycreateanewidentityforourlinkexample
server_identity=RNS.Identity()
```

```
#Wecreateadestinationthatclientscanconnectto.We
#wantclientstocreatelinkstothisdestination,sowe
#needtocreatea"single"destinationtype.
server_destination=RNS.Destination(
server_identity,
RNS.Destination.IN,
RNS.Destination.SINGLE,
APP_NAME,
"channelexample"
```

(continues on next page) 

**13.8. Channel** 

**195** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
)
```

```
#Weconfigureafunctionthatwillgetcalledeverytime
#anewclientcreatesalinktothisdestination.
server_destination.set_link_established_callback(client_connected)
```

_`# Everything` '_ _`s ready! # Let` '_ _`s Wait for client requests or user input`_ `server_loop(server_destination) def server_loop(destination):` _`# Let the user know that everything is ready`_ `RNS.log( "Channel example "+ RNS.prettyhexrep(destination.hash)+ " running, waiting for a connection." )` 

```
RNS.log("Hitentertomanuallysendanannounce(Ctrl-Ctoquit)")
```

```
#Weenteraloopthatrunsuntiltheusersexits.
#Iftheuserhitsenter,wewillannounceourserver
#destinationonthenetwork,whichwillletclients
#knowhowtocreatemessagesdirectedtowardsit.
whileTrue:
entered=input()
destination.announce()
RNS.log("Sentannouncefrom"+RNS.prettyhexrep(destination.hash))
```

```
#Whenaclientestablishesalinktoourserver
#destination,thisfunctionwillbecalledwith
#areferencetothelink.
defclient_connected(link):
globallatest_client_link
latest_client_link=link
RNS.log("Clientconnected")
link.set_link_closed_callback(client_disconnected)
```

```
#Registermessagetypesandaddcallbacktochannel
channel=link.get_channel()
channel.register_message_type(StringMessage)
channel.add_message_handler(server_message_received)
```

```
defclient_disconnected(link):
RNS.log("Clientdisconnected")
```

```
defserver_message_received(message):
"""
Amessagehandler
@parammessage:AninstanceofasubclassofMessageBase
@return:Trueifmessagewashandled
```

(continues on next page) 

**Chapter 13. Code Examples** 

**196** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

_`"""`_ `global latest_client_link` _`# When a message is received over any active link, # the replies will all be directed to the last client # that connected. # In a message handler, any deserializable message # that arrives over the link` '_ _`s channel will be passed # to all message handlers, unless a preceding handler indicates it # has handled the message. # #`_ `if isinstance(message, StringMessage): RNS.log("Received data on the link: " + message.data + " (message created at " +␣` _˓→_ `str(message.timestamp) + ")")` 

```
reply_message=StringMessage("Ireceived\""+message.data+"\"overthelink")
latest_client_link.get_channel().send(reply_message)
```

```
#Incomingmessagesaresenttoeachmessage
#handleraddedtothechannel,intheorderthey
#wereadded.
#IfanymessagehandlerreturnsTrue,themessage
#isconsideredhandledandanysubsequent
#handlersareskipped.
returnTrue
```

_`########################################################## #### Client Part ######################################### ########################################################## # A reference to the server link`_ `server_link = None` _`# This initialisation is executed when the users chooses # to run as a client`_ `def client(destination_hexhash, configpath):` _`# We need a binary representation of the destination # hash that was entered on the command line`_ `try: dest_len = (RNS.Reticulum.TRUNCATED_HASHLENGTH//8)*2 if len(destination_hexhash) != dest_len: raise ValueError( "Destination length is invalid, must be` _`{hex}`_ `hexadecimal characters (` _˓→_ _`{byte}`_ `bytes).".format(hex=dest_len, byte=dest_len//2) ) destination_hash = bytes.fromhex(destination_hexhash) except: " RNS.log("Invalid destination entered. Check your input!\n ) sys.exit(0)` 

(continues on next page) 

**13.8. Channel** 

**197** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
#WemustfirstinitialiseReticulum
reticulum=RNS.Reticulum(configpath)
```

_`# Check if we know a path to the destination`_ `if not RNS.Transport.has_path(destination_hash): RNS.log("Destination is not yet known. Requesting path and waiting for announce␣` _˓→_ `to arrive...") RNS.Transport.request_path(destination_hash) while not RNS.Transport.has_path(destination_hash): time.sleep(0.1)` 

```
#Recalltheserveridentity
server_identity=RNS.Identity.recall(destination_hash)
```

_`# Inform the user that we` '_ _`ll begin connecting`_ `RNS.log("Establishing link with server...")` _`# When the server identity is known, we set # up a destination`_ `server_destination = RNS.Destination( server_identity, RNS.Destination.OUT, RNS.Destination.SINGLE, APP_NAME, "channelexample" )` _`# And create a link`_ `link = RNS.Link(server_destination)` _`# We` '_ _`ll also set up functions to inform the # user when the link is established or closed`_ `link.set_link_established_callback(link_established) link.set_link_closed_callback(link_closed)` _`# Everything is set up, so let` '_ _`s enter a loop # for the user to interact with the example`_ `client_loop() def client_loop(): global server_link` _`# Wait for the link to become active`_ `while not server_link: time.sleep(0.1) should_quit = False while not should_quit: try: print("> ", end=" ") text = input()` 

(continues on next page) 

**Chapter 13. Code Examples** 

**198** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

_`# Check if we should quit the example`_ `if text == "quit" or text == "q" or text == "exit": should_quit = True server_link.teardown()` _`# If not, send the entered text over the link`_ `if text != "": message = StringMessage(text) packed_size = len(message.pack()) channel = server_link.get_channel() if channel.is_ready_to_send(): if packed_size <= channel.mdu: channel.send(message) else: RNS.log( "Cannot send this packet, the data size of "+ str(packed_size)+" bytes exceeds the link packet MDU of "+ str(channel.MDU)+" bytes", RNS.LOG_ERROR ) else: RNS.log("Channel is not ready to send, please wait for " + "pending messages to complete.", RNS.LOG_ERROR) except Exception as e: RNS.log("Error while sending data over the link: "+str(e)) should_quit = True server_link.teardown()` _`# This function is called when a link # has been established with the server`_ `def link_established(link):` _`# We store a reference to the link # instance for later use`_ `global server_link server_link = link` _`# Register messages and add handler to channel`_ `channel = link.get_channel() channel.register_message_type(StringMessage) channel.add_message_handler(client_message_received)` _`# Inform the user that the server is # connected`_ `RNS.log("Link established with server, enter some text to send, or \"quit\" to quit")` _`# When a link is closed, we` '_ _`ll inform the # user, and exit the program`_ `def link_closed(link): if link.teardown_reason == RNS.Link.TIMEOUT: RNS.log("The link timed out, exiting now")` (continues on next page) 

**13.8. Channel** 

**199** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

`elif link.teardown_reason == RNS.Link.DESTINATION_CLOSED: RNS.log("The link was closed by the server, exiting now") else: RNS.log("Link closed, exiting now") time.sleep(1.5) sys.exit(0)` _`# When a packet is received over the channel, we # simply print out the data.`_ `def client_message_received(message): if isinstance(message, StringMessage): RNS.log("Received data on the link: " + message.data + " (message created at " +␣` _˓→_ `str(message.timestamp) + ")") print("> ", end=" ") sys.stdout.flush()` _`########################################################## #### Program Startup ##################################### ########################################################## # This part of the program runs at startup, # and parses input of from the user, and then # starts up the desired program mode.`_ `if __name__ == "__main__": try: parser = argparse.ArgumentParser(description="Simple channel example") parser.add_argument( "-s", "--server", action="store_true", help="wait for incoming link requests from clients" ) parser.add_argument( "--config", action="store", default=None, help="path to alternative Reticulum config directory", type=str ) parser.add_argument( "destination", nargs="?", default=None, help="hexadecimal hash of the server destination", type=str )` 

(continues on next page) 

**Chapter 13. Code Examples** 

**200** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
args=parser.parse_args()
ifargs.config:
configarg=args.config
else:
configarg=None
ifargs.server:
server(configarg)
else:
if(args.destination==None):
print("")
parser.print_help()
print("")
else:
client(args.destination,configarg)
exceptKeyboardInterrupt:
print("")
sys.exit(0)
```

This example can also be found at https://github.com/markqvist/Reticulum/blob/master/Examples/Channel.py. 

## **13.9 Buffer** 

The _Buffer_ example explores using buffered readers and writers to send binary data between peers of a `Link` . 

_`########################################################## # This RNS example demonstrates how to set up a link to # # a destination, and pass binary data over it using a # # channel buffer. # ##########################################################`_ `from __future__ import annotations import os import sys import time import argparse from datetime import datetime import RNS from RNS.vendor import umsgpack` _`# Let` '_ _`s define an app name. We` '_ _`ll use this for all # destinations we create. Since this echo example # is part of a range of example utilities, we` '_ _`ll put # them all within the app namespace "example_utilities"`_ `APP_NAME = "example_utilities"` _`########################################################## #### Server Part ######################################### ##########################################################`_ 

(continues on next page) 

**13.9. Buffer** 

**201** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

_`# A reference to the latest client link that connected`_ `latest_client_link = None` _`# A reference to the latest buffer object`_ `latest_buffer = None` _`# This initialisation is executed when the users chooses # to run as a server`_ `def server(configpath):` _`# We must first initialise Reticulum`_ `reticulum = RNS.Reticulum(configpath)` _`# Randomly create a new identity for our example`_ `server_identity = RNS.Identity()` _`# We create a destination that clients can connect to. We # want clients to create links to this destination, so we # need to create a "single" destination type.`_ `server_destination = RNS.Destination( server_identity, RNS.Destination.IN, RNS.Destination.SINGLE, APP_NAME, "bufferexample" )` _`# We configure a function that will get called every time # a new client creates a link to this destination.`_ `server_destination.set_link_established_callback(client_connected)` _`# Everything` '_ _`s ready! # Let` '_ _`s Wait for client requests or user input`_ `server_loop(server_destination) def server_loop(destination):` _`# Let the user know that everything is ready`_ `RNS.log( "Link buffer example "+ RNS.prettyhexrep(destination.hash)+ " running, waiting for a connection." ) RNS.log("Hit enter to manually send an announce (Ctrl-C to quit)")` _`# We enter a loop that runs until the users exits. # If the user hits enter, we will announce our server # destination on the network, which will let clients # know how to create messages directed towards it.`_ `while True: entered = input() destination.announce()` 

(continues on next page) 

**Chapter 13. Code Examples** 

**202** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
RNS.log("Sentannouncefrom"+RNS.prettyhexrep(destination.hash))
```

_`# When a client establishes a link to our server # destination, this function will be called with # a reference to the link.`_ `def client_connected(link): global latest_client_link, latest_buffer latest_client_link = link RNS.log("Client connected") link.set_link_closed_callback(client_disconnected)` _`# If a new connection is received, the old reader # needs to be disconnected.`_ `if latest_buffer: latest_buffer.close()` _`# Create buffer objects. # The stream_id parameter to these functions is # a bit like a file descriptor, except that it # is unique to the *receiver*. # # In this example, both the reader and the writer # use stream_id = 0, but there are actually two # separate unidirectional streams flowing in # opposite directions. #`_ `channel = link.get_channel() latest_buffer = RNS.Buffer.create_bidirectional_buffer(0, 0, channel, server_buffer_` _˓→_ `ready)` 

```
defclient_disconnected(link):
RNS.log("Clientdisconnected")
```

```
defserver_buffer_ready(ready_bytes:int):
"""
Callbackfrombufferwhenbufferhasdataavailable
:paramready_bytes:Thenumberofbytesreadytoread
"""
globallatest_buffer
```

```
data=latest_buffer.read(ready_bytes)
data=data.decode("utf-8")
```

```
RNS.log("Receiveddataoverthebuffer:"+data)
reply_message="Ireceived\""+data+"\"overthebuffer"
reply_message=reply_message.encode("utf-8")
latest_buffer.write(reply_message)
latest_buffer.flush()
```

(continues on next page) 

**13.9. Buffer** 

**203** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
##########################################################
####ClientPart#########################################
##########################################################
```

```
#Areferencetotheserverlink
server_link=None
```

```
#Areferencetothebufferobject,neededtosharethe
#objectfromthelinkconnectedcallbacktotheclient
#loop.
buffer=None
```

_`# This initialisation is executed when the users chooses # to run as a client`_ `def client(destination_hexhash, configpath):` _`# We need a binary representation of the destination # hash that was entered on the command line`_ `try: dest_len = (RNS.Reticulum.TRUNCATED_HASHLENGTH//8)*2 if len(destination_hexhash) != dest_len: raise ValueError( "Destination length is invalid, must be` _`{hex}`_ `hexadecimal characters (` _˓→_ _`{byte}`_ `bytes).".format(hex=dest_len, byte=dest_len//2) )` 

```
destination_hash=bytes.fromhex(destination_hexhash)
except:
"
RNS.log("Invaliddestinationentered.Checkyourinput!\n)
sys.exit(0)
```

```
#WemustfirstinitialiseReticulum
reticulum=RNS.Reticulum(configpath)
```

```
#Checkifweknowapathtothedestination
ifnotRNS.Transport.has_path(destination_hash):
```

`RNS.log("Destination is not yet known. Requesting path and waiting for announce␣` _˓→_ `to arrive...")` 

```
RNS.Transport.request_path(destination_hash)
whilenotRNS.Transport.has_path(destination_hash):
time.sleep(0.1)
```

```
#Recalltheserveridentity
server_identity=RNS.Identity.recall(destination_hash)
```

_`# Inform the user that we` '_ _`ll begin connecting`_ `RNS.log("Establishing link with server...")` 

```
#Whentheserveridentityisknown,weset
```

(continues on next page) 

**Chapter 13. Code Examples** 

**204** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

_`# up a destination`_ `server_destination = RNS.Destination( server_identity, RNS.Destination.OUT, RNS.Destination.SINGLE, APP_NAME, "bufferexample" )` _`# And create a link`_ `link = RNS.Link(server_destination)` _`# We` '_ _`ll also set up functions to inform the # user when the link is established or closed`_ `link.set_link_established_callback(link_established) link.set_link_closed_callback(link_closed)` _`# Everything is set up, so let` '_ _`s enter a loop # for the user to interact with the example`_ `client_loop() def client_loop(): global server_link` _`# Wait for the link to become active`_ `while not server_link: time.sleep(0.1) should_quit = False while not should_quit: try: print("> ", end=" ") text = input()` _`# Check if we should quit the example`_ `if text == "quit" or text == "q" or text == "exit": should_quit = True server_link.teardown() else:` _`# Otherwise, encode the text and write it to the buffer.`_ `text = text.encode("utf-8") buffer.write(text)` _`# Flush the buffer to force the data to be sent.`_ `buffer.flush() except Exception as e: RNS.log("Error while sending data over the link buffer: "+str(e)) should_quit = True server_link.teardown()` _`# This function is called when a link`_ 

(continues on next page) 

**13.9. Buffer** 

**205** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

_`# has been established with the server`_ `def link_established(link):` _`# We store a reference to the link # instance for later use`_ `global server_link, buffer server_link = link` _`# Create buffer, see server_client_connected() for # more detail about setting up the buffer.`_ `channel = link.get_channel() buffer = RNS.Buffer.create_bidirectional_buffer(0, 0, channel, client_buffer_ready)` _`# Inform the user that the server is # connected`_ `RNS.log("Link established with server, enter some text to send, or \"quit\" to quit")` _`# When a link is closed, we` '_ _`ll inform the # user, and exit the program`_ `def link_closed(link): if link.teardown_reason == RNS.Link.TIMEOUT: RNS.log("The link timed out, exiting now") elif link.teardown_reason == RNS.Link.DESTINATION_CLOSED: RNS.log("The link was closed by the server, exiting now") else: RNS.log("Link closed, exiting now") time.sleep(1.5) sys.exit(0)` _`# When the buffer has new data, read it and write it to the terminal.`_ `def client_buffer_ready(ready_bytes: int): global buffer data = buffer.read(ready_bytes) RNS.log("Received data over the link buffer: " + data.decode("utf-8")) print("> ", end=" ") sys.stdout.flush()` 

```
##########################################################
####ProgramStartup#####################################
##########################################################
#Thispartoftheprogramrunsatstartup,
#andparsesinputoffromtheuser,andthen
#startsupthedesiredprogrammode.
if__name__=="__main__":
try:
parser=argparse.ArgumentParser(description="Simplebufferexample")
parser.add_argument(
"-s",
"--server",
```

(continues on next page) 

**Chapter 13. Code Examples** 

**206** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
action="store_true",
help="waitforincominglinkrequestsfromclients"
)
parser.add_argument(
"--config",
action="store",
default=None,
help="pathtoalternativeReticulumconfigdirectory",
type=str
)
parser.add_argument(
"destination",
nargs="?",
default=None,
help="hexadecimalhashoftheserverdestination",
type=str
)
args=parser.parse_args()
ifargs.config:
configarg=args.config
else:
configarg=None
ifargs.server:
server(configarg)
else:
if(args.destination==None):
print("")
parser.print_help()
print("")
else:
client(args.destination,configarg)
exceptKeyboardInterrupt:
print("")
sys.exit(0)
```

This example can also be found at https://github.com/markqvist/Reticulum/blob/master/Examples/Buffer.py. 

## **13.10 Filetransfer** 

The _Filetransfer_ example implements a basic file-server program that allow clients to connect and download files. The program uses the Resource interface to efficiently pass files of any size over a Reticulum _Link_ . 

```
##########################################################
#ThisRNSexampledemonstratesasimplefiletransfer#
#serverandclientprogram.Theserverwillservea#
#directoryoffiles,andtheclientscanlistand#
```

(continues on next page) 

**13.10. Filetransfer** 

**207** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
#downloadfilesfromtheserver.#
##
#PleasenotethatusingRNSResourcesforlargefile#
#transfersisnotrecommended,sincecompression,#
#encryptionandhashmapsequencingcantakealongtime#
#onsystemswithslowCPUs,whichwillprobablyresult#
#intheclienttimingoutbeforetheresourcesender#
#cancompletepreparingtheresource.#
##
#Ifyouneedtotransferlargefiles,usetheBundle#
#classinstead,whichwillautomaticallyslicethedata#
#intochunkssuitableforpackingasaResource.#
##########################################################
```

```
importos
importsys
importtime
importthreading
importargparse
importRNS
importRNS.vendor.umsgpackasumsgpack
```

_`# Let` '_ _`s define an app name. We` '_ _`ll use this for all # destinations we create. Since this echo example # is part of a range of example utilities, we` '_ _`ll put # them all within the app namespace "example_utilities"`_ `APP_NAME = "example_utilities"` 

_`# We` '_ _`ll also define a default timeout, in seconds`_ `APP_TIMEOUT = 45.0` 

```
##########################################################
####ServerPart#########################################
##########################################################
```

```
serve_path=None
```

```
#Thisinitialisationisexecutedwhentheuserschooses
#torunasaserver
```

```
defserver(configpath,path):
#WemustfirstinitialiseReticulum
reticulum=RNS.Reticulum(configpath)
```

```
#Randomlycreateanewidentityforourfileserver
server_identity=RNS.Identity()
```

```
globalserve_path
serve_path=path
```

```
#Wecreateadestinationthatclientscanconnectto.We
#wantclientstocreatelinkstothisdestination,sowe
#needtocreatea"single"destinationtype.
```

(continues on next page) 

**Chapter 13. Code Examples** 

**208** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

`server_destination = RNS.Destination( server_identity, RNS.Destination.IN, RNS.Destination.SINGLE, APP_NAME, "filetransfer", "server" )` _`# We configure a function that will get called every time # a new client creates a link to this destination.`_ `server_destination.set_link_established_callback(client_connected)` _`# Everything` '_ _`s ready! # Let` '_ _`s Wait for client requests or user input`_ `announceLoop(server_destination)` 

```
defannounceLoop(destination):
#Lettheuserknowthateverythingisready
RNS.log("Fileserver"+RNS.prettyhexrep(destination.hash)+"running")
RNS.log("Hitentertomanuallysendanannounce(Ctrl-Ctoquit)")
```

_`# We enter a loop that runs until the users exits. # If the user hits enter, we will announce our server # destination on the network, which will let clients # know how to create messages directed towards it.`_ `while True: entered = input() destination.announce() RNS.log("Sent announce from "+RNS.prettyhexrep(destination.hash))` _`# Here` '_ _`s a convenience function for listing all files # in our served directory`_ `def list_files():` _`# We add all entries from the directory that are # actual files, and does not start with "."`_ `global serve_path return [file for file in os.listdir(serve_path) if os.path.isfile(os.path.join(serve_` _˓→_ `path, file)) and file[:1] != "."]` 

```
#Whenaclientestablishesalinktoourserver
#destination,thisfunctionwillbecalledwith
#areferencetothelink.Wethensendtheclient
#alistoffileshostedontheserver.
defclient_connected(link):
#Checkiftheserveddirectorystillexists
ifos.path.isdir(serve_path):
RNS.log("Clientconnected,sendingfilelist...")
link.set_link_closed_callback(client_disconnected)
#Wepackalistoffilesforsendinginapacket
```

(continues on next page) 

**13.10. Filetransfer** 

**209** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

`data = umsgpack.packb(list_files())` _`# Check the size of the packed data`_ `if len(data) <= RNS.Link.MDU:` _`# If it fits in one packet, we will just # send it as a single packet over the link.`_ `list_packet = RNS.Packet(link, data) list_receipt = list_packet.send() list_receipt.set_timeout(APP_TIMEOUT) list_receipt.set_delivery_callback(list_delivered) list_receipt.set_timeout_callback(list_timeout) else: RNS.log("Too many files in served directory!", RNS.LOG_ERROR) RNS.log("You should implement a function to split the filelist over multiple␣` _˓→_ `packets.", RNS.LOG_ERROR) RNS.log("Hint: The client already supports it :)", RNS.LOG_ERROR)` _`# After this, we` '_ _`re just going to keep the link # open until the client requests a file. We` '_ _`ll # configure a function that get` '_ _`s called when # the client sends a packet with a file request.`_ `link.set_packet_callback(client_request) else: RNS.log("Client connected, but served path no longer exists!", RNS.LOG_ERROR) link.teardown() def client_disconnected(link): RNS.log("Client disconnected") def client_request(message, packet): global serve_path try: filename = message.decode("utf-8") except Exception as e: filename = None if filename in list_files(): try:` _`# If we have the requested file, we` '_ _`ll # read it and pack it as a resource`_ `RNS.log("Client requested \""+filename+"\"") file = open(os.path.join(serve_path, filename), "rb") file_resource = RNS.Resource( file, packet.link, callback=resource_sending_concluded ) file_resource.filename = filename except Exception as e:` 

(continues on next page) 

**Chapter 13. Code Examples** 

**210** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

_`# If somethign went wrong, we close # the link`_ `RNS.log("Error while reading file \""+filename+"\"", RNS.LOG_ERROR) packet.link.teardown() raise e else:` _`# If we don` '_ _`t have it, we close the link`_ `RNS.log("Client requested an unknown file") packet.link.teardown()` _`# This function is called on the server when a # resource transfer concludes.`_ `def resource_sending_concluded(resource): if hasattr(resource, "filename"): name = resource.filename else: name = "resource" if resource.status == RNS.Resource.COMPLETE: RNS.log("Done sending \""+name+"\" to client") elif resource.status == RNS.Resource.FAILED: RNS.log("Sending \""+name+"\" to client failed") def list_delivered(receipt): RNS.log("The file list was received by the client") def list_timeout(receipt): RNS.log("Sending list to client timed out, closing this link") link = receipt.destination link.teardown()` _`########################################################## #### Client Part ######################################### ########################################################## # We store a global list of files available on the server`_ `server_files = []` _`# A reference to the server link`_ `server_link = None` _`# And a reference to the current download`_ `current_download = None current_filename = None` _`# Variables to store download statistics`_ `download_started = 0 download_finished = 0 download_time = 0 transfer_size = 0 file_size = 0` 

(continues on next page) 

**13.10. Filetransfer** 

**211** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

_`# This initialisation is executed when the users chooses # to run as a client`_ `def client(destination_hexhash, configpath):` _`# We need a binary representation of the destination # hash that was entered on the command line`_ `try: dest_len = (RNS.Reticulum.TRUNCATED_HASHLENGTH//8)*2 if len(destination_hexhash) != dest_len: raise ValueError( "Destination length is invalid, must be` _`{hex}`_ `hexadecimal characters (` _˓→_ _`{byte}`_ `bytes).".format(hex=dest_len, byte=dest_len//2) ) destination_hash = bytes.fromhex(destination_hexhash) except: " RNS.log("Invalid destination entered. Check your input!\n ) sys.exit(0)` 

```
#WemustfirstinitialiseReticulum
reticulum=RNS.Reticulum(configpath)
```

_`# Check if we know a path to the destination`_ `if not RNS.Transport.has_path(destination_hash): RNS.log("Destination is not yet known. Requesting path and waiting for announce␣` _˓→_ `to arrive...") RNS.Transport.request_path(destination_hash) while not RNS.Transport.has_path(destination_hash): time.sleep(0.1)` 

```
#Recalltheserveridentity
server_identity=RNS.Identity.recall(destination_hash)
```

_`# Inform the user that we` '_ _`ll begin connecting`_ `RNS.log("Establishing link with server...")` _`# When the server identity is known, we set # up a destination`_ `server_destination = RNS.Destination( server_identity, RNS.Destination.OUT, RNS.Destination.SINGLE, APP_NAME, "filetransfer", "server" )` 

```
#Wealsowanttoautomaticallyproveincomingpackets
server_destination.set_proof_strategy(RNS.Destination.PROVE_ALL)
```

```
#Andcreatealink
```

(continues on next page) 

**Chapter 13. Code Examples** 

**212** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
link=RNS.Link(server_destination)
```

```
#Weexpectanynormaldatapacketsonthelink
#tocontainalistofservedfiles,soweset
#acallbackaccordingly
link.set_packet_callback(filelist_received)
```

_`# We` '_ _`ll also set up functions to inform the # user when the link is established or closed`_ `link.set_link_established_callback(link_established) link.set_link_closed_callback(link_closed)` _`# And set the link to automatically begin # downloading advertised resources`_ `link.set_resource_strategy(RNS.Link.ACCEPT_ALL) link.set_resource_started_callback(download_began) link.set_resource_concluded_callback(download_concluded) menu()` 

_`# Requests the specified file from the server`_ `def download(filename): global server_link, menu_mode, current_filename, transfer_size, download_started current_filename = filename download_started = 0 transfer_size = 0` _`# We just create a packet containing the # requested filename, and send it down the # link. We also specify we don` '_ _`t need a # packet receipt.`_ `request_packet = RNS.Packet(server_link, filename.encode("utf-8"), create_` _˓→_ `receipt=False) request_packet.send() print("") print(("Requested \""+filename+"\" from server, waiting for download to begin...")) menu_mode = "download_started"` 

```
#Thisfunctionrunsasimplemenufortheuser
#toselectwhichfilestodownload,orquit
menu_mode=None
defmenu():
globalserver_files,server_link
#Waituntilwehaveafilelist
whilelen(server_files)==0:
time.sleep(0.1)
RNS.log("Ready!")
time.sleep(0.5)
globalmenu_mode
menu_mode="main"
```

(continues on next page) 

**13.10. Filetransfer** 

**213** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

`should_quit = False while (not should_quit): print_menu() while not menu_mode == "main":` _`# Wait`_ `time.sleep(0.25) user_input = input() if user_input == "q" or user_input == "quit" or user_input == "exit": should_quit = True print("") else: if user_input in server_files: download(user_input) else: try: if 0 <= int(user_input) < len(server_files): download(server_files[int(user_input)]) except: pass if should_quit: server_link.teardown()` _`# Prints out menus or screens for the # various states of the client program. # It` '_ _`s simple and quite uninteresting. # I won` '_ _`t go into detail here. Just # strings basically.`_ `def print_menu(): global menu_mode, download_time, download_started, download_finished, transfer_size,␣` _˓→_ `file_size if menu_mode == "main": clear_screen() print_filelist() print("") print("Select a file to download by entering name or number, or q to quit") print(("> "), end=' ') elif menu_mode == "download_started": download_began = time.time() while menu_mode == "download_started": time.sleep(0.1) if time.time() > download_began+APP_TIMEOUT: print("The download timed out") time.sleep(1) server_link.teardown() if menu_mode == "downloading": print("Download started") print("")` 

(continues on next page) 

**Chapter 13. Code Examples** 

**214** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

`while menu_mode == "downloading": global current_download percent = round(current_download.get_progress() * 100.0, 1) print(("\rProgress: "+str(percent)+" % "), end=' ') sys.stdout.flush() time.sleep(0.1) if menu_mode == "save_error": print(("\rProgress: 100.0 %"), end=' ') sys.stdout.flush() print("") print("Could not write downloaded file to disk") current_download.status = RNS.Resource.FAILED menu_mode = "download_concluded" if menu_mode == "download_concluded": if current_download.status == RNS.Resource.COMPLETE: print(("\rProgress: 100.0 %"), end=' ') sys.stdout.flush()` _`# Print statistics`_ `hours, rem = divmod(download_time, 3600) minutes, seconds = divmod(rem, 60) timestring = "` _`{:0>2}`_ `:` _`{:0>2}`_ `:` _`{:05.2f}`_ `".format(int(hours),int(minutes),seconds) print("") print("") print("--- Statistics -----") print("\tTime taken : "+timestring) print("\tFile size : "+size_str(file_size)) print("\tData transferred : "+size_str(transfer_size)) print("\tEffective rate : "+size_str(file_size/download_time, suffix='b')+` _˓→_ `"/s") print("\tTransfer rate : "+size_str(transfer_size/download_time, suffix='b` _˓→_ `')+"/s") print("") print("The download completed! Press enter to return to the menu.") print("") input() else: print("") print("The download failed! Press enter to return to the menu.") input() current_download = None menu_mode = "main" print_menu()` _`# This function prints out a list of files # on the connected server.`_ `def print_filelist(): global server_files` 

(continues on next page) 

**13.10. Filetransfer** 

**215** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

`print("Files on server:") for index,file in enumerate(server_files): print("\t("+str(index)+")\t"+file) def filelist_received(filelist_data, packet): global server_files, menu_mode try:` _`# Unpack the list and extend our # local list of available files`_ `filelist = umsgpack.unpackb(filelist_data) for file in filelist: if not file in server_files: server_files.append(file)` _`# If the menu is already visible, # we` '_ _`ll update it with what was # just received`_ `if menu_mode == "main": print_menu() except: RNS.log("Invalid file list data received, closing link") packet.link.teardown()` _`# This function is called when a link # has been established with the server`_ `def link_established(link):` _`# We store a reference to the link # instance for later use`_ `global server_link server_link = link` _`# Inform the user that the server is # connected`_ `RNS.log("Link established with server") RNS.log("Waiting for filelist...")` _`# And set up a small job to check for # a potential timeout in receiving the # file list`_ `thread = threading.Thread(target=filelist_timeout_job, daemon=True) thread.start()` _`# This job just sleeps for the specified # time, and then checks if the file list # was received. If not, the program will # exit.`_ `def filelist_timeout_job(): time.sleep(APP_TIMEOUT) global server_files if len(server_files) == 0: RNS.log("Timed out waiting for filelist, exiting")` 

(continues on next page) 

**Chapter 13. Code Examples** 

**216** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
sys.exit(0)
```

_`# When a link is closed, we` '_ _`ll inform the # user, and exit the program`_ `def link_closed(link): if link.teardown_reason == RNS.Link.TIMEOUT: RNS.log("The link timed out, exiting now") elif link.teardown_reason == RNS.Link.DESTINATION_CLOSED: RNS.log("The link was closed by the server, exiting now") else: RNS.log("Link closed, exiting now") time.sleep(1.5) sys.exit(0)` 

_`# When RNS detects that the download has # started, we` '_ _`ll update our menu state # so the user can be shown a progress of # the download.`_ `def download_began(resource): global menu_mode, current_download, download_started, transfer_size, file_size current_download = resource` 

```
ifdownload_started==0:
download_started=time.time()
transfer_size+=resource.size
file_size=resource.total_size
menu_mode="downloading"
```

_`# When the download concludes, successfully # or not, we` '_ _`ll update our menu state and # inform the user about how it all went.`_ `def download_concluded(resource): global menu_mode, current_filename, download_started, download_finished, download_` _˓→_ `time download_finished = time.time() download_time = download_finished - download_started saved_filename = current_filename` 

```
ifresource.status==RNS.Resource.COMPLETE:
counter=0
whileos.path.isfile(saved_filename):
counter+=1
saved_filename=current_filename+"."+str(counter)
try:
file=open(saved_filename,"wb")
file.write(resource.data.read())
```

(continues on next page) 

**13.10. Filetransfer** 

**217** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
file.close()
menu_mode="download_concluded"
except:
menu_mode="save_error"
else:
menu_mode="download_concluded"
#Aconveniencefunctionforprintingahuman-
#readablefilesize
defsize_str(num,suffix='B'):
units=['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']
last_unit='Yi'
ifsuffix=='b':
num*=8
units=['','K','M','G','T','P','E','Z']
last_unit='Y'
forunitinunits:
ifabs(num)<1024.0:
return"%3.2f%s%s"%(num,unit,suffix)
num/=1024.0
return"%.2f%s%s"%(num,last_unit,suffix)
#Aconveniencefunctionforclearingthescreen
defclear_screen():
os.system('cls'ifos.name=='nt'else'clear')
##########################################################
####ProgramStartup#####################################
##########################################################
#Thispartoftheprogramrunsatstartup,
#andparsesinputoffromtheuser,andthen
#startsupthedesiredprogrammode.
if__name__=="__main__":
try:
parser=argparse.ArgumentParser(
description="Simplefiletransferserverandclientutility"
)
parser.add_argument(
"-s",
"--serve",
action="store",
metavar="dir",
help="serveadirectoryoffilestoclients"
)
parser.add_argument(
"--config",
action="store",
```

(continues on next page) 

**Chapter 13. Code Examples** 

**218** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
default=None,
help="pathtoalternativeReticulumconfigdirectory",
type=str
)
parser.add_argument(
"destination",
nargs="?",
default=None,
help="hexadecimalhashoftheserverdestination",
type=str
)
args=parser.parse_args()
ifargs.config:
configarg=args.config
else:
configarg=None
ifargs.serve:
ifos.path.isdir(args.serve):
server(configarg,args.serve)
else:
RNS.log("Thespecifieddirectorydoesnotexist")
else:
if(args.destination==None):
print("")
parser.print_help()
print("")
else:
client(args.destination,configarg)
exceptKeyboardInterrupt:
print("")
sys.exit(0)
```

This example can also be found at https://github.com/markqvist/Reticulum/blob/master/Examples/Filetransfer.py. 

## **13.11 Custom Interfaces** 

The _ExampleInterface_ demonstrates creating custom interfaces for Reticulum. Any number of custom interfaces can be loaded and utilised by Reticulum, and will be fully on-par with natively included interfaces, including all supported _interface modes_ and _common configuration options_ . 

```
#Thisexampleillustratescreatingacustominterface
#definition,thatcanbeloadedandusedbyReticulumat
#runtime.Anynumberofcustominterfacescanbecreated
#andloaded.Tousetheinterfaceplaceitinthefolder
#~/.reticulum/interfaces,andaddaninterfaceentryto
#yourReticulumconfigurationfilesimilartothis:
```

(continues on next page) 

**13.11. Custom Interfaces** 

**219** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

_`# [[Example Custom Interface]] # type = ExampleInterface # enabled = no # mode = gateway # port = /dev/ttyUSB0 # speed = 115200 # databits = 8 # parity = none # stopbits = 1`_ `from time import sleep import sys import threading import time` _`# This HDLC helper class is used by the interface # to delimit and packetize data over the physical # medium - in this case a serial connection.`_ `class HDLC():` _`# This example interface packetizes data using # simplified HDLC framing, similar to PPP`_ `FLAG = 0x7E ESC = 0x7D ESC_MASK = 0x20 @staticmethod def escape(data): data = data.replace(bytes([HDLC.ESC]), bytes([HDLC.ESC, HDLC.ESC^HDLC.ESC_MASK])) data = data.replace(bytes([HDLC.FLAG]), bytes([HDLC.ESC, HDLC.FLAG^HDLC.ESC_` _˓→_ `MASK])) return data` 

_`# Let` '_ _`s define our custom interface class. It must # be a sub-class of the RNS "Interface" class.`_ `class ExampleInterface(Interface):` _`# All interface classes must define a default # IFAC size, used in IFAC setup when the user # has not specified a custom IFAC size. This # option is specified in bytes.`_ `DEFAULT_IFAC_SIZE = 8` _`# The following properties are local to this # particular interface implementation.`_ `owner = None port = None speed = None databits = None parity = None stopbits = None serial = None` _`# All Reticulum interfaces must have an __init__`_ 

(continues on next page) 

**Chapter 13. Code Examples** 

**220** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

_`# method that takes 2 positional arguments: # The owner RNS Transport instance, and a dict # of configuration values.`_ `def __init__(self, owner, configuration):` _`# The following lines demonstrate handling # potential dependencies required for the # interface to function correctly.`_ `import importlib if importlib.util.find_spec('serial') != None: import serial else: RNS.log("Using this interface requires a serial communication module to be␣` _˓→_ `installed.", RNS.LOG_CRITICAL) RNS.log("You can install one with the command: python3 -m pip install␣` _˓→_ `pyserial", RNS.LOG_CRITICAL) RNS.panic()` _`# We start out by initialising the super-class`_ `super().__init__()` _`# To make sure the configuration data is in the # correct format, we parse it through the following # method on the generic Interface class. This step # is required to ensure compatibility on all the # platforms that Reticulum supports.`_ `ifconf = Interface.get_config_obj(configuration)` _`# Read the interface name from the configuration # and set it on our interface instance.`_ `name = ifconf["name"] self.name = name` _`# We read configuration parameters from the supplied # configuration data, and provide default values in # case any are missing.`_ `port = ifconf["port"] if "port" in ifconf else None speed = int(ifconf["speed"]) if "speed" in ifconf else 9600 databits = int(ifconf["databits"]) if "databits" in ifconf else 8 parity = ifconf["parity"] if "parity" in ifconf else "N" stopbits = int(ifconf["stopbits"]) if "stopbits" in ifconf else 1` _`# In case no port is specified, we abort setup by # raising an exception.`_ `if port == None: raise ValueError(f"No port specified for` _`{`_ `self` _`}`_ `")` _`# All interfaces must supply a hardware MTU value # to the RNS Transport instance. This value should # be the maximum data packet payload size that the # underlying medium is capable of handling in all # cases without any segmentation.`_ 

(continues on next page) 

**13.11. Custom Interfaces** 

**221** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

```
self.HW_MTU=564
```

```
#Weinitiallysetthe"online"propertytofalse,
#sincetheinterfacehasnotactuallybeenfully
#initialisedandconnectedyet.
self.online=False
```

```
#Inthiscase,wecanalsosettheindicatedbit-
#rateoftheinterfacetotheserialportspeed.
self.bitrate=speed
```

```
#Configureinternalpropertiesontheinterface
#accordingtothesuppliedconfiguration.
self.pyserial=serial
self.serial=None
self.owner=owner
self.port=port
self.speed=speed
self.databits=databits
self.parity=serial.PARITY_NONE
self.stopbits=stopbits
self.timeout=100
```

```
ifparity.lower()=="e"orparity.lower()=="even":
self.parity=serial.PARITY_EVEN
```

```
ifparity.lower()=="o"orparity.lower()=="odd":
self.parity=serial.PARITY_ODD
```

```
#Sinceallrequiredparametersarenowconfigured,
#wewilltryopeningtheserialport.
try:
self.open_port()
exceptExceptionase:
RNS.log("Couldnotopenserialportforinterface"+str(self),RNS.LOG_ERROR)
raisee
#Ifopeningtheportsucceeded,runanypost-open
#configurationrequired.
ifself.serial.is_open:
self.configure_device()
else:
raiseIOError("Couldnotopenserialport")
#Opentheserialportwithsuppliedconfiguration
#parametersandstoreareferencetotheopenport.
defopen_port(self):
RNS.log("Openingserialport"+self.port+"...",RNS.LOG_VERBOSE)
self.serial=self.pyserial.Serial(
port=self.port,
baudrate=self.speed,
bytesize=self.databits,
```

(continues on next page) 

**Chapter 13. Code Examples** 

**222** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

`parity = self.parity, stopbits = self.stopbits, xonxoff = False, rtscts = False, timeout = 0, inter_byte_timeout = None, write_timeout = None, dsrdtr = False, )` _`# The only thing required after opening the port # is to wait a small amount of time for the # hardware to initialise and then start a thread # that reads any incoming data from the device.`_ `def configure_device(self): sleep(0.5) thread = threading.Thread(target=self.read_loop) thread.daemon = True thread.start() self.online = True RNS.log("Serial port "+self.port+" is now open", RNS.LOG_VERBOSE)` _`# This method will be called from our read-loop # whenever a full packet has been received over # the underlying medium.`_ `def process_incoming(self, data):` _`# Update our received bytes counter`_ `self.rxb += len(data)` _`# And send the data packet to the Transport # instance for processing.`_ `self.owner.inbound(data, self)` _`# The running Reticulum Transport instance will # call this method on the interface whenever the # interface must transmit a packet.`_ `def process_outgoing(self,data): if self.online:` _`# First, escape and packetize the data # according to HDLC framing.`_ `data = bytes([HDLC.FLAG])+HDLC.escape(data)+bytes([HDLC.FLAG])` _`# Then write the framed data to the port`_ `written = self.serial.write(data)` _`# Update the transmitted bytes counter # and ensure that all data was written`_ `self.txb += len(data) if written != len(data): raise IOError("Serial interface only wrote "+str(written)+" bytes of "` _˓→_ `+str(len(data)))` 

(continues on next page) 

**13.11. Custom Interfaces** 

**223** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

_`# This read loop runs in a thread and continously # receives bytes from the underlying serial port. # When a full packet has been received, it will # be sent to the process_incoming methed, which # will in turn pass it to the Transport instance.`_ `def read_loop(self): try: in_frame = False escape = False data_buffer = b"" last_read_ms = int(time.time()*1000) while self.serial.is_open: if self.serial.in_waiting: byte = ord(self.serial.read(1)) last_read_ms = int(time.time()*1000) if (in_frame and byte == HDLC.FLAG): in_frame = False self.process_incoming(data_buffer) elif (byte == HDLC.FLAG): in_frame = True data_buffer = b"" elif (in_frame and len(data_buffer) < self.HW_MTU): if (byte == HDLC.ESC): escape = True else: if (escape): if (byte == HDLC.FLAG ^ HDLC.ESC_MASK): byte = HDLC.FLAG if (byte == HDLC.ESC ^ HDLC.ESC_MASK): byte = HDLC.ESC escape = False data_buffer = data_buffer+bytes([byte]) else: time_since_last = int(time.time()*1000) - last_read_ms if len(data_buffer) > 0 and time_since_last > self.timeout: data_buffer = b"" in_frame = False escape = False sleep(0.08) except Exception as e: self.online = False RNS.log("A serial port error occurred, the contained exception was: "+str(e),` _˓→_ `RNS.LOG_ERROR) RNS.log("The interface "+str(self)+" experienced an unrecoverable error and␣` _˓→_ `is now offline.", RNS.LOG_ERROR) if RNS.Reticulum.panic_on_interface_error:` 

(continues on next page) 

**Chapter 13. Code Examples** 

**224** 

**Reticulum Network Stack, Release 1.3.0** 

(continued from previous page) 

`RNS.panic() RNS.log("Reticulum will attempt to reconnect the interface periodically.",␣` _˓→_ `RNS.LOG_ERROR) self.online = False self.serial.close() self.reconnect_port()` _`# This method handles serial port disconnects.`_ `def reconnect_port(self): while not self.online: try: time.sleep(5) RNS.log("Attempting to reconnect serial port "+str(self.port)+" for "` _˓→_ `+str(self)+"...", RNS.LOG_VERBOSE) self.open_port() if self.serial.is_open: self.configure_device() except Exception as e: RNS.log("Error while reconnecting port, the contained exception was: "` _˓→_ `+str(e), RNS.LOG_ERROR) RNS.log("Reconnected serial port for "+str(self))` _`# Signal to Reticulum that this interface should # not perform any ingress limiting.`_ `def should_ingress_limit(self): return False` _`# We must provide a string representation of this # interface, that is used whenever the interface # is printed in logs or external programs.`_ `def __str__(self): return "ExampleInterface["+self.name+"]"` _`# Finally, register the defined interface class as the # target class for Reticulum to use as an interface`_ `interface_class = ExampleInterface` 

This example can also be found at https://github.com/markqvist/Reticulum/blob/master/Examples/ExampleInterface. py. 

**13.11. Custom Interfaces** 

**225** 

**Reticulum Network Stack, Release 1.3.0** 

**Chapter 13. Code Examples** 

**226** 

## **CHAPTER FOURTEEN** 

## **RETICULUM LICENSE** 

```
ReticulumLicense
```

```
Copyright(c)2016-2026MarkQvist
```

```
Permissionisherebygranted,freeofcharge,toanypersonobtainingacopy
ofthissoftwareandassociateddocumentationfiles(the"Software"),todeal
intheSoftwarewithoutrestriction,includingwithoutlimitationtherights
touse,copy,modify,merge,publish,distribute,sublicense,and/orsell
copiesoftheSoftware,andtopermitpersonstowhomtheSoftwareis
furnishedtodoso,subjecttothefollowingconditions:
```

```
-TheSoftwareshallnotbeusedinanykindofsystemwhichincludesamongst
itsfunctionstheabilitytopurposefullydoharmtohumanbeings.
```

```
-TheSoftwareshallnotbeused,directlyorindirectly,inthecreationof
anartificialintelligence,machinelearningorlanguagemodeltraining
dataset,includingbutnotlimitedtoanyusethatcontributestothe
trainingordevelopmentofsuchamodeloralgorithm.
```

```
-Theabovecopyrightnoticeandthispermissionnoticeshallbeincludedin
allcopiesorsubstantialportionsoftheSoftware.
```

```
THESOFTWAREISPROVIDED"ASIS",WITHOUTWARRANTYOFANYKIND,EXPRESSOR
IMPLIED,INCLUDINGBUTNOTLIMITEDTOTHEWARRANTIESOFMERCHANTABILITY,
FITNESSFORAPARTICULARPURPOSEANDNONINFRINGEMENT.INNOEVENTSHALLTHE
AUTHORSORCOPYRIGHTHOLDERSBELIABLEFORANYCLAIM,DAMAGESOROTHER
LIABILITY,WHETHERINANACTIONOFCONTRACT,TORTOROTHERWISE,ARISINGFROM,
OUTOFORINCONNECTIONWITHTHESOFTWAREORTHEUSEOROTHERDEALINGSINTHE
SOFTWARE.
```

**227** 

**Reticulum Network Stack, Release 1.3.0** 

**Chapter 14. Reticulum License** 

**228** 

**CHAPTER FIFTEEN** 

## **API REFERENCE** 

Communication over Reticulum networks is achieved by using a simple set of classes exposed by the RNS API. This chapter lists and explains all classes exposed by the Reticulum Network Stack API, along with their method signatures and usage. It can be used as a reference while writing applications that utilise Reticulum, or it can be read in entirity to gain an understanding of the complete functionality of RNS from a developers perspective. 

## **15.1 Reticulum** 

## `class RNS.Reticulum(` _configdir=None_ , _loglevel=None_ , _logdest=None_ , _verbosity=None_ , _require_shared_instance=False_ , _shared_instance_type=None_ `)` 

This class is used to initialise access to Reticulum within a program. You must create exactly one instance of this class before carrying out any other RNS operations, such as creating destinations or sending traffic. Every independently executed program must create their own instance of the Reticulum class, but Reticulum will automatically handle inter-program communication on the same system, and expose all connected programs to external interfaces as well. 

As soon as an instance of this class is created, Reticulum will start opening and configuring any hardware devices specified in the supplied configuration. 

Currently the first running instance must be kept running while other local instances are connected, as the first created instance will act as a master instance that directly communicates with external hardware such as modems, TNCs and radios. If a master instance is asked to exit, it will not exit until all client processes have terminated (unless killed forcibly). 

If you are running Reticulum on a system with several different programs that use RNS starting and terminating at different times, it will be advantageous to run a master RNS instance as a daemon for other programs to use on demand. 

## `MTU = 500` 

The MTU that Reticulum adheres to, and will expect other peers to adhere to. By default, the MTU is 500 bytes. In custom RNS network implementations, it is possible to change this value, but doing so will completely break compatibility with all other RNS networks. An identical MTU is a prerequisite for peers to communicate in the same network. 

Unless you really know what you are doing, the MTU should be left at the default value. 

## `LINK_MTU_DISCOVERY = True` 

Whether automatic link MTU discovery is enabled by default. Link MTU discovery significantly increases throughput over fast links. 

## `ANNOUNCE_CAP = 2` 

The maximum percentage of interface bandwidth that, at any given time, may be used to propagate announces. If an announce was scheduled for broadcasting on an interface, but doing so would exceed the 

**229** 

**Reticulum Network Stack, Release 1.3.0** 

allowed bandwidth allocation, the announce will be queued for transmission when there is bandwidth available. 

Reticulum will always prioritise propagating announces with fewer hops, ensuring that distant, large networks with many peers on fast links don’t overwhelm the capacity of smaller networks on slower mediums. If an announce remains queued for an extended amount of time, it will eventually be dropped. 

This value will be applied by default to all created interfaces, but it can be configured individually on a per-interface basis. In general, the global default setting should not be changed, and any alterations should be made on a per-interface basis instead. 

## `MINIMUM_BITRATE = 5` 

Minimum bitrate required across a medium for Reticulum to be able to successfully establish links. Currently 5 bits per second. 

## `static get_instance()` 

Return the currently running Reticulum instance 

## `static should_use_implicit_proof()` 

Returns whether proofs sent are explicit or implicit. 

## **Returns** 

True if the current running configuration specifies to use implicit proofs. False if not. 

## `static transport_enabled()` 

Returns whether Transport is enabled for the running instance. 

When Transport is enabled, Reticulum will route traffic for other peers, respond to path requests and pass announces over the network. 

## **Returns** 

True if Transport is enabled, False if not. 

## `static link_mtu_discovery()` 

Returns whether link MTU discovery is enabled for the running instance. 

When link MTU discovery is enabled, Reticulum will automatically upgrade link MTUs to the highest supported value, increasing transfer speed and efficiency. 

## **Returns** 

True if link MTU discovery is enabled, False if not. 

## `static remote_management_enabled()` 

Returns whether remote management is enabled for the running instance. 

When remote management is enabled, authenticated peers can remotely query and manage this instance. 

## **Returns** 

True if remote management is enabled, False if not. 

## `static required_discovery_value()` 

Returns the required stamp value for a discovered interface to be considered valid and remembered. 

## **Returns** 

The required stamp value as an integer. 

## `static publish_blackhole_enabled()` 

Returns whether blackhole list publishing is enabled for the running instance. 

## **Returns** 

True if blackhole list publishing is enabled, False if not. 

**Chapter 15. API Reference** 

**230** 

**Reticulum Network Stack, Release 1.3.0** 

## `static blackhole_sources()` 

Returns the list of transport identity hashes from which blackhole lists are sourced. 

## **Returns** 

A list of identity hashes. 

## `static discovered_interfaces()` 

Returns a list of interfaces discovered over the network. 

## **Returns** 

A list of discovered interfaces. 

## `static interface_discovery_sources()` 

Returns the list of network identity hashes from which interfaces are discovered. 

## **Returns** 

A list of identity hashes. 

## **15.2 Identity** 

## `class RNS.Identity(` _create_keys=True_ `)` 

This class is used to manage identities in Reticulum. It provides methods for encryption, decryption, signatures and verification, and is the basis for all encrypted communication over Reticulum networks. 

## **Parameters** 

`create_keys` – Specifies whether new encryption and signing keys should be generated. 

## `CURVE = 'Curve25519'` 

The curve used for Elliptic Curve DH key exchanges 

## `KEYSIZE = 512` 

X.25519 key size in bits. A complete key is the concatenation of a 256 bit encryption key, and a 256 bit signing key. 

## `RATCHETSIZE = 256` 

- X.25519 ratchet key size in bits. 

## `RATCHET_EXPIRY = 2592000` 

The expiry time for received ratchets in seconds, defaults to 30 days. Reticulum will always use the most recently announced ratchet, and remember it for up to `RATCHET_EXPIRY` since receiving it, after which it will be discarded. If a newer ratchet is announced in the meantime, it will be replace the already known ratchet. 

## `TRUNCATED_HASHLENGTH = 128` 

Constant specifying the truncated hash length (in bits) used by Reticulum for addressable hashes and other purposes. Non-configurable. 

## `static recall(` _target_hash_ , _from_identity_hash=False_ , __no_use=False_ `)` 

Recall identity for a destination or identity hash. By default, this function will return the identity associated with a given _destination_ hash. As an example, if you know the `lxmf.delivery` destination hash of an endpoint, this function will return the associated underlying identity. You can also search for an identity from a known _identity hash_ , by setting the `from_identity_hash` argument. 

## **Parameters** 

- `target_hash` – Destination or identity hash as _bytes_ . 

- `from_identity_hash` – Whether to search based on identity hash instead of destination hash as _bool_ . 

**15.2. Identity** 

**231** 

**Reticulum Network Stack, Release 1.3.0** 

## **Returns** 

An _RNS.Identity_ instance that can be used to create an outgoing _RNS.Destination_ , or _None_ if the destination is unknown. 

## `static recall_app_data(` _destination_hash_ , __no_use=False_ `)` 

Recall last heard app_data for a destination hash. 

## **Parameters** 

`destination_hash` – Destination hash as _bytes_ . 

## **Returns** 

_Bytes_ containing app_data, or _None_ if the destination is unknown. 

## `static full_hash(` _data_ `)` 

Get a SHA-256 hash of passed data. 

## **Parameters** 

`data` – Data to be hashed as _bytes_ . 

## **Returns** 

SHA-256 hash as _bytes_ . 

## `static truncated_hash(` _data_ `)` 

Get a truncated SHA-256 hash of passed data. 

## **Parameters** 

`data` – Data to be hashed as _bytes_ . 

## **Returns** 

Truncated SHA-256 hash as _bytes_ . 

## `static get_random_hash()` 

Get a random SHA-256 hash. 

## **Parameters** 

`data` – Data to be hashed as _bytes_ . 

## **Returns** 

Truncated SHA-256 hash of random data as _bytes_ . 

## `static current_ratchet_id(` _destination_hash_ `)` 

Get the ID of the currently used ratchet key for a given destination hash 

## **Parameters** 

`destination_hash` – A destination hash as _bytes_ . 

## **Returns** 

A ratchet ID as _bytes_ or _None_ . 

## `static from_bytes(` _prv_bytes_ `)` 

Create a new _RNS.Identity_ instance from _bytes_ of private key. Can be used to load previously created and saved identities into Reticulum. 

## **Parameters** 

`prv_bytes` – The _bytes_ of private a saved private key. **HAZARD!** Never use this to generate a new key by feeding random data in prv_bytes. 

## **Returns** 

A _RNS.Identity_ instance, or _None_ if the _bytes_ data was invalid. 

**Chapter 15. API Reference** 

**232** 

**Reticulum Network Stack, Release 1.3.0** 

## `static from_file(` _path_ `)` 

Create a new _RNS.Identity_ instance from a file. Can be used to load previously created and saved identities into Reticulum. 

## **Parameters** 

`path` – The full path to the saved _RNS.Identity_ data 

## **Returns** 

A _RNS.Identity_ instance, or _None_ if the loaded data was invalid. 

## `to_file(` _path_ `)` 

Saves the identity to a file. This will write the private key to disk, and anyone with access to this file will be able to decrypt all communication for the identity. Be very careful with this method. 

## **Parameters** 

`path` – The full path specifying where to save the identity. 

## **Returns** 

True if the file was saved, otherwise False. 

## `pub_to_file(` _path_ `)` 

Saves the public identity to a file. 

## **Parameters** 

`path` – The full path specifying where to save the identity. 

## **Returns** 

True if the file was saved, otherwise False. 

## `get_private_key()` 

## **Returns** 

The private key as _bytes_ 

```
get_public_key()
```

## **Returns** 

The public key as _bytes_ 

## `load_private_key(` _prv_bytes_ `)` 

Load a private key into the instance. 

## **Parameters** 

`prv_bytes` – The private key as _bytes_ . 

## **Returns** 

True if the key was loaded, otherwise False. 

## `load_public_key(` _pub_bytes_ `)` 

Load a public key into the instance. 

## **Parameters** 

`pub_bytes` – The public key as _bytes_ . 

## **Returns** 

True if the key was loaded, otherwise False. 

`encrypt(` _plaintext_ , _ratchet=None_ `)` 

Encrypts information for the identity. 

## **Parameters** 

`plaintext` – The plaintext to be encrypted as _bytes_ . 

**15.2. Identity** 

**233** 

**Reticulum Network Stack, Release 1.3.0** 

## **Returns** 

Ciphertext token as _bytes_ . 

## **Raises** 

_KeyError_ if the instance does not hold a public key. 

`decrypt(` _ciphertext_token_ , _ratchets=None_ , _enforce_ratchets=False_ , _ratchet_id_receiver=None_ `)` 

Decrypts information for the identity. 

## **Parameters** 

`ciphertext` – The ciphertext to be decrypted as _bytes_ . 

## **Returns** 

Plaintext as _bytes_ , or _None_ if decryption fails. 

## **Raises** 

_KeyError_ if the instance does not hold a private key. 

## `sign(` _message_ `)` 

Signs information by the identity. 

## **Parameters** 

`message` – The message to be signed as _bytes_ . 

## **Returns** 

Signature as _bytes_ . 

## **Raises** 

_KeyError_ if the instance does not hold a private key. 

`validate(` _signature_ , _message_ `)` 

Validates the signature of a signed message. 

## **Parameters** 

- `signature` – The signature to be validated as _bytes_ . 

- `message` – The message to be validated as _bytes_ . 

## **Returns** 

True if the signature is valid, otherwise False. 

## **Raises** 

_KeyError_ if the instance does not hold a public key. 

## **15.3 Destination** 

`class RNS.Destination(` _identity_ , _direction_ , _type_ , _app_name_ , _*aspects_ `)` 

A class used to describe endpoints in a Reticulum Network. Destination instances are used both to create outgoing and incoming endpoints. The destination type will decide if encryption, and what type, is used in communication with the endpoint. A destination can also announce its presence on the network, which will distribute necessary keys for encrypted communication with it. 

## **Parameters** 

- `identity` – An instance of _RNS.Identity_ . Can hold only public keys for an outgoing destination, or holding private keys for an ingoing. 

- `direction` – `RNS.Destination.IN` or `RNS.Destination.OUT` . 

- `type` – `RNS.Destination.SINGLE` , `RNS.Destination.GROUP` or `RNS.Destination. PLAIN` . 

**Chapter 15. API Reference** 

**234** 

**Reticulum Network Stack, Release 1.3.0** 

- `app_name` – A string specifying the app name. 

- `*aspects` – Any non-zero number of string arguments. 

## `RATCHET_COUNT = 512` 

The default number of generated ratchet keys a destination will retain, if it has ratchets enabled. 

## `RATCHET_INTERVAL = 1800` 

The minimum interval between rotating ratchet keys, in seconds. 

`static expand_name(` _identity_ , _app_name_ , _*aspects_ `)` 

## **Returns** 

A string containing the full human-readable name of the destination, for an app_name and a number of aspects. 

`static app_and_aspects_from_name(` _full_name_ `)` 

## **Returns** 

A tuple containing the app name and a list of aspects, for a full-name string. 

`static hash_from_name_and_identity(` _full_name_ , _identity_ `)` 

## **Returns** 

A destination name in adressable hash form, for a full name string and Identity instance. 

`static hash(` _identity_ , _app_name_ , _*aspects_ `)` 

## **Returns** 

A destination name in adressable hash form, for an app_name and a number of aspects. 

## `announce(` _app_data=None_ , _path_response=False_ , _attached_interface=None_ , _tag=None_ , _send=True_ `)` 

Creates an announce packet for this destination and broadcasts it on all relevant interfaces. Application specific data can be added to the announce. 

## **Parameters** 

- `app_data` – _bytes_ containing the app_data. 

- `path_response` – Internal flag used by _RNS.Transport_ . Ignore. 

## `accepts_links(` _accepts=None_ `)` 

Set or query whether the destination accepts incoming link requests. 

## **Parameters** 

`accepts` – If `True` or `False` , this method sets whether the destination accepts incoming link requests. If not provided or `None` , the method returns whether the destination currently accepts link requests. 

## **Returns** 

`True` or `False` depending on whether the destination accepts incoming link requests, if the _accepts_ parameter is not provided or `None` . 

`set_link_established_callback(` _callback_ `)` 

Registers a function to be called when a link has been established to this destination. 

## **Parameters** 

`callback` – A function or method with the signature _callback(link)_ to be called when a new link is established with this destination. 

**15.3. Destination** 

**235** 

**Reticulum Network Stack, Release 1.3.0** 

## `set_packet_callback(` _callback_ `)` 

Registers a function to be called when a packet has been received by this destination. 

## **Parameters** 

`callback` – A function or method with the signature _callback(data, packet)_ to be called when this destination receives a packet. 

## `set_proof_requested_callback(` _callback_ `)` 

Registers a function to be called when a proof has been requested for a packet sent to this destination. Allows control over when and if proofs should be returned for received packets. 

## **Parameters** 

`callback` – A function or method to with the signature _callback(packet)_ be called when a packet that requests a proof is received. The callback must return one of True or False. If the callback returns True, a proof will be sent. If it returns False, a proof will not be sent. 

## `set_proof_strategy(` _proof_strategy_ `)` 

Sets the destinations proof strategy. 

## **Parameters** 

`proof_strategy` – One of `RNS.Destination.PROVE_NONE` , `RNS.Destination. PROVE_ALL` or `RNS.Destination.PROVE_APP` . If `RNS.Destination.PROVE_APP` is set, the _proof_requested_callback_ will be called to determine whether a proof should be sent or not. 

`register_request_handler(` _path_ , _response_generator=None_ , _allow=ALLOW_NONE_ , _allowed_list=None_ , _auto_compress=True_ `)` 

Registers a request handler. 

## **Parameters** 

- `path` – The path for the request handler to be registered. 

- `response_generator` – A function or method with the signature _response_generator(path, data, request_id, link_id, remote_identity, requested_at)_ to be called. Whatever this funcion returns will be sent as a response to the requester. If the function returns `None` , no response will be sent. 

- `allow` – One of `RNS.Destination.ALLOW_NONE` , `RNS.Destination.ALLOW_ALL` or `RNS.Destination.ALLOW_LIST` . If `RNS.Destination.ALLOW_LIST` is set, the request handler will only respond to requests for identified peers in the supplied list. 

- `allowed_list` – A list of _bytes-like RNS.Identity_ hashes. 

- `auto_compress` – If `True` or `False` , determines whether automatic compression of responses should be carried out. If set to an integer value, responses will only be autocompressed if under this size in bytes. If omitted, the default compression settings will be followed. 

## **Raises** 

`ValueError` if any of the supplied arguments are invalid. 

## `deregister_request_handler(` _path_ `)` 

Deregisters a request handler. 

## **Parameters** 

`path` – The path for the request handler to be deregistered. 

## **Returns** 

True if the handler was deregistered, otherwise False. 

**Chapter 15. API Reference** 

**236** 

**Reticulum Network Stack, Release 1.3.0** 

## `enable_ratchets(` _ratchets_path_ `)` 

Enables ratchets on the destination. When ratchets are enabled, Reticulum will automatically rotate the keys used to encrypt packets to this destination, and include the latest ratchet key in announces. 

Enabling ratchets on a destination will provide forward secrecy for packets sent to that destination, even when sent outside a `Link` . The normal Reticulum `Link` establishment procedure already performs its own ephemeral key exchange for each link establishment, which means that ratchets are not necessary to provide forward secrecy for links. 

Enabling ratchets will have a small impact on announce size, adding 32 bytes to every sent announce. 

## **Parameters** 

`ratchets_path` – The path to a file to store ratchet data in. 

## **Returns** 

True if the operation succeeded, otherwise False. 

## `enforce_ratchets()` 

When ratchet enforcement is enabled, this destination will never accept packets that use its base Identity key for encryption, but only accept packets encrypted with one of the retained ratchet keys. 

## `set_retained_ratchets(` _retained_ratchets_ `)` 

Sets the number of previously generated ratchet keys this destination will retain, and try to use when decrypting incoming packets. Defaults to `Destination.RATCHET_COUNT` . 

## **Parameters** 

`retained_ratchets` – The number of generated ratchets to retain. 

## **Returns** 

True if the operation succeeded, False if not. 

## `set_ratchet_interval(` _interval_ `)` 

Sets the minimum interval in seconds between ratchet key rotation. Defaults to `Destination. RATCHET_INTERVAL` . 

## **Parameters** 

`interval` – The minimum interval in seconds. 

## **Returns** 

True if the operation succeeded, False if not. 

```
create_keys()
```

For a `RNS.Destination.GROUP` type destination, creates a new symmetric key. 

## **Raises** 

`TypeError` if called on an incompatible type of destination. 

```
get_private_key()
```

For a `RNS.Destination.GROUP` type destination, returns the symmetric private key. 

**Raises** 

`TypeError` if called on an incompatible type of destination. 

`load_private_key(` _key_ `)` 

For a `RNS.Destination.GROUP` type destination, loads a symmetric private key. 

**Parameters** 

`key` – A _bytes-like_ containing the symmetric key. 

**Raises** 

`TypeError` if called on an incompatible type of destination. 

**15.3. Destination** 

**237** 

**Reticulum Network Stack, Release 1.3.0** 

## `encrypt(` _plaintext_ `)` 

Encrypts information for `RNS.Destination.SINGLE` or `RNS.Destination.GROUP` type destination. 

## **Parameters** 

`plaintext` – A _bytes-like_ containing the plaintext to be encrypted. 

## **Raises** 

`ValueError` if destination does not hold a necessary key for encryption. 

`decrypt(` _ciphertext_ `)` 

Decrypts information for `RNS.Destination.SINGLE` or `RNS.Destination.GROUP` type destination. 

## **Parameters** 

`ciphertext` – _Bytes_ containing the ciphertext to be decrypted. 

**Raises** 

`ValueError` if destination does not hold a necessary key for decryption. 

## `sign(` _message_ `)` 

Signs information for `RNS.Destination.SINGLE` type destination. 

## **Parameters** 

`message` – _Bytes_ containing the message to be signed. 

## **Returns** 

A _bytes-like_ containing the message signature, or _None_ if the destination could not sign the message. 

`set_default_app_data(` _app_data=None_ `)` 

Sets the default app_data for the destination. If set, the default app_data will be included in every announce sent by the destination, unless other app_data is specified in the _announce_ method. 

## **Parameters** 

`app_data` – A _bytes-like_ containing the default app_data, or a _callable_ returning a _bytes-like_ containing the app_data. 

## `clear_default_app_data()` 

Clears default app_data previously set for the destination. 

## **15.4 Packet** 

`class RNS.Packet(` _destination_ , _data_ , _create_receipt=True_ `)` 

The Packet class is used to create packet instances that can be sent over a Reticulum network. Packets will automatically be encrypted if they are addressed to a `RNS.Destination.SINGLE` destination, `RNS.Destination. GROUP` destination or a _RNS.Link_ . 

For `RNS.Destination.GROUP` destinations, Reticulum will use the pre-shared key configured for the destination. All packets to group destinations are encrypted with the same AES-256 key. 

For `RNS.Destination.SINGLE` destinations, Reticulum will use a newly derived ephemeral AES-256 key for every packet. 

For _RNS.Link_ destinations, Reticulum will use per-link ephemeral keys, and offers **Forward Secrecy** . 

## **Parameters** 

- `destination` – A _RNS.Destination_ instance to which the packet will be sent. 

- `data` – The data payload to be included in the packet as _bytes_ . 

**Chapter 15. API Reference** 

**238** 

**Reticulum Network Stack, Release 1.3.0** 

- `create_receipt` – Specifies whether a _RNS.PacketReceipt_ should be created when instantiating the packet. 

`ENCRYPTED_MDU = 383` The maximum size of the payload data in a single encrypted packet `PLAIN_MDU = 464` The maximum size of the payload data in a single unencrypted packet `send()` Sends the packet. 

**Returns** A _RNS.PacketReceipt_ instance if _create_receipt_ was set to _True_ when the packet was instantiated, if not returns _None_ . If the packet could not be sent _False_ is returned. `resend()` Re-sends the packet. 

## **Returns** 

A _RNS.PacketReceipt_ instance if _create_receipt_ was set to _True_ when the packet was instantiated, if not returns _None_ . If the packet could not be sent _False_ is returned. `get_rssi()` 

**Returns** The physical layer _Received Signal Strength Indication_ if available, otherwise `None` . 

```
get_snr()
```

**Returns** The physical layer _Signal-to-Noise Ratio_ if available, otherwise `None` . 

```
get_q()
```

**Returns** The physical layer _Link Quality_ if available, otherwise `None` . 

## **15.5 Packet Receipt** 

## `class RNS.PacketReceipt` 

The PacketReceipt class is used to receive notifications about _RNS.Packet_ instances sent over the network. Instances of this class are never created manually, but always returned from the _send()_ method of a _RNS.Packet_ instance. 

```
get_status()
```

## **Returns** 

The status of the associated _RNS.Packet_ instance. Can be one of `RNS.PacketReceipt. SENT` , `RNS.PacketReceipt.DELIVERED` , `RNS.PacketReceipt.FAILED` or `RNS. PacketReceipt.CULLED` . 

```
get_rtt()
```

## **Returns** 

The round-trip-time in seconds 

**15.5. Packet Receipt** 

**239** 

**Reticulum Network Stack, Release 1.3.0** 

## `set_timeout(` _timeout_ `)` 

Sets a timeout in seconds 

## **Parameters** 

`timeout` – The timeout in seconds. 

## `set_delivery_callback(` _callback_ `)` 

Sets a function that gets called if a successfull delivery has been proven. 

## **Parameters** 

`callback` – A _callable_ with the signature _callback(packet_receipt)_ 

## `set_timeout_callback(` _callback_ `)` 

Sets a function that gets called if the delivery times out. 

## **Parameters** 

`callback` – A _callable_ with the signature _callback(packet_receipt)_ 

## **15.6 Link** 

`class RNS.Link(` _destination_ , _established_callback=None_ , _closed_callback=None_ `)` 

This class is used to establish and manage links to other peers. When a link instance is created, Reticulum will attempt to establish verified and encrypted connectivity with the specified destination. 

## **Parameters** 

- `destination` – A _RNS.Destination_ instance which to establish a link to. 

- `established_callback` – An optional function or method with the signature _callback(link)_ to be called when the link has been established. 

- `closed_callback` – An optional function or method with the signature _callback(link)_ to be called when the link is closed. 

## `CURVE = 'Curve25519'` 

The curve used for Elliptic Curve DH key exchanges 

## `ESTABLISHMENT_TIMEOUT_PER_HOP = 6` 

Timeout for link establishment in seconds per hop to destination. 

## `KEEPALIVE_TIMEOUT_FACTOR = 4` 

RTT timeout factor used in link timeout calculation. 

## `STALE_GRACE = 5` 

Grace period in seconds used in link timeout calculation. 

## `KEEPALIVE = 360` 

Default interval for sending keep-alive packets on established links in seconds. 

## `STALE_TIME = 720` 

If no traffic or keep-alive packets are received within this period, the link will be marked as stale, and a final keep-alive packet will be sent. If after this no traffic or keep-alive packets are received within `RTT` * `KEEPALIVE_TIMEOUT_FACTOR` + `STALE_GRACE` , the link is considered timed out, and will be torn down. 

## `identify(` _identity_ `)` 

Identifies the initiator of the link to the remote peer. This can only happen once the link has been established, and is carried out over the encrypted link. The identity is only revealed to the remote peer, and initiator anonymity is thus preserved. This method can be used for authentication. 

**Chapter 15. API Reference** 

**240** 

**Reticulum Network Stack, Release 1.3.0** 

## **Parameters** 

`identity` – An RNS.Identity instance to identify as. 

- `request(` _path_ , _data=None_ , _response_callback=None_ , _failed_callback=None_ , _progress_callback=None_ , _timeout=None_ `)` 

Sends a request to the remote peer. 

## **Parameters** 

- `path` – The request path. 

- `response_callback` – An optional function or method with the signature _response_callback(request_receipt)_ to be called when a response is received. See the _Request Example_ for more info. 

- `failed_callback` – An optional function or method with the signature _failed_callback(request_receipt)_ to be called when a request fails. See the _Request Example_ for more info. 

- `progress_callback` – An optional function or method with the signature _progress_callback(request_receipt)_ to be called when progress is made receiving the response. Progress can be accessed as a float between 0.0 and 1.0 by the _request_receipt.progress_ property. 

- `timeout` – An optional timeout in seconds for the request. If _None_ is supplied it will be calculated based on link RTT. 

## **Returns** 

A _RNS.RequestReceipt_ instance if the request was sent, or _False_ if it was not. 

`track_phy_stats(` _track_ `)` 

You can enable physical layer statistics on a per-link basis. If this is enabled, and the link is running over an interface that supports reporting physical layer statistics, you will be able to retrieve stats such as _RSSI_ , _SNR_ and physical _Link Quality_ for the link. 

## **Parameters** 

`track` – Whether or not to keep track of physical layer statistics. Value must be `True` or `False` . 

```
get_rssi()
```

## **Returns** 

The physical layer _Received Signal Strength Indication_ if available, otherwise `None` . Physical layer statistics must be enabled on the link for this method to return a value. 

```
get_snr()
```

## **Returns** 

The physical layer _Signal-to-Noise Ratio_ if available, otherwise `None` . Physical layer statistics must be enabled on the link for this method to return a value. 

```
get_q()
```

## **Returns** 

The physical layer _Link Quality_ if available, otherwise `None` . Physical layer statistics must be enabled on the link for this method to return a value. 

```
get_establishment_rate()
```

## **Returns** 

The data transfer rate at which the link establishment procedure ocurred, in bits per second. 

**15.6. Link** 

**241** 

**Reticulum Network Stack, Release 1.3.0** 

```
get_mtu()
```

## **Returns** 

The MTU of an established link. 

```
get_mdu()
```

## **Returns** 

The packet MDU of an established link. 

```
get_expected_rate()
```

## **Returns** 

The packet expected in-flight data rate of an established link. 

```
get_mode()
```

## **Returns** 

The mode of an established link. 

```
get_age()
```

## **Returns** 

The time in seconds since this link was established. 

```
no_inbound_for()
```

## **Returns** 

The time in seconds since last inbound packet on the link. This includes keepalive packets. 

```
no_outbound_for()
```

## **Returns** 

The time in seconds since last outbound packet on the link. This includes keepalive packets. 

```
no_data_for()
```

## **Returns** 

The time in seconds since payload data traversed the link. This excludes keepalive packets. 

```
inactive_for()
```

## **Returns** 

The time in seconds since activity on the link. This includes keepalive packets. 

```
get_remote_identity()
```

## **Returns** 

The identity of the remote peer, if it is known. Calling this method will not query the remote initiator to reveal its identity. Returns `None` if the link initiator has not already independently called the `identify(identity)` method. 

## `teardown()` 

Closes the link and purges encryption keys. New keys will be used if a new link to the same destination is established. 

## `get_channel()` 

Get the `Channel` for this link. 

**Returns** `Channel` object 

**Chapter 15. API Reference** 

**242** 

**Reticulum Network Stack, Release 1.3.0** 

## `set_link_closed_callback(` _callback_ `)` 

Registers a function to be called when a link has been torn down. 

## **Parameters** 

`callback` – A function or method with the signature _callback(link)_ to be called. 

## `set_packet_callback(` _callback_ `)` 

Registers a function to be called when a packet has been received over this link. 

## **Parameters** 

`callback` – A function or method with the signature _callback(message, packet)_ to be called. 

## `set_resource_callback(` _callback_ `)` 

Registers a function to be called when a resource has been advertised over this link. If the function returns _True_ the resource will be accepted. If it returns _False_ it will be ignored. 

## **Parameters** 

`callback` – A function or method with the signature _callback(resource)_ to be called. Please note that only the basic information of the resource is available at this time, such as _get_transfer_size()_ , _get_data_size()_ , _get_parts()_ and _is_compressed()_ . 

## `set_resource_started_callback(` _callback_ `)` 

Registers a function to be called when a resource has begun transferring over this link. 

## **Parameters** 

`callback` – A function or method with the signature _callback(resource)_ to be called. 

## `set_resource_concluded_callback(` _callback_ `)` 

Registers a function to be called when a resource has concluded transferring over this link. 

## **Parameters** 

`callback` – A function or method with the signature _callback(resource)_ to be called. 

## `set_remote_identified_callback(` _callback_ `)` 

Registers a function to be called when an initiating peer has identified over this link. 

## **Parameters** 

`callback` – A function or method with the signature _callback(link, identity)_ to be called. 

## `set_resource_strategy(` _resource_strategy_ `)` 

Sets the resource strategy for the link. 

## **Parameters** 

`resource_strategy` – One of `RNS.Link.ACCEPT_NONE` , `RNS.Link.ACCEPT_ALL` or `RNS.Link.ACCEPT_APP` . If `RNS.Link.ACCEPT_APP` is set, the _resource_callback_ will be called to determine whether the resource should be accepted or not. 

## **Raises** 

_TypeError_ if the resource strategy is unsupported. 

## **15.7 Request Receipt** 

## `class RNS.RequestReceipt` 

An instance of this class is returned by the `request` method of `RNS.Link` instances. It should never be instantiated manually. It provides methods to check status, response time and response data when the request concludes. 

**15.7. Request Receipt** 

**243** 

**Reticulum Network Stack, Release 1.3.0** 

```
get_request_id()
```

**Returns** 

The request ID as _bytes_ . 

```
get_status()
```

**Returns** 

The current status of the request, one of `RNS.RequestReceipt.FAILED` , `RNS. RequestReceipt.SENT` , `RNS.RequestReceipt.DELIVERED` , `RNS.RequestReceipt. READY` . `get_progress()` 

## **Returns** 

The progress of a response being received as a _float_ between 0.0 and 1.0. 

```
get_response()
```

**Returns** The response as _bytes_ if it is ready, otherwise _None_ . 

```
get_response_time()
```

**Returns** 

The response time of the request in seconds. 

```
concluded()
```

## **Returns** 

True if the associated request has concluded (successfully or with a failure), otherwise False. 

## **15.8 Resource** 

`class RNS.Resource(` _data_ , _link_ , _advertise=True_ , _auto_compress=True_ , _callback=None_ , _progress_callback=None_ , _timeout=None_ `)` 

The Resource class allows transferring arbitrary amounts of data over a link. It will automatically handle sequencing, compression, coordination and checksumming. 

## **Parameters** 

- `data` – The data to be transferred. Can be _bytes_ or an open _file handle_ . See the _Filetransfer Example_ for details. 

- `link` – The _RNS.Link_ instance on which to transfer the data. 

- `advertise` – Optional. Whether to automatically advertise the resource. Can be _True_ or _False_ . 

- `auto_compress` – Optional. Whether to auto-compress the resource. Can be _True_ or _False_ . 

- `callback` – An optional _callable_ with the signature _callback(resource)_ . Will be called when the resource transfer concludes. 

- `progress_callback` – An optional _callable_ with the signature _callback(resource)_ . Will be called whenever the resource transfer progress is updated. 

## `advertise()` 

Advertise the resource. If the other end of the link accepts the resource advertisement it will begin transferring. 

**Chapter 15. API Reference** 

**244** 

**Reticulum Network Stack, Release 1.3.0** 

```
cancel()
```

Cancels transferring the resource. 

```
get_progress()
```

**Returns** 

The current progress of the resource transfer as a _float_ between 0.0 and 1.0. 

```
get_transfer_size()
```

**Returns** 

The number of bytes needed to transfer the resource. 

```
get_data_size()
```

**Returns** The total data size of the resource. 

```
get_parts()
```

**Returns** 

The number of parts the resource will be transferred in. 

```
get_segments()
```

## **Returns** 

The number of segments the resource is divided into. 

```
get_hash()
```

**Returns** The hash of the resource. 

```
is_compressed()
```

**Returns** 

Whether the resource is compressed. 

## **15.9 Channel** 

```
classRNS.Channel.Channel
```

Provides reliable delivery of messages over a link. 

`Channel` differs from `Request` and `Resource` in some important ways: 

## **Continuous** 

Messages can be sent or received as long as the `Link` is open. 

## **Bi-directional** 

Messages can be sent in either direction on the `Link` ; neither end is the client or server. 

## **Size-constrained** 

Messages must be encoded into a single packet. 

`Channel` is similar to `Packet` , except that it provides reliable delivery (automatic retries) as well as a structure for exchanging several types of messages over the `Link` . 

`Channel` is not instantiated directly, but rather obtained from a `Link` with `get_channel()` . 

**15.9. Channel** 

**245** 

**Reticulum Network Stack, Release 1.3.0** 

## `register_message_type(` _message_class: Type[_ MessageBase _]_ `)` 

Register a message class for reception over a `Channel` . 

Message classes must extend `MessageBase` . 

## **Parameters** 

`message_class` – Class to register 

`add_message_handler(` _callback: MessageCallbackType_ `)` 

Add a handler for incoming messages. A handler has the following signature: 

```
(message:MessageBase)->bool
```

Handlers are processed in the order they are added. If any handler returns True, processing of the message stops; handlers after the returning handler will not be called. 

## **Parameters** 

`callback` – Function to call 

`remove_message_handler(` _callback: MessageCallbackType_ `)` 

Remove a handler added with `add_message_handler` . 

## **Parameters** 

`callback` – handler to remove 

## `is_ready_to_send()` _→_ bool 

Check if `Channel` is ready to send. 

## **Returns** 

True if ready 

`send(` _message:_ MessageBase `)` _→_ Envelope 

Send a message. If a message send is attempted and `Channel` is not ready, an exception is thrown. 

## **Parameters** 

`message` – an instance of a `MessageBase` subclass 

## `property mdu` 

Maximum Data Unit: the number of bytes available for a message to consume in a single send. This value is adjusted from the `Link` MDU to accommodate message header information. 

## **Returns** 

number of bytes available 

## **15.10 MessageBase** 

## `class RNS.MessageBase` 

Base type for any messages sent or received on a Channel. Subclasses must define the two abstract methods as well as the `MSGTYPE` class variable. 

## `MSGTYPE = None` 

Defines a unique identifier for a message class. 

- Must be unique within all classes registered with a `Channel` 

- Must be less than `0xf000` . Values greater than or equal to `0xf000` are reserved. 

`abstractmethod pack()` _→_ bytes 

Create and return the binary representation of the message 

**Chapter 15. API Reference** 

**246** 

**Reticulum Network Stack, Release 1.3.0** 

## **Returns** 

binary representation of message 

## `abstractmethod unpack(` _raw: bytes_ `)` 

Populate message from binary representation 

## **Parameters** 

`raw` – binary representation 

## **15.11 Buffer** 

## `class RNS.Buffer` 

Static functions for creating buffered streams that send and receive over a `Channel` . 

These functions use `BufferedReader` , `BufferedWriter` , and `BufferedRWPair` to add buffering to `RawChannelReader` and `RawChannelWriter` . 

`static create_reader(` _stream_id: int_ , _channel:_ Channel, _ready_callback: Callable[[int], None] | None = None_ `)` _→_ BufferedReader 

Create a buffered reader that reads binary data sent over a `Channel` , with an optional callback when new data is available. 

Callback signature: `(ready_bytes: int) -> None` 

For more information on the reader-specific functions of this object, see the Python documentation for `BufferedReader` 

## **Parameters** 

- `stream_id` – the local stream id to receive from 

- `channel` – the channel to receive on 

- `ready_callback` – function to call when new data is available 

## **Returns** 

a BufferedReader object 

`static create_writer(` _stream_id: int_ , _channel:_ Channel `)` _→_ BufferedWriter 

Create a buffered writer that writes binary data over a `Channel` . 

For more information on the writer-specific functions of this object, see the Python documentation for `BufferedWriter` 

## **Parameters** 

- `stream_id` – the remote stream id to send to 

- `channel` – the channel to send on 

## **Returns** 

a BufferedWriter object 

`static create_bidirectional_buffer(` _receive_stream_id: int_ , _send_stream_id: int_ , _channel:_ Channel, _ready_callback: Callable[[int], None] | None = None_ `)` _→_ BufferedRWPair 

Create a buffered reader/writer pair that reads and writes binary data over a `Channel` , with an optional callback when new data is available. 

Callback signature: `(ready_bytes: int) -> None` 

**15.11. Buffer** 

**247** 

**Reticulum Network Stack, Release 1.3.0** 

For more information on the reader-specific functions of this object, see the Python documentation for `BufferedRWPair` 

## **Parameters** 

- `receive_stream_id` – the local stream id to receive at 

- `send_stream_id` – the remote stream id to send to 

- `channel` – the channel to send and receive on 

- `ready_callback` – function to call when new data is available 

## **Returns** 

a BufferedRWPair object 

## **15.12 RawChannelReader** 

## `class RNS.RawChannelReader(` _stream_id: int_ , _channel:_ Channel `)` 

An implementation of RawIOBase that receives binary stream data sent over a `Channel` . 

This class generally need not be instantiated directly. Use _`RNS.Buffer.create_reader()`_ , _`RNS. Buffer.create_writer()`_ , and _`RNS.Buffer.create_bidirectional_buffer()`_ functions to create buffered streams with optional callbacks. 

For additional information on the API of this object, see the Python documentation for `RawIOBase` . 

- `__init__(` _stream_id: int_ , _channel:_ Channel `)` 

Create a raw channel reader. 

## **Parameters** 

- `stream_id` – local stream id to receive at 

- `channel` – `Channel` object to receive from 

## `add_ready_callback(` _cb: Callable[[int], None]_ `)` 

Add a function to be called when new data is available. The function should have the signature `(ready_bytes: int) -> None` 

## **Parameters** 

`cb` – function to call 

## `remove_ready_callback(` _cb: Callable[[int], None]_ `)` 

Remove a function added with _`RNS.RawChannelReader.add_ready_callback()`_ 

## **Parameters** 

`cb` – function to remove 

## **15.13 RawChannelWriter** 

## `class RNS.RawChannelWriter(` _stream_id: int_ , _channel:_ Channel `)` 

An implementation of RawIOBase that receives binary stream data sent over a channel. 

This class generally need not be instantiated directly. Use _`RNS.Buffer.create_reader()`_ , _`RNS. Buffer.create_writer()`_ , and _`RNS.Buffer.create_bidirectional_buffer()`_ functions to create buffered streams with optional callbacks. 

For additional information on the API of this object, see the Python documentation for `RawIOBase` . 

**Chapter 15. API Reference** 

**248** 

**Reticulum Network Stack, Release 1.3.0** 

## `__init__(` _stream_id: int_ , _channel:_ Channel `)` 

Create a raw channel writer. 

## **Parameters** 

- `stream_id` – remote stream id to sent do 

- `channel` – `Channel` object to send on 

## **15.14 Transport** 

## `class RNS.Transport` 

Through static methods of this class you can interact with the Transport system of Reticulum. 

## `PATHFINDER_M = 128` 

Maximum amount of hops that Reticulum will transport a packet. 

## `static register_announce_handler(` _handler_ `)` 

Registers an announce handler. 

## **Parameters** 

`handler` – Must be an object with an _aspect_filter_ attribute and a _received_announce(destination_hash, announced_identity, app_data)_ or _received_announce(destination_hash, announced_identity, app_data, announce_packet_hash)_ or _received_announce(destination_hash, announced_identity, app_data, announce_packet_hash, is_path_response)_ callable. Can optionally have a _receive_path_responses_ attribute set to `True` , to also receive all path responses, in addition to live announces. See the _Announce Example_ for more info. 

## `static deregister_announce_handler(` _handler_ `)` 

Deregisters an announce handler. 

## **Parameters** 

`handler` – The announce handler to be deregistered. 

`static has_path(` _destination_hash_ `)` 

## **Parameters** 

`destination_hash` – A destination hash as _bytes_ . 

## **Returns** 

_True_ if a path to the destination is known, otherwise _False_ . 

`static hops_to(` _destination_hash_ `)` 

## **Parameters** 

`destination_hash` – A destination hash as _bytes_ . 

## **Returns** 

The number of hops to the specified destination, or `RNS.Transport.PATHFINDER_M` if the number of hops is unknown. 

`static next_hop(` _destination_hash_ `)` 

## **Parameters** 

`destination_hash` – A destination hash as _bytes_ . 

## **Returns** 

The destination hash as _bytes_ for the next hop to the specified destination, or _None_ if the next hop is unknown. 

**15.14. Transport** 

**249** 

**Reticulum Network Stack, Release 1.3.0** 

`static next_hop_interface(` _destination_hash_ `)` 

## **Parameters** 

`destination_hash` – A destination hash as _bytes_ . 

## **Returns** 

The interface for the next hop to the specified destination, or _None_ if the interface is unknown. 

`static await_path(` _destination_hash_ , _timeout=None_ , _on_interface=None_ `)` 

Requests a path to the destination from the network and blocks until the path is available, or the timeout is reached. 

## **Parameters** 

- `destination_hash` – A destination hash as _bytes_ . 

- `timeout` – An optional timeout in seconds. 

- `on_interface` – If specified, the path request will only be sent on this interface. In normal use, Reticulum handles this automatically, and this parameter should not be used. 

## **Returns** 

_True_ if a path to the destination is found, otherwise _False_ . 

`static request_path(` _destination_hash_ , _on_interface=None_ , _tag=None_ , _recursive=False_ `)` 

Requests a path to the destination from the network. If another reachable peer on the network knows a path, it will announce it. 

## **Parameters** 

- `destination_hash` – A destination hash as _bytes_ . 

- `on_interface` – If specified, the path request will only be sent on this interface. In normal use, Reticulum handles this automatically, and this parameter should not be used. 

## `static blackhole_identity(` _identity_hash_ , _until=None_ , _reason=None_ `)` 

Blackholes an identity. 

## **Parameters** 

- `identity_hash` – The identity hash to blackhole as _bytes_ . 

- `until` – Optional unix timestamp of when the blackhole expires as _float_ or _int_ . 

- `reason` – Optional reason for the blackhole as _str_ . 

## **Returns** 

_True_ if successful, otherwise _False_ . 

## `static unblackhole_identity(` _identity_hash_ `)` 

Lifts blackhole for an identity. 

## **Parameters** 

`identity_hash` – The identity hash to blackhole as _bytes_ . 

## **Returns** 

_True_ if successful, otherwise _False_ . 

**Chapter 15. API Reference** 

**250** 

## **INDEX** 

## Symbols 

`__init__()` ( _RNS.RawChannelReader method_ ), 248 `__init__()` ( _RNS.RawChannelWriter method_ ), 248 

## A 

`accepts_links()` ( _RNS.Destination method_ ), 235 `add_message_handler()` ( _RNS.Channel.Channel method_ ), 246 `add_ready_callback()` ( _RNS.RawChannelReader method_ ), 248 `advertise()` ( _RNS.Resource method_ ), 244 `announce()` ( _RNS.Destination method_ ), 235 `ANNOUNCE_CAP` ( _RNS.Reticulum attribute_ ), 229 `app_and_aspects_from_name()` ( _RNS.Destination static method_ ), 235 `await_path()` ( _RNS.Transport static method_ ), 250 

## B 

`blackhole_identity()` ( _RNS.Transport static method_ ), 250 `blackhole_sources()` ( _RNS.Reticulum static method_ ), 230 `Buffer` ( _class in RNS_ ), 247 

## C 

`cancel()` ( _RNS.Resource method_ ), 244 `Channel` ( _class in RNS.Channel_ ), 245 `clear_default_app_data()` ( _RNS.Destination method_ ), 238 `concluded()` ( _RNS.RequestReceipt method_ ), 244 `create_bidirectional_buffer()` ( _RNS.Buffer static method_ ), 247 `create_keys()` ( _RNS.Destination method_ ), 237 `create_reader()` ( _RNS.Buffer static method_ ), 247 `create_writer()` ( _RNS.Buffer static method_ ), 247 `current_ratchet_id()` ( _RNS.Identity static method_ ), 232 

`CURVE` ( _RNS.Identity attribute_ ), 231 `CURVE` ( _RNS.Link attribute_ ), 240 

## D 

`decrypt()` ( _RNS.Destination method_ ), 238 

`decrypt()` ( _RNS.Identity method_ ), 234 `deregister_announce_handler()` ( _RNS.Transport static method_ ), 249 `deregister_request_handler()` ( _RNS.Destination method_ ), 236 `Destination` ( _class in RNS_ ), 234 `discovered_interfaces()` ( _RNS.Reticulum static method_ ), 231 

## E 

`enable_ratchets()` ( _RNS.Destination method_ ), 236 `encrypt()` ( _RNS.Destination method_ ), 237 `encrypt()` ( _RNS.Identity method_ ), 233 `ENCRYPTED_MDU` ( _RNS.Packet attribute_ ), 239 `enforce_ratchets()` ( _RNS.Destination method_ ), 237 `ESTABLISHMENT_TIMEOUT_PER_HOP` ( _RNS.Link attribute_ ), 240 `expand_name()` ( _RNS.Destination static method_ ), 235 

## F 

`from_bytes()` ( _RNS.Identity static method_ ), 232 `from_file()` ( _RNS.Identity static method_ ), 232 `full_hash()` ( _RNS.Identity static method_ ), 232 

## G 

`get_age()` ( _RNS.Link method_ ), 242 `get_channel()` ( _RNS.Link method_ ), 242 `get_data_size()` ( _RNS.Resource method_ ), 245 `get_establishment_rate()` ( _RNS.Link method_ ), 241 `get_expected_rate()` ( _RNS.Link method_ ), 242 `get_hash()` ( _RNS.Resource method_ ), 245 `get_instance()` ( _RNS.Reticulum static method_ ), 230 `get_mdu()` ( _RNS.Link method_ ), 242 `get_mode()` ( _RNS.Link method_ ), 242 `get_mtu()` ( _RNS.Link method_ ), 241 `get_parts()` ( _RNS.Resource method_ ), 245 `get_private_key()` ( _RNS.Destination method_ ), 237 `get_private_key()` ( _RNS.Identity method_ ), 233 `get_progress()` ( _RNS.RequestReceipt method_ ), 244 `get_progress()` ( _RNS.Resource method_ ), 245 `get_public_key()` ( _RNS.Identity method_ ), 233 `get_q()` ( _RNS.Link method_ ), 241 

**251** 

**Reticulum Network Stack, Release 1.3.0** 

`get_q()` ( _RNS.Packet method_ ), 239 `get_random_hash()` ( _RNS.Identity static method_ ), 232 `get_remote_identity()` ( _RNS.Link method_ ), 242 `get_request_id()` ( _RNS.RequestReceipt method_ ), 243 `get_response()` ( _RNS.RequestReceipt method_ ), 244 `get_response_time()` ( _RNS.RequestReceipt method_ ), 244 

`get_rssi()` ( _RNS.Link method_ ), 241 `get_rssi()` ( _RNS.Packet method_ ), 239 `get_rtt()` ( _RNS.PacketReceipt method_ ), 239 `get_segments()` ( _RNS.Resource method_ ), 245 `get_snr()` ( _RNS.Link method_ ), 241 `get_snr()` ( _RNS.Packet method_ ), 239 `get_status()` ( _RNS.PacketReceipt method_ ), 239 `get_status()` ( _RNS.RequestReceipt method_ ), 244 `get_transfer_size()` ( _RNS.Resource method_ ), 245 

## H 

`has_path()` ( _RNS.Transport static method_ ), 249 `hash()` ( _RNS.Destination static method_ ), 235 `hash_from_name_and_identity()` ( _RNS.Destination static method_ ), 235 `hops_to()` ( _RNS.Transport static method_ ), 249 

## I 

`identify()` ( _RNS.Link method_ ), 240 `Identity` ( _class in RNS_ ), 231 `inactive_for()` ( _RNS.Link method_ ), 242 `interface_discovery_sources()` ( _RNS.Reticulum static method_ ), 231 `is_compressed()` ( _RNS.Resource method_ ), 245 `is_ready_to_send()` ( _RNS.Channel.Channel method_ ), 246 

## K 

`KEEPALIVE` ( _RNS.Link attribute_ ), 240 `KEEPALIVE_TIMEOUT_FACTOR` ( _RNS.Link attribute_ ), 240 `KEYSIZE` ( _RNS.Identity attribute_ ), 231 

## L 

`Link` ( _class in RNS_ ), 240 `LINK_MTU_DISCOVERY` ( _RNS.Reticulum attribute_ ), 229 `link_mtu_discovery()` ( _RNS.Reticulum static method_ ), 230 

`load_private_key()` ( _RNS.Destination method_ ), 237 `load_private_key()` ( _RNS.Identity method_ ), 233 `load_public_key()` ( _RNS.Identity method_ ), 233 

## M 

`mdu` ( _RNS.Channel.Channel property_ ), 246 `MessageBase` ( _class in RNS_ ), 246 `MINIMUM_BITRATE` ( _RNS.Reticulum attribute_ ), 230 `MSGTYPE` ( _RNS.MessageBase attribute_ ), 246 

`MTU` ( _RNS.Reticulum attribute_ ), 229 

## N 

`next_hop()` ( _RNS.Transport static method_ ), 249 `next_hop_interface()` ( _RNS.Transport static method_ ), 249 `no_data_for()` ( _RNS.Link method_ ), 242 `no_inbound_for()` ( _RNS.Link method_ ), 242 `no_outbound_for()` ( _RNS.Link method_ ), 242 

## P 

`pack()` ( _RNS.MessageBase method_ ), 246 `Packet` ( _class in RNS_ ), 238 `PacketReceipt` ( _class in RNS_ ), 239 `PATHFINDER_M` ( _RNS.Transport attribute_ ), 249 `PLAIN_MDU` ( _RNS.Packet attribute_ ), 239 `pub_to_file()` ( _RNS.Identity method_ ), 233 `publish_blackhole_enabled()` ( _RNS.Reticulum static method_ ), 230 

## R 

`RATCHET_COUNT` ( _RNS.Destination attribute_ ), 235 `RATCHET_EXPIRY` ( _RNS.Identity attribute_ ), 231 `RATCHET_INTERVAL` ( _RNS.Destination attribute_ ), 235 `RATCHETSIZE` ( _RNS.Identity attribute_ ), 231 `RawChannelReader` ( _class in RNS_ ), 248 `RawChannelWriter` ( _class in RNS_ ), 248 `recall()` ( _RNS.Identity static method_ ), 231 `recall_app_data()` ( _RNS.Identity static method_ ), 232 `register_announce_handler()` ( _RNS.Transport static method_ ), 249 `register_message_type()` ( _RNS.Channel.Channel method_ ), 245 `register_request_handler()` ( _RNS.Destination method_ ), 236 `remote_management_enabled()` ( _RNS.Reticulum static method_ ), 230 `remove_message_handler()` ( _RNS.Channel.Channel method_ ), 246 

`remove_ready_callback()` ( _RNS.RawChannelReader method_ ), 248 `request()` ( _RNS.Link method_ ), 241 `request_path()` ( _RNS.Transport static method_ ), 250 `RequestReceipt` ( _class in RNS_ ), 243 `required_discovery_value()` ( _RNS.Reticulum static method_ ), 230 `resend()` ( _RNS.Packet method_ ), 239 `Resource` ( _class in RNS_ ), 244 `Reticulum` ( _class in RNS_ ), 229 

## S 

`send()` ( _RNS.Channel.Channel method_ ), 246 `send()` ( _RNS.Packet method_ ), 239 

**Index** 

**252** 

**Reticulum Network Stack, Release 1.3.0** 

`set_default_app_data()` ( _RNS.Destination method_ ), 238 

`set_delivery_callback()` ( _RNS.PacketReceipt method_ ), 240 `set_link_closed_callback()` ( _RNS.Link method_ ), 242 

`set_link_established_callback()` ( _RNS.Destination method_ ), 235 `set_packet_callback()` ( _RNS.Destination method_ ), 235 

`set_packet_callback()` ( _RNS.Link method_ ), 243 

`set_proof_requested_callback()` ( _RNS.Destination method_ ), 236 

`set_proof_strategy()` ( _RNS.Destination method_ ), 236 `set_ratchet_interval()` ( _RNS.Destination method_ ), 237 

`set_remote_identified_callback()` ( _RNS.Link method_ ), 243 `set_resource_callback()` ( _RNS.Link method_ ), 243 `set_resource_concluded_callback()` ( _RNS.Link method_ ), 243 

`set_resource_started_callback()` ( _RNS.Link method_ ), 243 

`set_resource_strategy()` ( _RNS.Link method_ ), 243 `set_retained_ratchets()` ( _RNS.Destination method_ ), 237 

`set_timeout()` ( _RNS.PacketReceipt method_ ), 239 `set_timeout_callback()` ( _RNS.PacketReceipt method_ ), 240 `should_use_implicit_proof()` ( _RNS.Reticulum static method_ ), 230 `sign()` ( _RNS.Destination method_ ), 238 `sign()` ( _RNS.Identity method_ ), 234 `STALE_GRACE` ( _RNS.Link attribute_ ), 240 `STALE_TIME` ( _RNS.Link attribute_ ), 240 

## T 

`teardown()` ( _RNS.Link method_ ), 242 `to_file()` ( _RNS.Identity method_ ), 233 `track_phy_stats()` ( _RNS.Link method_ ), 241 `Transport` ( _class in RNS_ ), 249 `transport_enabled()` ( _RNS.Reticulum static method_ ), 230 `truncated_hash()` ( _RNS.Identity static method_ ), 232 `TRUNCATED_HASHLENGTH` ( _RNS.Identity attribute_ ), 231 

## U 

`unblackhole_identity()` ( _RNS.Transport static method_ ), 250 `unpack()` ( _RNS.MessageBase method_ ), 247 

## V 

`validate()` ( _RNS.Identity method_ ), 234 

**Index** 

**253** 

