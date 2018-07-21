---
layout: post
title:  "share my experience in playong with hyperledger fabric"
date:   2018-07-20 21:26:00 +0800
categories: daily-posts
---

## 7-14
Saw a [contest about blockchain here](https://tianchi.aliyun.com/competition/gameList.htm#tab%3DActive%26pageIndex%3D1) and decided to try it out.  
The experiences about the work are wrote at the end of this article. Before them I wrote a lot of details just for fun...

The site sent emails about contests to my mailbox regularly. I'm not interested in these contests usually. Most of them are related to data analysis with many machine learning algorithms which I disliked a lot. I do not like to solve problems without doing researches about them seriously and simply use some algorithms based on probability theory, and too many people are attracted to the field, going with the stream always makes me anxious and I decide not to pursue what most people are pursuing.   
This contest seems very different. I happened to see another challenge on topcoder about hacking a smart contracts and I read some related materials, though I do not get the work done at last, things about smart contracts really attracted me. This contest seems much easier than the previous one and the time allowed to get work done is much longer, and most importantly it requires  participants to use Go ❤. Following my heart I registered for it and chose a very cool nickname and a very cool pseudo institute name.


 \>\_< Can't help praising [golang's beautiful documentation](https://golang.org/doc), in contrast with that of [Fabric](http://hyperledger-fabric.readthedocs.io/en/latest), I often get confused about how many people have contributed to its documentation. It seems so inconsistent in description in teaching a developer to learn its detail and some of contents get redundant. More love for my beautiful golang with many handy tools. A true modernized language that empowers developers a lot. ❤ ❤ ❤  
emmm, Fabric's example also has some problems in its deploying script, I had to read the script and completed some of its commands manually to get the example run properly....~>_<~....  
Strongly recommend this [documentation in godoc](https://godoc.org/github.com/hyperledger/fabric/core/chaincode/shim#Chaincode
). it is much more clear if you are a [Gopher](https://blog.golang.org/gopher) and are going to implement your code in golang. And in case the version you are used changes its function signature from the documentation, you had better refer [the source code mirror](https://github.com/hyperledger/fabric) in github also.

....emmm..the intellisense in vscode for golang seems not to work under ubuntu...so sad....

## 7-15
The intellisense for golang began to work properly after I restarted my vscode. Strongly recommend vscode for golang developing, with open source [plugin](https://github.com/Microsoft/vscode-go), quick start speed and much lower memory footprint in contrast with visual studio, it is almost the best IDE I have ever seen. ❤ ❤ ❤  
 It seems the Fabric does not follow golang's recommended path convention either, the compiled file was not sent to `bin` directory but in the same directory as the source code...  
 It reminds me of the days when I was developing with verilog under Xilinx software suite...😢...more time spent in struggling with development environment rather than coding and debugging...

## 7-16
It also seems good to do the unit test only. So few instructions for deploying the whole project in its documentation and so many obstacles in the practise...😢 Planning to do the unit test first. See [testing package](https://godoc.org/testing) and [unit test example for chaincode in fabric](https://github.com/hyperledger/fabric/tree/release-1.2/examples/chaincode/go/example02) for a reference.

## 7-17
could not test the part with encryption...seems no interface to import ```transient``` parameter. Find the documentation [Build your first network](http://hyperledger-fabric.readthedocs.io/en/release-1.2/build_network.html) can provide some help, and its [referred directory](https://github.com/hyperledger/fabric-samples/blob/release-1.2/first-network) also helps a lot.

## 7-18 
learned how to write shell scripts and how to use docker from scratch....near the end....😭  
...test passed, uploaded my code, hoping I have understood the meaning of the question correctly...😭
work done...
The qualifying round is really easy in contrast with that of topcoder... but the competition is much less and the average hourly pay (if got successfully) is much higher in topcoder...  

## about 🙄
Happened to find that I really dislike the rules... different from the rules of other contest in this site, the rules showed in this contest indicates that it may required more teams than the number of the eventual prizes to go to the final round. I really do not care what the final teams will show about their works, really do not care the mysterious conference and do not to go to a tourism city 🙄. If some teams are not certain to get the bonus attractive enough, why should they travel so long to go to the final round on site 🙄.  
decided to choose the third topic which is about implementing some basic functionalities supporting hyperledger-fabric. Not caring about the prize now, 🙄 the first two topics are really hard, and I do not think any team here may issue a good solution in a month time. In real world's scenario, there are always a lot of parts to take into consideration and hackers can easily hack your system if any section of your system is unsecure.  
doubt about why they choose Go to implement a framework supporting smart contracts now 🙄, really convinced haskell would be a better choice, or just Rust?  
Anyway, smart contract is a really attractive field, will continue to focus on it.  

## Share some experience in getting work done

Fabric's documents are a bit of a mess and these following parts seems more important:
- [glossary](http://hyperledger-fabric.readthedocs.io/en/release-1.2/glossary.html) learn key concepts in fabric
- [network in fabric](http://hyperledger-fabric.readthedocs.io/en/release-1.2/network/network.html) very important in understanding the test scripts correctly and rewriting them
- [Build your first network](http://hyperledger-fabric.readthedocs.io/en/release-1.2/build_network.html) about testing your chaincode in network
- [Chaincode for developers](http://hyperledger-fabric.readthedocs.io/en/release-1.2/chaincode4ade.html) about testing your chaincode in developing mode, this mode is much easier to use than the previous one and you just need to fix the path mapped to docker containers' path and replace the testcase in tutorials with your own.
- [fabric samples with test scripts](https://github.com/hyperledger/fabric-samples/)
- [godoc for fabric](https://godoc.org/github.com/hyperledger/fabric/core/chaincode/shim) it matters a lot to read the signatures carefully and write your code with many error catches, it helps a lot in quickly locating the error parts and get the feedback from error messages, ```fmt.print()``` seems not to work in chaincode in devmode, I did not read scripts about output carefully and can not provide more details. 

The samples may vary a lot and you may get confused by some parameters' usage, I returned the parameters I got as the results while developing to make it clear.
The encryption parts can be solved using functions in ```bccsp/sw``` and [this example](https://github.com/hyperledger/fabric/tree/master/examples/chaincode/go/enccc_example) helps a lot.   

