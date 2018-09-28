---
layout: post
title:  "Haksell compiler on FPGA"
date:   2018-09-14 14:27:05 +0800
categories: daily-posts
---

Learned a little Haskell recently and found Haskell is really like Verilog to some extent.

Haskell program is composed of functions and data, verilog program is composed of different module and IO is important in both language.

They both take a lot of time to compile.😅

They are both good at doing parallel work.

And I thought maybe they are similar in programming paradigms too. And why not try to compile haskell to verilog or just executable files on FPGA?

Tried searching whether someone had done some similar work first.

Seems a lot of people had worked on this problem...

Results from bing.

![search-results](images/search-results.png)


## clash
Its github repository: https://github.com/clash-lang/clash-compiler

Homepage: https://www.clash-lang.org/

It is in fact a functional hardware description language(it describe the hardware directly) but its semantics and syntax is similar to Haskell... emm.. why not write verilog directly... I do not think it is a good solution, it may be welcome only to those who had learned Haskell and start to hardware description language recently...

But it can also be a tradeoff, which lets the user to do some optimization to their program before it run on FPGA.

>Features of CλaSH:
1. Strongly typed, but with a very high degree of type inference, enabling both safe and fast prototyping using concise descriptions.
2. Interactive REPL: load your designs in an interpreter and easily test all your component without needing to setup a test bench.
Higher-order functions, with type inference, result in designs that are fully parametric by default.
3. Synchronous sequential circuit design based on streams of values, called Signals, lead to natural descriptions of feedback loops.
4. Support for multiple clock domains, with type safe clock domain crossing.

Seems point 2, 3 could be features that surpass classic hardware description languge, have not designed any complex systems myself, and not know about the fourth point.

A simple tutorials http://hackage.haskell.org/package/clash-prelude-0.99.3/docs/Clash-Tutorial.html#g:4

rather similar to Haskell in programming mode and syntax, but this abstraction could also be done in verilog, the number of code lines is decreased a lot(logic which may need a lot of lines of code to describe in verilog or VHDL can just be showed with very few lines here!!!) and much dirty work is covered, seems really greater than just use verilog, systemVerilog...

Hasekell seems rather good at code generation work(Haskell is good at data processing work), and there are many previous works on [hackage](http://hackage.haskell.org/packages/#cat:Code%20Generation), clash will also be generated to other languages at last.

May try programming with clash and FPGA myself, if sometimes in the future I will need it, maybe use them to accelerate graphics provessing? But it seems I can do it with GPU and its correspoding language too...Teacher Tang once emphasized in the class that FPGA is used for circuit prototype design at first(because it is programmable versus ASIC, sucessful designs are usually implemented on ASIC at last), but it seems now many people are just use FPGA just as if it was GPU...

Using it to implement some encryption and decryption algorithms seems a good idea! Emmm...have recently also read some news that some people are using ASIC to mine digital coins(ASIC will consume less energy). First, using clash to design a algorithm-specified circuit on FPGA and make it into ASIC?

## Some other similer work
http://www.dougandjean.com/hngn.html The author tried it just about 10 years ago about his version seems simple.

http://catherineh.github.io/programming/2016/12/26/haskell-on-a-xilinx-fpga This blog author tried to let clash work on Xilinx FPGA and introduced his work in detail.

Seems no person has tried to compile Haskell directly to executable program on FPGA, and I have just thinked of that it is not a good a idea, since there is a valid specification for Verilog, VHDL, and systemVerilog, but the executeble program for various FPGA can vary a lot...

Above all, Haskell is really a fascinating language but there seems to be very few people learning it now. In fact, it is very stable, you do not need to adapt yourself to many various new syntax and there are many very smart persons who are supporting this language to grow healthy. Every little change added is considered and debated a lot, and there are many successful usecases in commercial, its community is also very friendly. I guess maybe many people are just thinking it is harder to learn than other language, and you could not write a runnable program until you have learned a lot of it, however, if I start to learn golang or python now, it may just take me a few hours to get the most key points of the language, and I can write a runnable language in a short time. 

Also, it take a lot of time to compile a Haskell language, but in fact, its runtime performance is rather good, a related test results can be seen here, http://greenlab.di.uminho.pt/wp-content/uploads/2017/10/sleFinal.pdf, (C, C++, and Rust are all system-level languages `:)`, Haskell may not do as good as them in performance, but you just need to write much fewer lines of code if you choose Haskell!)

## Some other trivias:

Did not learn verilog well myself, I was not experienced in learning programming language at that time, and teacher Tang just provided us a slide with very limited reference on the language usage and I was not good at learn something from just a summary, I was like AI in some ways, I learned from examples and learned something better because it has more probability to appear.😥

What teacher Tang emphasized in the past really benefited me a lot, though I did not understand the key points at that time, say, he taught us to imagine the circuit in mind while programming using verilog, and taught us to put different module in different files...

And above all, he is one of the most visionary persons I have met in university, many points he talked with us is really valuable. In fact, elder teachers I met in university tends to be more visionary than those younger, e.g. teacher Wang, Guo, Shen, Zhou, Wei... 

Some of them may not very at good at teaching from my perspective(or I just could learn well from those who provided a textbook with a lot of practise...), but they chose very good textbook for us, and they talked a lot of the history of what they have experience in the past, whihc is really heuristic. They also focus more on what they had devoted to, not those fashionable. It made me rethink the real value of these fashionable technologies.

Really apprecicate that I have met these teachers and learned a lot from them!


REF

https://www.clash-lang.org/

http://cufp.org/2012/peter-braam-parallel-scientific-awesome-haskell-fp.html

http://www.dougandjean.com/hngn.html

http://hackage.haskell.org/package/clash-prelude-0.99.3/docs/Clash-Tutorial.html

https://news.8btc.com/gpu-mining-prospectus-equihash-is-no-match-for-ram-assisted-asics





