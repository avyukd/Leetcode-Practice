class Solution {
public:
    bool isRobotBounded(string instructions) {
        int direction = 0; 
        int xpos = 0; 
        int ypos = 0;
        bool turned = false;  
        for(char c : instructions){
            if(c == 'L'){
                turned = true; 
                direction -= 90;
                if(direction == -180) direction = 180;
                if(direction == -270) direction = 90;
            }else if(c == 'R'){
                turned = true; 
                direction += 90; 
                if(direction == 270) direction = -90;
            }else{
                if(direction == 0) ypos++;
                if(direction == 180) ypos--;
                if(direction == 90) xpos++;
                if(direction == -90) xpos--;
            }
        }
        if( (xpos==0 && ypos==0) || direction!=0 ) return true;
        return false;
    }
};