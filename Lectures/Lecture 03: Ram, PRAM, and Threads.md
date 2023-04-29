Introduction and Plan

Title: Notes on Parallel Programming Lecture

In this lecture on parallel programming, the speaker starts by acknowledging the audience for braving the cold to be present. He goes on to highlight the plan for the day, which is to examine a couple of examples that set the stage for the entire course, including some more language and pictures for understanding.
 
Accessing the High-Performance Computing Cluster

The lecturer mentions that Amherst College has a new, high-performance computing cluster which students in the course can use. He notes that he will post the first assignment and that the students will be required to write a parallel program to run on their computer and then on the high-performance computing cluster. He admits that the cluster is not yet fully set up, but encourages students to submit the assignment by Friday, regardless.

Terminology

The lecturer emphasizes the importance of understanding some basic concepts such as program, process and execution, even though they can be confusing for novices. He explains that a program is the code written by a programmer, while a process is the computing element that executes those instructions. Execution is the result of those instructions.

Model of Computation

The lecturer goes on to explain the Random Access Machine model of computation, which describes how computing devices interact with memory. The interaction involves reading and writing data through a series of memory and CPU interactions. He provides simple illustrations to explain read and write methods in computer programs.

Counterexample

The speaker gives an example of a simple program that increments a counter by one each time it is called. He explains that this program interacts with memory by reading the value of the counter, incrementing it, and then writing the new value to memory. He explains that problems could arise when multiple processes run concurrently.Multicore Architecture and the P RAM Model

**Introduction**

This text discusses the concept of concurrent programming in multicore architecture and the use of the P RAM model.

**Multicore Architecture and Memory**

Multicore architecture computers can perform multiple tasks at the same time. Each core has access to the same shared memory, and this can pose challenges when multiple cores access the same memory location. One solution is to divide the memory into chunks for different cores, but some tasks still require communication between cores.

**Processes and Concurrency vs. Parallelism**

Laptop or consumer-grade computers usually have 4-8 cores. Multiple concurrent processes can run on one core, but each core can only do one instruction at a time. Multicores enable the computer to do more than one instruction at a time, but this is different from concurrency vs. parallelism, where programs overlap in time vs. doing multiple things at the same time.

**The P RAM Model and Atomic Operations**

The P RAM model is similar to the RAM model, but with multiple cores accessing memory concurrently. The model assumes that all operations are atomic and cannot be divided into smaller pieces. If two processes write to the same location, one operation succeeds, but it is unclear which one. For a read and write, the written value will eventually be stored, but the read value could be either the previous value or the new one.

**Understanding Atomicity**

Atomicity means that an operation cannot be divided into smaller steps. In the RAM and P RAM models, read and write operations are atomic. This is different from physical writing or other operations that can be broken down into smaller steps. In this context, concurrent and parallel processes are functionally the same.

**Conclusion**

Concurrent programming in multicore architecture using the P RAM model requires an understanding of atomic operations and their limitations. Although hardware has been developed to prevent multiple threads from manipulating the same value simultaneously, this is not the default behavior, and programmers must take care to prevent errors.# Atomic Operations in Computation

This text discusses the limitations of read and write operations in computation. It notes that under certain assumptions, there are problems that cannot be solved without atomic operations besides read and write.

## Development of Computer Hardware

The theory of computing drove the development of computer hardware due to mathematical proofs that hardware could not solve certain problems. Therefore, hardware had to be developed with atomic operations to allow for the solution of such problems.

## Computation in Computers

Computation in computers involves read and write operations, with arithmetic taking place in the CPU. However, it is important to break down computations into their atomic elements, similar to the building of molecules from atoms in chemistry.

## Threaded Program Example

An example of a threaded program is given, where two threads concurrently execute the increment operation. The relative timing of the read and write operations of the threads can result in different outcomes in the count variable.

## Embarrassingly Parallel Computation and Mutual Exclusion

Next week's discussion will focus on embarrassingly parallel computation, which involves problems that lend themselves well to parallelism without encountering issues with counters. There will also be a discussion on the limits of parallelism and the problem of mutual exclusion, which involves implementing counter operations with reading and writing operations only.