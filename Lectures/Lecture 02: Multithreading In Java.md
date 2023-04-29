Title: Parallel and Distributed Computing Day 2

## Introduction
- The plan for the day is to understand and run multi-threaded programs.
- Modern computers are becoming more powerful and can execute more operations at the same time.
- Throughput is the number of operations a computer can do in a fixed amount of time.
- The goal is to achieve a k-fold increase in throughput by executing different threads on different parts of the processor.

## Multi-threading
- A program is a sequence of operations to be performed.
- Multi-threading is about partitioning a program into pieces that are logically independent of one another.
- A thread is a subprogram or a part of the program that runs independently of other threads.
- The goal is to achieve a k-fold increase in throughput by running threads on different parts of the processor in parallel.

## Challenges
- The main challenge is partition program logic into threads and synchronize access to shared resources such as memory.
- We must ensure that our multi-threaded program is correct for every choice that the operating system could make about how these threads should be executed.

## How to Write Multi-threaded Programs in Java
- Define what an individual thread should do by creating an object that implements the Runnable interface in Java.
- The Runnable interface has a method called 'void run' which defines what the thread should do.
- The next step is to create threads using the Thread class in Java.
- Finally, call the 'start' method to begin execution of the thread.

Note: The text was edited slightly for grammar and coherence.Introduction to Multi-Threaded Programming in Java

Defining a Runnable Object and Creating Threads 
- To create a multi-threaded program, you first need to define a distinct set of operations that you want to perform and create a different class for each task you want to do. 
- The thread takes a Runnable object as an argument so that Java knows that it's creating a multi-threaded program. 
- After creating a Runnable object, pass it into the thread constructor and start the thread. 
- To wait for threads to finish in a multi-threaded program, use the join method.

Counter Example 
- The example provided in the class is a Java program that creates multiple threads to increment a counter. 
- The program creates a Counter Thread that increments the counter a fixed number of times. 
- A counter object stores all the increments and is accessed by all the threads. 
- The main method initializes threads, creates an array of thread objects, starts the threads, and waits for them to complete. 

Running the Program 
- Students are instructed to download the file from the teacher’s website and run the program. 
- Students run the program with different number of threads and record the actual and expected final count of the increments. 
- It is observed that when the number of threads increases, the actual count of the increments changes even though the number of times it’s incremented is fixed. 
- The running times do not scale linearly when the number of threads increase due to overhead of thread creation. 

Conclusion 
- Computer architecture is a black box, and multi-threaded programming requires trial and error to achieve the desired results. 
- The main issue with the Counter Example was that all threads were using the same Counter object, resulting in different observed actual count values.Understanding Computer Architecture and its Role in Program Execution

**Introduction**
- Purpose is to understand why we see certain behavior in programs
- Modern computers use variations of Von Neumann architecture
- Two main components: CPU and memory
- CPU does logic/arithmetic while all data is stored in memory
- Limited interaction between CPU and memory

**Random Access Machine Model**
- CPU, registers and memory are present
- Instructions involve copying values to and from memory and registers
- Increment operation requires reading, incrementing and writing back to memory 

**Code Example**
- One line of code performs three actions: read, increment, write
- When two threads try to read/write to the same location in memory simultaneously, the explicit ordering of these operations determines the outcome
- Understanding the fine grained interaction between CPU and memory is key to understanding program behavior during execution