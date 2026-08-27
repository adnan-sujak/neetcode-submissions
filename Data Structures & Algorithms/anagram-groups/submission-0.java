public class Solution {
   
    public List<List<String>> groupAnagrams(String[] strs) {
       
        // create a HashMap where:
        // key = the sorted version of a word (String generic in this case)
        // value = a list of words that share that sorted key (anagrams)
        
        Map<String, List<String>> res = new HashMap<>();
     
        for (String s : strs) { //loop through the string array
            
            char[] charArray = s.toCharArray(); // s stores the values found in strs, convert it to charArray and store in charArray
            Arrays.sort(charArray); //sort the char array in alphabetical order
            String sortedS = new String(charArray); //store sorted charArray into sortedS
            res.putIfAbsent(sortedS, new ArrayList<>()); //if the map doesnt have this sorted key yet, add it with an empty list
            res.get(sortedS).add(s);

            // ^^ add the ORIGINAL word (not the sorted version) to the list for this key
            // this is how the anagrams get grouped together
        }
        return new ArrayList<>(res.values());
        //return all the grouped anagram lists after the loop
    }
}