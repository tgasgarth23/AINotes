Concurrent Objects and Final Project Descriptions

Introduction
- Introducing a new topic of concurrent objects that will take up most of the rest of the semester
- Goal is to implement larger data structures like linked lists, queues, and binary trees that support multithreading
- Defining what it means to be correct in concurrent implementation can be challenging
- Lab 3 is due on Friday, which involves computing Mandelbrot using vector operations
- Students should make sure they have a recent version of Java that supports vector operations
- Final project options involve sorting, computing prime numbers and choosing your own problem to solve using parallelism
- There will be a semi-competitive aspect to the final projects with an anonymized leaderboard of fastest benchmarks
- There will also be weekly quizzes covering conceptual topics

Locks and Concurrent ADTs
- Introduction to lock-based protection for shared objects
- Advantages and disadvantages of using locks
- Challenges in defining correctness with concurrent access to ADTs

Example: Doubly Linked List
- Overview of how to implement a doubly linked list
- Explanation of how to insert a new node in a single threaded implementation
- Example implementation in pseudo code

Final Project Descriptions
- Three options for final projects: sorting, computing prime numbers, and choosing your own problem to solve
- Final projects will involve exhaustive testing and recording of changes and performance improvements
- Semi-competitive aspect to final projects with anonymized leaderboard of fastest benchmarksNotes on Concurrent Insertion in Linked Lists

Overview:
- This text discusses the issue of concurrent insertion in linked lists
- The author provides code examples and diagrams to explain the problem and potential solutions
- The text covers locking the whole list, locking individual nodes, and locking only specific parts of nodes

Locking the Whole List:
- If two threads try to insert concurrently, it can cause issues with the linked list
- Locking the whole list avoids these issues, but it is not a fast solution
- The performance is pointless if the implementation is not correct

Locking Individual Nodes:
- To avoid locking the whole list and improve performance, locking individual nodes can be done
- If the insertions do not interfere with each other on separate nodes, they can be done in parallel
- The node class needs to be changed to support locking

Locking Specific Parts of Nodes:
- If the insertions only modify specific parts of nodes, then locking can be done even more specifically
- If one thread only modifies the previous of a node and the other thread only modifies the next, they can be done in parallel
- This method requires more locks and a heavier node class, but could improve performance depending on the application# Note on Locking in Multithreading

## Introduction
In multithreading, locking is an approach to manage race conditions that occur when multiple threads try to access shared resources simultaneously.

## Locking the Entire Object vs. Locking Individual Components
Locking the entire object is easy to reason about; however, it forces sequential execution, eliminating any value from parallelism. In contrast, locking individual parts enables parallelism and better performance, but may lead to blocking execution, where individual threads are doing the right thing and locks are well-behaved, but collectively they get stuck since everyone's waiting for someone else.

## Circular Linked List
When dealing with a circular linked list, locking of individual nodes can lead to thread blocking similar to locking individual components. 

## Conclusion
Locking presents a fundamental tension in multithreading between ensuring sequential execution and achieving better performance through parallelism. Careful consideration is necessary in deciding which locking approach to apply for a given program.