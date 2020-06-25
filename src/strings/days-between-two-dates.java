package strings;

class Solution {
    
    public int daysSinceBeginning(String date){
        int[] monthToDays = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int result = 0;
        
        String[] dates = date.split("-");
        
        int year = Integer.parseInt(dates[0]);
        int month = Integer.parseInt(dates[1]);
        int days = Integer.parseInt(dates[2]);
        
        for(int i = 1971; i < year; i++){
            result += isLeapYear(i) ? 366: 365; 
        }
        
        for(int i = 1; i < month; i++){
            if(isLeapYear(year) && i == 2){
                result += 29;
            }
            else{
                result += monthToDays[i];
            }
        }
        
        return result + days;
        
        
    }
    
    public int daysBetweenDates(String date1, String date2) {
        return Math.abs(daysSinceBeginning(date1) - daysSinceBeginning(date2));
    }
    
    
    public boolean isLeapYear(int year){
        return (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
    }
}