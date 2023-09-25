//Creator: Benjamin Hardy
//include needed files
#include <Keyboard.h>
#include <math.h>
#include <Mouse.h>
#include <ArduinoJson.h>

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
      //Serial.println("time");
     // Serial.println(micros() - start);
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


//global variables


//char containing binary value for certain characters
char KEY_SPACE = 32;
char test = 180;
//2D arrays holding characters to be given to JoyStick objects
char arr3[4][4] = {{'w', 'a', 's', 'd'}, {'q', 'e', 'r', 't'}, {'y', 'u', 'i', 'o'}, {'p', 'f', 'g', 'h'}};
char arr4[4][4] = {{'e', KEY_LEFT_SHIFT, KEY_LEFT_CTRL, KEY_DELETE}, {'j', 'k', 'l', 'z'}, {'x', 'c', 'v', 'b'}, {'n', 'm', KEY_ESC, KEY_CAPS_LOCK}};
char arr2[4][4] = {{KEY_UP_ARROW, KEY_LEFT_ARROW, KEY_DOWN_ARROW, KEY_LEFT_ARROW},{KEY_F1, KEY_F2, KEY_F3, KEY_F4}, {KEY_F5, KEY_F6, KEY_F7, KEY_F8}, {KEY_F9, KEY_F10, KEY_F11, KEY_F12}};
char arr1[4][4] = {{'1', '2', '3', '4'}, {'5', '6', '7', '8'}, {KEY_LEFT_ALT, KEY_TAB, KEY_INSERT, KEY_BACKSPACE}, {KEY_KP_ASTERISK, KEY_RETURN, KEY_HOME, KEY_END}};
//{KEY_LEFT_ALT, KEY_TAB, KEY_INSERT, KEY_BACKSPACE}
//KEY_KP_PLUS, KEY_KP_MINUS KEY_KP_SLASH
//Declare and instantiate JoyStick objects, passing 2D arrays of chars as explicit parameters
JoyStick joy1 (arr4, 1);
JoyStick joy2 (arr3, 2);
JoyStick joy3 (arr2, 3); 
JoyStick joy4 (arr1, 4);

class SerialReader
{
  public:
    const JoyStick* allJoySticks[4];  // Array of pointers to JoyStick objects

    SerialReader(const JoyStick& j1, const JoyStick& j2, const JoyStick& j3, const JoyStick& j4){
        allJoySticks[0] = &j1;
        allJoySticks[1] = &j2;
        allJoySticks[2] = &j3;
        allJoySticks[3] = &j4;
    }

    void checkIfMessage(){
          if (SerialUSB.available()) {
            for(const auto& joyStick : allJoySticks) {


                SerialUSB.println("message detected");
                //String jsonString = SerialUSB.readString();
                String jsonString = SerialUSB.readStringUntil('\n');
                SerialUSB.println(jsonString);
                //String jsonString = sentMessage;
                //const char* jsonCharArray = jsonString.c_str();
                //const char* jsonString = "[[\"a\", \"a\", \"a\", \"a\"], [\"a\", \"a\", \"a\", \"a\"], [\"a\", \"a\", \"a\", \"a\"], [\"a\", \"a\", \"a\", \"a\"]]";
                //String jsonString = "[[\"a\", \"a\", \"a\", \"a\"], [\"a\", \"a\", \"a\", \"a\"], [\"a\", \"a\", \"a\", \"a\"], [\"a\", \"a\", \"a\", \"a\"]]";
                char myArray[4][4];

                DynamicJsonDocument doc(1024);
                DeserializationError error = deserializeJson(doc, jsonString);

                if (error) {
                  SerialUSB.print("JSON parsing failed! Error code: ");
                  SerialUSB.println(error.c_str());
                  return;
                }

                JsonArray array = doc.as<JsonArray>();

                // Extract data into 2D array
                for (int i = 0; i < 4; i++) {
                  JsonArray subArray = array[i];
                  for (int j = 0; j < 4; j++) {
                    if(subArray[j].as<String>().length() > 1){
                      int intValue = subArray[j].as<String>().toInt();
                      myArray[i][j] = static_cast<char>(intValue);
                    }
                    else{
                      myArray[i][j] = subArray[j].as<String>().charAt(0);
                    }
                  }
                }
                SerialUSB.println("array from program at arduino");
                // Print the extracted array
                for (int i = 0; i < 4; i++) {
                  for (int j = 0; j < 4; j++) {
                    SerialUSB.print(myArray[i][j]);
                    SerialUSB.print(" ");
                  }
                  SerialUSB.println();
                }
              joyStick -> setNewLayout(&myArray);
              SerialUSB.println("after the method - arduino");
            }
      }
       // }
    }
};

SerialReader reader(joy1, joy2, joy3, joy4);


//variable holding the pin number for each button
int alt1 = 5;
int alt2 = 4;
int alt3 = 6;
int alt4 = 2;
int spaceButton = 10;
int comb = 7;
//int times = 2;


void setup() {

  // Other code here
  delay(1000);
 //set each JoyStick object to have x and y variables with pin numbers
 joy1.setXY(A0, A1);
 joy2.setXY(A2, A3);
 joy3.setXY(A4, A5);
 joy4.setXY(A6, A7);
 //set pins to be receiving input
 pinMode(alt1, INPUT);
 pinMode(alt2, INPUT);
 pinMode(alt3, INPUT);
 pinMode(alt4, INPUT);
 pinMode(spaceButton, INPUT);
 pinMode(comb, INPUT);
 //Serial.begin(115200);
 Serial.begin(9600);
 SerialUSB.begin(200000);    // Initialize Native USB port
 Keyboard.begin(); // starts emulating a keyboard connection to the computer
 Mouse.begin();
}


void loop() {
 if(digitalRead(alt1) == HIGH) //checks if first button alt is clicked
 {
  //  reader.checkIfMessage();
   alt = 0;
   SerialUSB.println("alt_#1");
   delay(300);
 }
 if(digitalRead(alt2) == HIGH) //checks if second button alt is clicked
 {
   alt = 1;
   SerialUSB.println("alt_#2");
   delay(300);
 }
 if(digitalRead(alt3) == HIGH) //checks if third button alt is clicked
 {
   alt = 2;
   SerialUSB.println("alt_#3");
   delay(300);
 }
 if(digitalRead(alt4) == HIGH) //checks if fourth button alt is clicked
 {
   alt = 3;
   SerialUSB.println("alt_#4");
   delay(300);
 }
 if(digitalRead(comb) == HIGH) //checks if combine button  is clicked
 {
   combineClicked++; //update number of times combined has been clicked
   SerialUSB.println("comb#1"); //tells the computer to update the gui displaying how many times the user has pressed combine
   delay(300); //delay to prevent updating combineClicked too many times
 }

 joy1.checkToEnter();
 joy2.checkToEnter();
 joy3.checkToEnter();
 joy4.checkToEnter(); 
 reader.checkIfMessage();
}

