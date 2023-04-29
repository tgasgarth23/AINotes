Concurrent and Parallel Programming Lecture: Embarrassingly Parallel Computation and Limits of Parallelism

Homework Assignment and Office Hours
- First programming assignment is posted, but not everything is set up with the high-performance computing cluster yet
- Short written assignment due next week with questions related to lecture and readings
- Drop-in office hours with TA, Mary Kay, on Wednesdays from 7-9 PM in the computer lab and individual office hours with the instructor, by appointment, on Thursdays from 1-2:30 PM

Embarrassingly Parallel Computation
- Discussion of the activity from the last lecture about concurrent modification of an array
- Explanation of thread-local variables and shared objects in Java
- Example of incrementing an array with multiple threads and the non-deterministic outcomes that can occur
- Explanation of embarrassingly parallel computation as tasks that can be split into independently runnable parts, eliminating any need for coordination between threads and allowing for significant speedups
- Example of image processing as an embarrassingly parallel task

Limits of Parallelism
- Discussion of the maximum speedup achievable by parallel computation, limited by the amount of non-parallelizable work and communication overhead between threads
- Explanation of Amdahl's law as a way to calculate the maximum speedup possible
- Example of calculating the maximum speedup for a program with a fixed amount of non-parallelizable work

Note: Timestamps are not provided as the text is a transcript of a lecture and does not contain specific timestamps.# Concurrency and Parallelism

This text discusses the concepts of concurrency and parallelism in computer science. These topics are fundamental to operating systems and computer architecture. While parallelism can offer a significant performance boost, concurrency is necessary for many aspects of computer systems. However, nondeterminism can make reasoning about concurrent programs difficult. 

## RAM Model and Shared Memory

The text explains that shared memory is a significant issue with the RAM model, as it can lead to overwriting or uncertainty with the true state of the computer's memory. The interaction between the memory and the CPU is complex, and threads have their own versions of what they read, increment, and write.

## Concurrency vs. Parallelism

The text outlines the differences between concurrency and parallelism. Concurrency refers to multiple programs running at the same time, while parallelism means making progress on multiple tasks precisely at the same time. Parallelism offers a performance boost, while concurrency is essential to computer systems at a basic level. 

## Fixing the Multithreaded Counter

The text presents an issue where the multithreaded counter is not behaving as expected. The solution is to give each thread its own local counter and accumulate the values at the end. However, this easy solution may not always be sufficient to solve concurrency issues.Notes on Multithreading: Embarrassingly parallel problems and the Monte Carlo method

### Efficiency in Multithreading
- Issue of efficiency with k core is, now k counters are needed, using more resources (timestamp: 0:18)
- A counter is an int or a long, but problems may need intermediate counts or ongoing counts (timestamp: 1:55)
- Mutual exclusion problem: fundamental in concurrent programming, deals with locking counters so only one thread modifies it at a time (timestamp: 3:15)

### Embarrassingly Parallel Problems
- Embarrassingly parallel problem: can be broken into many simple computations that can be performed in parallel (timestamp: 4:45)
- Example: counting to 1 billion, partitioning the counts up, and adding the counts together at the end (timestamp: 5:20)
- Monte Carlo method: picking a random process to generate random numbers to estimate a value (timestamp: 7:42)
- The experiment: throwing darts at a square to estimate pi (timestamp: 9:55)
- Embarrassingly parallel: randomly throwing darts, summing up the number of darts, and hits to get a better estimate of pi faster (timestamp: 13:40)

### Next Steps
- Next time: problems that are not embarrassingly parallel and expected performance increase (timestamp: 14:51)