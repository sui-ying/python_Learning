## 4. part4 多进程和多线程


### 4.2 多线程

多线程：
- 多线程是Python程序中实现多任务的一种方式
- 线程是程序执行的最小单位
- 同属一个进程的多个线程共享进程所拥有的全部资源

[线程创建实例](./part4_process_thread/demo_multithread.py)， 和多进程创建类似

类似地，主线程会等待子线程执行完成才结束; 如果主线程结束时不想等待子线程结束，可以[将子线程设置为守护主线程](./part4_process_thread/demo_multithread_daemon.py)

[线程执行的顺序是无序的，通过CPU调度完成](./part4_process_thread/demo_multithread_order.py)


### 4.3 进程和线程对比

- 线程是依附在进程里面的，没有进程就没有线程；一个进程默认提供一条线程，进程可以创建多个线程
- 进程创建的资源开销比创建线程的资源开销大；进程是操作系统资源分配的基本单位，线程是CPU调度的基本单位；线程不能独立执行，必须依附在进程中
- 进程可以用多核，但是资源开销大；线程资源开销小，但是不能使用多核

