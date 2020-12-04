class MyThread extends Thread {
    static volatile int mostDivisorCount = 0;
    static volatile int desiredNumber = 0;
    int startingRange;
    int finishingRange;

    public MyThread(int start, int finish) {
        startingRange = start;
        finishingRange = finish;
    }

    public int divCount(int num) {
        int total = 0;
        for (int i = 1; i * i <= num; i++) {
            if (num % i == 0) {
                if (i * i == num) {
                    total++;
                } else {
                    total += 2;
                }
            }
        }
        return total;
    }

    public int getNumber() {
        return desiredNumber;
    }

    public int getNumberOfDivisors() {
        return mostDivisorCount;
    }

    @Override
    public void run() {
        for (int i = startingRange; i <= finishingRange; i++) {
            int divisionCount = divCount(i);
            if (divisionCount > mostDivisorCount) {
                desiredNumber = i;
                mostDivisorCount = divisionCount;
            }
        }
    }
}

public class Task2 {
    public static void main(String[] args) {
        // --------- Single-threaded -------------
        long startTime = System.currentTimeMillis();
        // declaring and initializing thread
        MyThread singleThread = new MyThread(1, 100000);
        // running thread
        singleThread.start();
        // wait till thread finishes to approach further
        try {
            singleThread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        // print results
        System.out.println("Single-threaded:");
        System.out.println("---------------------------------------");
        System.out.println("result = " + singleThread.getNumber());
        long endTime = System.currentTimeMillis();
        System.out.println("time= " + (endTime - startTime));
        System.out.println();
        // ---------- Multi-threaded -------------
        startTime = System.currentTimeMillis();
        // declaring and initializing 10 threads
        MyThread[] threadArray = new MyThread[10];
        for (int i = 0, j = 1; i < 10; i++, j++) {
            threadArray[i] = new MyThread(j, (j += 9999));
        }
        // running threads
        for (MyThread thread : threadArray) {
            thread.start();
        }
        // waiting for all the threads to finish
        try {
            for (MyThread thread : threadArray) {
                thread.join();
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        // end message
        System.out.println("Multi-threaded:");
        System.out.println("---------------------------------------");
        System.out.println("result = " + threadArray[9].getNumber());
        endTime = System.currentTimeMillis();
        System.out.println("time= " + (endTime - startTime));
    }
}
