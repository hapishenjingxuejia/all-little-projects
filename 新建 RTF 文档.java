import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class RandomNumberMultiplier {
    public static void main(String[] args) {
        // 创建一个Random对象
        Random random = new Random();

        // 创建一个列表来存储结果
        List<Integer> resultList = new ArrayList<>();

        // 运行100次并将结果存入列表中
        for (int i = 0; i < 100; i++) {
            // 生成两个1到100之间的随机数
            int number1 = random.nextInt(100) + 1;
            int number2 = random.nextInt(100) + 1;

            // 计算两个随机数的乘积
            int result = number1 * number2;

            // 将结果添加到列表中
            resultList.add(result);
        }

        // 输出列表中的结果
        for (int i = 0; i < resultList.size(); i++) {
            System.out.println("第 " + (i + 1) + " 次的相乘结果：" + resultList.get(i));
        }
    }
}
