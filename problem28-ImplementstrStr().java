class Solution {
    public static int strStr(String haystack, String needle) {
	        
	        
	        if(needle.length() <1){
	            return 0;
	        }
	        
	       else if (haystack.length() >= needle.length()){
	        if(haystack.contains(needle)) {
	           
	        	
	        	return haystack.indexOf(needle);
	        }
	                
	                
	        }
	        
	     return -1;
	    }
    
}
