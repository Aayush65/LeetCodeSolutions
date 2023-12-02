class Solution {
    public int countCharacters(String[] words, String chars) {
        HashMap<Character, Integer> hm = new HashMap<>();
        for(int i = 0 ; i < chars.length() ; i++){
            char c = chars.charAt(i);
            if(hm.containsKey(c)) hm.put(c, hm.get(c) + 1);
            else hm.put(c, 1); 
        }
        
        int ans = 0;
        for(int i = 0 ; i < words.length ; i++){
            
            HashMap<Character,Integer>hm2 = new HashMap<>();
            for(int j = 0 ; j < words[i].length(); j++){
                char c = words[i].charAt(j);
                if(hm2.containsKey(c)) hm2.put(c, hm2.get(c) + 1);
                else hm2.put(c, 1);
            }
            
            Boolean isPartOfAns = true;
            for(int j = 0 ; j < words[i].length(); j++){
                Character c = words[i].charAt(j);
                // check if hm has all chars from hm2 available 
                if(!hm.containsKey(c)) {
                    isPartOfAns = false;
                    break;
                }
                if( hm2.get(c) > hm.get(c) ){
                   isPartOfAns = false;
                   break;
                }
            }
            
            if(isPartOfAns == true) ans = ans + words[i].length();
        }
        return ans;
    }
}