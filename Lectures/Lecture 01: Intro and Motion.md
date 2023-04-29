Overview of Computer Power, Throughput, and Parallelism

In this class, the instructor talks about computer power, throughput, and parallelism. They start the class by checking if everything is working after a software update. Then, they talk about the course structure, policies, and show some motivational pictures. The instructor asks the class how to quantify the computational power of a computer and how much more powerful computers are now compared to the past. They discuss various ways to measure power, such as CPU memory, computation speed, and benchmarking.

The instructor compares their old laptop from 2002 with their current MacBook Pro and explains that although the clock speed of the new laptop is less, it is faster in practical terms due to having four cores. They explain that the reason for constraints in computer speed is largely physical and that the speed of light and communication between different parts of the computer can limit a computer's performance.

The class then shifts focus from speed to throughput, which is the number of useful operations a computer can perform in a single second. They explain that by maximizing throughput, we can get programs to perform hundreds or thousands of times more useful operations per second than a simple sequence of operations.

Finally, the instructor introduces the concept of parallelism, which is the ability to perform multiple operations simultaneously, and gives examples of bit-level, instruction-level, data-level, and task-level parallelism. The rest of the course will be about maximizing the throughput of a computer through parallelism.Parallelism in Computer Science

Introduction to Parallelism in Computer Science

- Parallelism is an essential component of modern computing, allowing us to perform operations more efficiently and quickly.
- In this class, we will explore different methods of parallelism and how they work to increase computational power.

Binary Addition and Elementary School Arithmetic

- Binary addition is a fundamental operation used in computer science.
- Sequential addition of individual bits can be wasteful because it requires waiting for the previous sum to be calculated before moving on to the next.
- Computers use parallelism at the gate level to perform arithmetic operations more efficiently.

Types of Parallelism

- Three types of parallelism include SIMD parallelism, multi-core parallelism, and larger-scale parallelism such as computing clusters and server farms.
- These methods allow for greater throughput and the ability to run multiple operations at once.

Promise of Parallelism

- Parallelism allows for more operations to be performed per second and can lead to a significant speedup in certain programs.
- Careful optimization can result in huge performance gains.

Challenges of Parallelism

- Dependencies between operations can limit the effectiveness of parallelism.
- Processors must share resources, leading to communication and synchronization costs.
- Non-determinism can make it difficult to ensure that programs will run correctly under different execution scenarios.# Parallel Computing Course Overview

## Introduction
- Understanding program's intended purpose in parallel programming is challenging
- Effort in this course is to understand conditions for guaranteed program execution
- In modern computing, multiple components interact to function together

## Course 
- Exploiting parallelism to write performant code
- Reasoning about parallel programs executions
- Multithreaded programming, mutual exclusion, current object's locks, contention resolution, synchronization in current data structures, and the SIM D /vector operations are main topics
- Focus is to make programs that have provable guarantees for their behavior before performance
- Emphasis on understanding fundamental problems rather than writing the fewest lines of code
- Three lectures a week with coding assignments, written assignments, occasional quizzes, in class activities, and a final project focused on employing parallelism for efficient results

## Coursework logistics 
- Regular attendance and class activities are required
- Recorded lectures will be posted to ensure students can keep up with the classwork 
- Assignment of illness or fever is not recommended to attend the physical class
- Optional masks are allowed, but office hours require masks to be worn
- Coursework includes coding assignments, written assignments, occasional quizzes, in class activities, and a final project

## Course Focus
- Understanding computing independent of technology  
- Fundamental concepts that will not change in parallelism 

## Week 1 
- Introduction to multi-threaded programming in Java
- Subtleties of multithreading should be studies
- Reading should be done in preparation of Wednesday's class.