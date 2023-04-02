import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;
import java.util.Scanner;
public class GenerateInputMatrix {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        int h = sc.nextInt();
        // int k = sc.nextInt();

        int[][] matrix = generateMatrix(m, n, h);

        FileWriter fileWriter = new FileWriter("input.txt");
        fileWriter.write(m + " " + n + " " + h + "\n");
        // fileWriter.write(m + " " + n + " " + h + " " + k + "\n");
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    fileWriter.write(matrix[i][j] + " ");
                }
                fileWriter.write("\n");
            }
            fileWriter.close();
        }

        private static int[][] generateMatrix(int m, int n, int h) {
            int[][] matrix = new int[m][n];
            Random rand = new Random();
            // Set values greater than or less than h randomly
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    int value = rand.nextInt(100);
                    if (value < 50) {
                        matrix[i][j] = rand.nextInt(h + 1); // set value less than or equal to h
                    } else {
                        matrix[i][j] = rand.nextInt(100 - h) + h + 1; // set value greater than h
                    }
                }
            }
            return matrix;
        }
}
