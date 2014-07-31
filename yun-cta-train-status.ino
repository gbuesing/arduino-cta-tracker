#include "Arduino.h"
#include "Keypad.h"
#include <LiquidCrystal.h>
#include <Process.h>
#include "constants.h"


LiquidCrystal lcd(A5, A4, A3, A2, A1, A0);

const byte ROWS = 4;
const byte COLS = 3;
char keys[ROWS][COLS] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};
byte rowPins[ROWS] = {KEYPAD_ROW_PINS}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {KEYPAD_COL_PINS}; //connect to the column pinouts of the keypad

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );


void setup(){
  pinMode(LCD_BACKLIGHT_PIN, OUTPUT);
  lcd.begin(16, 2);
  
  digitalWrite(LCD_BACKLIGHT_PIN, HIGH);
  lcd.print(START_MESSAGE);
  
  Bridge.begin();
  
  digitalWrite(LCD_BACKLIGHT_PIN, LOW);
  lcd.clear();
}
  
void loop(){
  char key = keypad.getKey();
  
  if (key){
    digitalWrite(LCD_BACKLIGHT_PIN, HIGH);
    
    String label = getLabel(key);
    lcd.print(label);
    
    String command = getCommand(key);
    runCommandAndPrint(command);
    
    delay(SHOW_RESULTS_DELAY);
    
    digitalWrite(LCD_BACKLIGHT_PIN, LOW);
    lcd.clear();
  }
}

void runCommandAndPrint(String command) {
  Process p;
  p.runShellCommand(command);
  
  lcd.setCursor(0,1);
  
  while (p.available()>0) {
    char c = p.read();
    if (c != '\n') {
      lcd.write(c);
    }
  }
}

String getLabel(char key) {
  switch ( key ) {
    case '1':
      return KEY_1_LABEL;
    case '2':
      return KEY_2_LABEL;
    case '3':
      return KEY_3_LABEL;
    case '4':
      return KEY_4_LABEL;
    case '5':
      return KEY_5_LABEL;
    case '6':
      return KEY_6_LABEL;
    case '7':
      return KEY_7_LABEL;
    case '8':
      return KEY_8_LABEL;
    case '9':
      return KEY_9_LABEL;
    case '*':
      return KEY_STAR_LABEL;
    case '0':
      return KEY_0_LABEL;
    case '#':
      return KEY_POUND_LABEL;
  } 
}

String getCommand(char key) {
  switch ( key ) {
    case '1':
      return KEY_1_COMMAND;
    case '2':
      return KEY_2_COMMAND;
    case '3':
      return KEY_3_COMMAND;
    case '4':
      return KEY_4_COMMAND;
    case '5':
      return KEY_5_COMMAND;
    case '6':
      return KEY_6_COMMAND;
    case '7':
      return KEY_7_COMMAND;
    case '8':
      return KEY_8_COMMAND;
    case '9':
      return KEY_9_COMMAND;
    case '*':
      return KEY_STAR_COMMAND;
    case '0':
      return KEY_0_COMMAND;
    case '#':
      return KEY_POUND_COMMAND;
  } 
}
