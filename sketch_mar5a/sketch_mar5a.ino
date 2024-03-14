String state;

int led_pin = 11;
void setup() {
  pinMode(led_pin, OUTPUT);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    state = Serial.readStringUntil('\n');
    if(state == "on"){
      digitalWrite(led_pin, HIGH);
      Serial.write("On");
    }
    else if(state == "off"){
      digitalWrite(led_pin, LOW);
      Serial.write("Off");
    }
  }
}