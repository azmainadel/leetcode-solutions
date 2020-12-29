class Solution {
    fun maximumWealth(accounts: Array<IntArray>): Int {
        var maxWealth: Int = 0;
        
        for(account in accounts){
            var accountWealth: Int = account.sum();
            
            if(accountWealth > maxWealth){
                maxWealth = accountWealth;
            }
        }
        
        return maxWealth;
    }
}
