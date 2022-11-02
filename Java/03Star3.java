import java.util.Scanner;

/*

사용자에게 입력 받고 그 수만큼 역삼각형 * 만들기

입력
5

출력
*****
 ****
  ***3
   **
    *
*/

class _03Star3 {
    
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int inputValue = scanner.nextInt();

        for (int i = 0; i < inputValue; i++) {
            for(int j = 0; j < i; j++) {
                System.out.print(" ");
            }

            for(int j = 0; j < inputValue - i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
