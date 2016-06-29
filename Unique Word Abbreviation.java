// An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

// a) it                      --> it    (no abbreviation)

//      1
// b) d|o|g                   --> d1g

//               1    1  1
//      1---5----0----5--8
// c) i|nternationalizatio|n  --> i18n

//               1
//      1---5----0
// d) l|ocalizatio|n          --> l10n
// Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

// Example:
// Given dictionary = [ "deer", "door", "cake", "card" ]

// isUnique("dear") -> false
// isUnique("cart") -> true
// isUnique("cane") -> false
// isUnique("make") -> true
public class ValidWordAbbr {

    private HashMap<String, String> map = new HashMap<String, String>();
    public ValidWordAbbr(String[] dictionary) {
        for(String str : dictionary){
            String abbr = abbreviateWord(str);
            if(map.containsKey(abbr)){
                if(!map.get(abbr).equals(str)){
                    map.put(abbr, "");
                }
            } else {
                map.put(abbr, str);
            }
        }
    }

    private String abbreviateWord(String str) {
        int len = str.length();
        if(len <= 2){
            return str;
        }
        return str.charAt(0) + String.valueOf(len - 2) + str.charAt(len-1);
    }
    public boolean isUnique(String word) {
        String abbr = abbreviateWord(word);
        return !map.containsKey(abbr) || map.get(abbr).equals(word);
    }
}


// Your ValidWordAbbr object will be instantiated and called as such:
// ValidWordAbbr vwa = new ValidWordAbbr(dictionary);
// vwa.isUnique("Word");
// vwa.isUnique("anotherWord");
