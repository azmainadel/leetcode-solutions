class Solution {
    public int myAtoi(String s) {
        int index = 0;
        int sign = 1;
        int total = 0;
        
        // Check for empty string
        if (s.length() == 0) return 0;
        
        // Ignore leading whitespaces
        while (index < s.length() && s.charAt(index) == ' ') index++;
        if (index == s.length()) return 0;
        
        // Set sign if given
        if (s.charAt(index) == '+' || s.charAt(index) == '-') {
            sign = s.charAt(index) == '+' ? 1 : -1;
            index++;
        }
        
        while (index < s.length()) {
            // Get current digit and return if alphabetical character
            int digit = s.charAt(index) - '0';
            if (digit < 0 || digit > 9) break;
            
            // Check for overflow
            if ((Integer.MAX_VALUE - digit) /10 < total){
                return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }
            
            total = total * 10 + digit;
            index++;
        }
        
        return sign * total;
        
    }
}