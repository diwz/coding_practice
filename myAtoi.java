public class Solution {
	private static final int upperBound = Integer.MAX_VALUE / 10;
    public int myAtoi(String str) {
    	str = str.trim();
    	int i = 0, n = str.length();
    	int sign = 1;
    	if (i < n && str.charAt(i) == '+') {
    		i++;
    	} else if (i < n && str.charAt(i) == '-') {
    		i++;
    		sign = -1;
    	}
    	int num = 0;
    	while (i < n && Character.isDigit(str.charAt(i))) {
    		int digit = Character.getNumericValue(str.charAt(i));
    		if (num > upperBound || num == upperBound && digit >= 8) {
				return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;    			
    		}
    		num = num * 10 + digit;
    		i++;
    	}
    	return sign * num;
    }
}