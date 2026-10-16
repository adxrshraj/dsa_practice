class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        HashMap<String, List<String>> list = new HashMap<>();

        for (String word : strs){
            //convert strs[i] into char array
            char[] letter = word.toCharArray();
            //sorts the char array
            Arrays.sort(letter);

            //converts the sorted char array into a string
            String key = new String(letter);

            if (!map.containsKey(key)) {
                map.put(key, new ArrayList<>());
            }
            
            map.get(key).add(word);
        }
        List<String> groupAnagrams = new ArrayList<>(map.values());

        return groupAnagrams;
            

        
    }
}
