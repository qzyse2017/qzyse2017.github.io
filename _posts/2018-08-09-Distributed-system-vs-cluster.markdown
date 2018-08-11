---
layout: post
title:  "2018-08-09-Distributed-system-vs-cluster"
date:   2018-08-09 16:55:09 +0800
categories: daily-posts
---


It seems distributed system and cluster are similar to each other in their functionality and behaviours and I want to find out their main differences.  

## Searching answer from  ```Computer Architecture:A Quantitative```
At first, I did not think they are similar and as a super fan of ```Computer Architecture:A Quantitative```, I checked the book and want to get some answer, but I did not get a chapter or section which titled ```distributed system``` or ```cluster```, but it indeed has a chapter talking about the model which can describe the above two systems which titled ```Thread-Level parallelism``` and it talked about the genesis of the thread-level-parallelism trend at the start of the chapter.  

> The turning away from the conventional organization came in the middle 1960s, when the law of diminishing returns began to take 
> effect in the effort to increase the operational speed of a computer.... Electronic circuits are ultimately limited in their 
> speed of operation by the speed of light ... and many of the circuits were already operating in the nanosecond range.         
>    W. Jack Bouknight et al. The Illiac IV System (1972)

And the distributed system by its name may be more similar to the ```distributed shared memory (DSM).``` multimultiprocessors.

```
Existing shared-memory multiprocessors fall into two classes,
depending on the number of processors involved, which in turn dictates
a memory organization and interconnect strategy. We refer to the
multiprocessors by their memory organization because what constitutes
a small or large number of processors is likely to change over time.
...

```

In the book, the authors talked about clusters and DSM multiprocessors in different chapters because they use different strategies to communicate among threads. DSM multiprocessors use shared address space while clusters use network.

``` 
In both SMP and DSM architectures, 
communication among threads occurs through a shared address space.
...
In contrast, the clusters and warehouse-scale computers of the
next chapter look like individual computers connected by a network,
and the memory of one processor cannot be accessed by another
processor without the assistance of software protocols running on both
processors. In such designs, message-passing protocols are used to
communicate data among processors. 
```

With complex computer architectures today, I do not think these classifications can be adapted to every condition but IMHO why the discussion in the book matters a lot is that it describes the key problems engineers have to tackle in their daily work.  
As for clusters and distribued systems(what the authors talked about in his book), the main different problems between these two architectures can be listed below:

1. Distribued systems mainly need engineers to tackle the problem of multiprocessor cache coherence and the specific coherence requirements varies a lot. The authors gave some common protocols in the book.

2. There seems to more problems about network bandwidth and energy consumption in clusters.(the definitions of WSC and clusters are also controversial as discussed in the book)

And the author issued detailed models and gave correspoding data to discussed some possible solutions in practise for these two architectures.

## Answer from stackoverflow and quara
I listed the REF at the last of this post and the discussion here seems to be somewhat similar to what I listed above.  
and I think this statements from John Robertson seems to be rather appropriate to end the problem

```
As Avi says below, those terms often mean what a particular user 
chooses them to mean. They can have a ‘sales’ meaning as well 
as a strictly technical one
```

discussion from stackoverflow in the link below also talked about similar opinions but the user engineers in these two architectures usually struggle with different problems.

```
In general when working with distributed systems you work a lot
with long latencies and unexpected failures (like mentioned in p2p
systems). When building a cluster (or a big cluster which can be
called supercomputer) you try to prevent it by using more robust
hardware and better network interconnection (InfiniBand) 
```

The main differences when people talking about these two architectures may mainly from the four aspects which is listed by the author of the answer, ```John Robertson```.

```
1.Structure
2.Scale
3.Task
4.Price
5.Reliability
```

Other discussions in the link are also worth reading. 

## REF:  
[discussion from quara](https://www.quora.com/What-are-the-differences-between-a-cluster-computer-and-a-distributed-system
)  
[discussion from stackoverflow](https://stackoverflow.com/questions/21378427/what-is-the-difference-between-a-distributed-system-and-a-clustered-system
)  
The book ```Computer Architecture:A Quantitative```


## Some other trivias:

Thanks a lot for my teacher Tang and Chen to choose the great book, ```Computer Architecture:A Quantitative``` as our textbook for the course, computer architecture.  
Not so sure I will choose the course last year, but teacher Tang proudly told us he would be the teacher of another required course and welcomed us to choose his course. He also told us the textbook's name, having read the book before I chose the course, and really convinced it would be a fascinating course, at last I chose the course.  
Not feeling so easy to sit with senior schoolmates and very afraid I would fail the exam, it is really not happy to attend the class. However the textbook is really great, not even got to fully understand ten percent of all the fascinating works from the great masters, I indeed get some great ideas while programming from the book.  
And I found some software engineers programmed just like the models discussed in the book. IMHO It is really a book worth reading for every software engineer, especially the parts ```The programmer's view``` and ```fallacies and pitfalls```.  
Happy to know the two authors(they have been good friends over the years!~) have won Turing Award this year!!!! ```:)```