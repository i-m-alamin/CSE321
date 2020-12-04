class MyThread1 extends Thread {
    public MyThread1(String name) {
        super(name);
    }

    @Override
    public void run() {
        for (int i = 1; i <= 10; i++) {
            System.out.println("Printing from  the " + getName() + ": " + i);
        }
        try {
            sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        for (int i = 21; i <= 30; i++) {
            System.out.println("Printing from  the " + getName() + ": " + i);
        }
    }
}

class MyThread2 extends Thread {
    public MyThread2(String name) {
        super(name);
    }

    @Override
    public void run() {
        try {
            sleep(800);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        for (int i = 11; i <= 20; i++) {
            System.out.println("Printing from  the " + getName() + ": " + i);
        }
    }
}

public class Task1 {
    public static void main(String[] args) {
        MyThread1 thread1 = new MyThread1("1st thread");
        MyThread2 thread2 = new MyThread2("2nd thread");
        thread1.start();;
        thread2.start();
    }
}
