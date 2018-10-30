package double_pointer;

public class Rotate_strING {
    public void rotateString(char[] str, int offset) {
        // write your code here
        /*
        offset=0 => "abcdefg"
        offset=1 => "gabcdef"
        offset=2 => "fgabcde"
        offset=3 => "efgabcd" --- > dcbaefg --> dcbagfe-- efgabcd
         */
        if(str == null || str.length == 0){
            return;
        }
        offset = offset % str.length;
        reverse(str,0, str.length - offset - 1);
        reverse(str, str.length - offset, str.length - 1);
        reverse(str,0, str.length - 1);


    }

    private void reverse(char[] str, int start, int end){
        for(int i = start,j = end; i< j; i++,j--){
            char temp = str[i];
            str[i] = str[j];
            str[j] = temp;
        }
    }
}
