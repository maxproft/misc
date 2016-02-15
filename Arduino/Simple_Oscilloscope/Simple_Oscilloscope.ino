int ANALOG_IN = 0;
int val;
 void setup() {
    Serial.begin(9600);
}

void loop() {
    int val = analogRead(ANALOG_IN);
    Serial.println(val);
    if (Serial.available() >= 0) { 
        char incomingByte = Serial.read();
        if (incomingByte=='0') { 
           while(1) { } } }}

