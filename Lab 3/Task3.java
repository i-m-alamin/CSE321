import java.util.Random;

class SortingThread extends Thread {

    public int[] arr;
    public int[] newArr;

    public SortingThread(int[] arr) {
        this.arr = arr;
    }

    public int[] mergeSort(int[] givenArray) {
        int arrayLength = givenArray.length;
        if (arrayLength == 1)
            return givenArray;
        int[] first = new int[arrayLength / 2];
        int[] second = new int[arrayLength - arrayLength / 2];
        for (int i = 0; i < first.length; i++) {
            first[i] = givenArray[i];
        }
        // int c = 0;
        for (int i = 0; i < second.length; i++) {
            second[i] = givenArray[i + first.length];
            // c++;
        }
        first = mergeSort(first);
        second = mergeSort(second);
        return merge(first, second);
    }

    public int[] merge(int[] a, int[] b) {
        int[] c = new int[a.length + b.length];
        int ap = 0, bp = 0;
        int i;
        for (i = 0; i < c.length; i++) {
            if (ap == a.length) {
                for (int j = i; j < c.length; j++) {
                    c[j] = b[bp];
                    bp++;
                }
                break;
            } else if (bp == b.length) {
                for (int j = i; j < c.length; j++) {
                    c[j] = a[ap];
                    ap++;
                }
                break;

            } else if (a[ap] < b[bp]) {
                c[i] = a[ap];
                ap++;
            } else {
                c[i] = b[bp];
                bp++;
            }
        }
        return c;
    }

    public int[] getArray() {
        return newArr;
    }

    @Override
    public void run() {
        newArr = mergeSort(arr);
    }
}

public class Task3 {
    public static int[] merge(int[] a, int[] b) {
        int[] c = new int[a.length + b.length];
        int ap = 0, bp = 0;
        int i;
        for (i = 0; i < c.length; i++) {
            if (ap == a.length) {
                for (int j = i; j < c.length; j++) {
                    c[j] = b[bp];
                    bp++;
                }
                break;
            } else if (bp == b.length) {
                for (int j = i; j < c.length; j++) {
                    c[j] = a[ap];
                    ap++;
                }
                break;

            } else if (a[ap] < b[bp]) {
                c[i] = a[ap];
                ap++;
            } else {
                c[i] = b[bp];
                bp++;
            }
        }
        return c;
    }

    public static void main(String[] args) {
        // int[] randomArray =
        // {3,7,23,563,231,352,124,57,345,873,223,121,46,564,23,12,52,123,45,2,83,21,8,1,44,
        // 10000000};
        // int[] newArray = mergeSort(randomArray);
        // creating random array of and 2 subarrays
        Random rand = new Random();
        int[] randomArray = new int[20];
        for (int i = 0; i < randomArray.length; i++) {
            randomArray[i] = rand.nextInt(10000);
        }
        int[] subArray = new int[randomArray.length / 2];
        int[] subArray2 = new int[randomArray.length / 2];
        // copying array parts
        for (int i = 0; i < randomArray.length / 2; i++) {
            subArray[i] = randomArray[i];
        }
        for (int i = randomArray.length / 2; i < randomArray.length; i++) {
            subArray2[i - randomArray.length / 2] = randomArray[i];
        }
        // creating and running threads
        SortingThread thread1 = new SortingThread(subArray);
        SortingThread thread2 = new SortingThread(subArray2);
        thread1.start();
        thread2.start();
        try {
            thread1.join();
            thread2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        // finally merging
        int[] sortedArray = merge(thread1.getArray(), thread2.getArray());

        for (int x : sortedArray)
            System.out.println(x);

    }
}
