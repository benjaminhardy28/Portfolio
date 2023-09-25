//Creator: Benjamin Hardy
//include needed files
#include <Keyboard.h>
#include <math.h>
#include <Mouse.h>
#include <ArduinoJson.h>
#include <JoyStick.h>
#include <SerialReader.h>



//char containing binary value for certain characters
char KEY_SPACE = 32;
char test = 180;
//2D arrays holding characters to be given to JoyStick objects
char arr3[4][4] = {{'w', 'a', 's', 'd'}, {'q', 'e', 'r', 't'}, {'y', 'u', 'i', 'o'}, {'p', 'f', 'g', 'h'}};
char arr4[4][4] = {{'e', KEY_LEFT_SHIFT, KEY_LEFT_CTRL, KEY_DELETE}, {'j', 'k', 'l', 'z'}, {'x', 'c', 'v', 'b'}, {'n', 'm', KEY_ESC, KEY_CAPS_LOCK}};
char arr2[4][4] = {{KEY_UP_ARROW, KEY_LEFT_ARROW, KEY_DOWN_ARROW, KEY_LEFT_ARROW},{KEY_F1, KEY_F2, KEY_F3, KEY_F4}, {KEY_F5, KEY_F6, KEY_F7, KEY_F8}, {KEY_F9, KEY_F10, KEY_F11, KEY_F12}};
char arr1[4][4] = {{'1', '2', '3', '4'}, {'5', '6', '7', '8'}, {KEY_LEFT_ALT, KEY_TAB, KEY_INSERT, KEY_BACKSPACE}, {KEY_KP_ASTERISK, KEY_RETURN, KEY_HOME, KEY_END}};
//Declare and instantiate JoyStick objects, passing 2D arrays of chars as explicit parameters
JoyStick joy1 (arr4, 1);
JoyStick joy2 (arr3, 2);
JoyStick joy3 (arr2, 3); 
JoyStick joy4 (arr1, 4);
SerialReader reader(joy1, joy2, joy3, joy4);

//variable holding the pin number for each button
int alt1 = 5;
int alt2 = 4;
int alt3 = 6;
int alt4 = 2;
int spaceButton = 10;
int comb = 7;

void setup() {

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

