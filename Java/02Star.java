/*
 * 사용자에게 정수를 입력 받고 그 정수 만큼 피라미트 별 만들기
 * 
 * 입력 
 * 3
 * 
 * 출력 
 * 
 *   *
 *  ***
 * *****
 */

 import java.util.Scanner;

class _02Star {
    public static void main(String args[]) {

        Scanner scanner = new Scanner(System.in);
        int inputValue = scanner.nextInt();

        for (int i = 0; i < inputValue; i++) {
            for (int j = inputValue - i; j > 0; j--) {
                System.out.print(" ");
            }
            for (int j = 0; j < 2 * (i + 1) - 1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
