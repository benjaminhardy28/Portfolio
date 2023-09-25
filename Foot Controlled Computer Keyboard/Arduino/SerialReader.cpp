//class to read information from the serial port from the python program
//This is used for when the program sends custom config layouts

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
                String jsonString = SerialUSB.readStringUntil('\n');
                SerialUSB.println(jsonString);
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


