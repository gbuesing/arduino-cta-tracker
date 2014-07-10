#include <Process.h>
#include <LiquidCrystal.h>
#include "constants.h"

LiquidCrystal lcd(LCD_PINS);

boolean lastButton = LOW;
boolean currentButton = LOW;


void setup() {
  pinMode(BUTTON_PIN, INPUT);
  pinMode(LCD_BACKLIGHT_PIN, OUTPUT);
  
  lcd.begin(16,2);
  digitalWrite(LCD_BACKLIGHT_PIN, HIGH);
  lcd.print(START_MESSAGE);
  
  Bridge.begin();
//  Serial.begin(9600);

  digitalWrite(LCD_BACKLIGHT_PIN, LOW);
  lcd.clear();
}

void loop() {
   currentButton = debounce(lastButton);
   
   if (lastButton == LOW && currentButton == HIGH) {
     lcd.clear();
     digitalWrite(LCD_BACKLIGHT_PIN, HIGH);
     lcd.print(CTA_STOP_NAME);
     
     getTrainTimes();
     
     delay(SHOW_RESULTS_DELAY);
     
     digitalWrite(LCD_BACKLIGHT_PIN, LOW);
     lcd.clear();
   }
   
   lastButton = currentButton;
}

boolean debounce(boolean last) {
   boolean current = digitalRead(BUTTON_PIN);
   if (last != current) {
     delay(BUTTON_DEBOUNCE_DELAY);
     current = digitalRead(BUTTON_PIN);
   }
   return current;
}

void getTrainTimes() {
  Process p;
  p.begin("python");
  p.addParameter(SCRIPT_PATH);
  p.addParameter(CTA_API_KEY);
  p.addParameter(CTA_STOP_ID);
  p.addParameter(MINUTES_DELIMETER);
  p.run();
  
  lcd.setCursor(0,1);
  
  while (p.available()>0) {
    char c = p.read();
//    Serial.print(c);
    if (c != '\n') {
      lcd.write(c);
    }
  }

//  Serial.flush();
}
