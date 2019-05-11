package String;

import java.util.HashMap;
import java.util.Map;

public class Integer_to_Roman_12 {
    public String intToRoman(int num) {
        String[] M = {"","M","MM","MMM"};
        String[] C = {"","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"};
        String[] X = {"","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"};
        String[] I = {"","I","II","III","IV","V","VI","VII","VIII","IX"};

        return M[num / 1000] + C[(num % 1000) / 100] + X[(num % 100) / 10] + I[num % 10];
    }

    public int romanToInt(String s) {
        int[] dict = new int[s.length()];
        int result = 0;
        for(int i = 0; i < s.length(); i++){
            switch (s.charAt(i)){
                case 'I':
                    dict[i] = 1;
                    break;
                case 'V':
                    dict[i] = 5;
                    break;
                case 'X':
                    dict[i] = 10;
                    break;
                case 'L':
                    dict[i] = 50;
                    break;
                case 'C':
                    dict[i] = 100;
                    break;
                case 'D':
                    dict[i] = 500;
                    break;
                case 'M':
                    dict[i] = 1000;
                    break;
            }
        }
        for(int i = 0; i < s.length() - 1; i++){
            if(dict[i] < dict[i + 1])
                result -= dict[i];
            else
                result += dict[i];
        }
        result += dict[dict.length - 1];
        return result;
    }
}
