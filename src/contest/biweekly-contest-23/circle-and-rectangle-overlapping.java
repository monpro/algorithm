class Solution {
    public boolean checkOverlap(int radius, int x_center, int y_center, int x1, int y1, int x2, int y2) {
        int nearestX = getNearestCor(x_center, x1, x2);
        int nearestY = getNearestCor(y_center, y1, y2);
        
        int distX = nearestX - x_center;
        int distY = nearestY - y_center;
        
        return (distX * distX + distY * distY) <= radius * radius;
    }
    
    
    public int getNearestCor(int center, int bottomVal, int topVal){
        
        return Math.max(bottomVal, Math.min(center, topVal));
    }
}