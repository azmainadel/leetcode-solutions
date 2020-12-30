class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> results = new ArrayList<>();
        
        int maxCandies = Collections.max(Arrays.stream(candies).boxed().collect(Collectors.toList()));
        
        for(int perKidCandies: candies){
            if(perKidCandies == maxCandies) results.add(true);
            
            else if(perKidCandies + extraCandies >= maxCandies) results.add(true);
            
            else results.add(false);
        }
        
        return results;
    }
}
