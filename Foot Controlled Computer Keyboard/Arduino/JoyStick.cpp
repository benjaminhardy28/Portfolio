
//global variables needed for JoyStick Class
char enterTogether[4];  //list of chars to contain characters to be entered when user makes use of combine button
int entTogSize = 0; //Tracks the amount of characters the user has added to the enterTogether array
int combineClicked = 0; //the number of times the user clicks the combine button
int alt = 0;  //which alt the user has set the joysticks to
long start;

//Class for each joysticks
class JoyStick
{
public:
 bool isHeld = false;
 int joyNum;
 int zone; //which "zone" the joystick is entered into
 int x;    //the pin number where the arduino receives the analog x coordinate input
 int y;    //the pin number where the arduino receives the analog y coordinate input
 char keys[4][4];  //2D array of chars containing characters that can be entered
  JoyStick(char k[4][4], int joyNum)
 {
   memcpy (keys, k, 4*4*sizeof(char)); //copy chars of characters when object is instantiated
   this->joyNum = joyNum;
 }
 void setXY(int xNew, int yNew)  //sets x and y values
 {
  x = xNew;
  y = yNew;
 }
 bool updateZone()   //checks which zone the joystick was moved to by looking at x and y coordinates
 {
   int xval = analogRead(this->x); //reads x value
   int yval = analogRead(this->y); //reads y value
   //finds zone based on 2-axis analog joystick coordinate system
   int previousZone = zone;
   if(xval > 512 && yval < 512){
     zone = 0;
   }
   else if(xval < 512 && yval < 512){
     zone = 1;
   }
   else if(xval < 512 && yval > 512){
     zone = 2;
   }
   else {
     zone = 3;
   }
   return (previousZone != zone);
 }
 double distanceFromCenter() //checks how far the joystick was moved from the center
 {
  int xValue = analogRead(this->x) - 512;  // Subtract the center point
  int yValue = analogRead(this->y) - 512;
  int squaredDistance = xValue * xValue + yValue * yValue;
  int distance = sqrt(squaredDistance);
  return distance;
 }
  void enter(){
   char toEnter = keys[alt][zone]; //the char to be entered
   if(combineClicked>0 && entTogSize < 5)  //checks if the combine button has been clicked and if less than 4 keys have been put in enterTogether to prevent an index out of bounds error
   {
     if(entTogSize-1 != combineClicked) //checks if the characters are not ready to be entered, meaning they will be added to enterTogether array
     {
       enterTogether[entTogSize] = toEnter;  //adds the character to enterTogether array to save it
       entTogSize++;   //update size keeping track of how many characters are in the enterTogether list
       String stringChar = String(toEnter);
       if(toEnter)
       SerialUSB.println("combC" + stringChar); //sends the computer program the new character pressed
       //delay(300);     //delay to prevent joystick readings from continuously being read and running enter() method
     }
     if(entTogSize-1 == combineClicked){ //checks  to see if characters are now ready to be added
       for(int i=0; i<entTogSize; i++) //iterates through each character in enterTogether
       {
         toEnter = enterTogether[i];   //sets toEnter to character being iterated in EnterTogether
         Keyboard.press(toEnter);      //presses the character
      }
      Keyboard.releaseAll(); //release and unhold each character being held
      SerialUSB.println("comb#0"); //tell computer that the user used combine, setting it back to 0
      combineClicked = 0; //resets to 0
      entTogSize = 0;  //resets to 0
     }                      
   }
   else
   { //if combine button has not been clicked, simply press key selected
     Keyboard.press(toEnter); //press character
     Serial.println(toEnter);
   }
 }
 void unEnter(){
   Serial.println("unenter");
   Keyboard.releaseAll();
 }
 void checkToEnter(){
   if(distanceFromCenter() > 400) //checks if the joystick has been moved past a certain distance of 400, entering a character if so
     {

       if (updateZone()) { //check and update the zone the joystick was moved to 
         Serial.println("the zone changed");
         enter();
         isHeld = true;
         delay(100);
       }
       else if (isHeld == false){
        //delay(100);
        Serial.print("Entering: ");
        enter();
        if(isHeld)
          Serial.println("true");
        else
          Serial.println("false");
         isHeld = true;
       }
     }else{
       if(isHeld == true){
         unEnter();
       }
       isHeld = false;
     }
 }
  void setNewLayout(const char (*newArrayLayout)[4][4]) const {
      memcpy(const_cast<char*>(reinterpret_cast<const char*>(keys)), *newArrayLayout, sizeof(keys));
  }
};