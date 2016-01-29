//To set the default rotation direction, type 'dir0:' or 'dir1:'.
//To set the angle (in degrees) type 'rot30.5:' to rotate it by 30.5 degrees (approximately).
//You can enter in negative values to rotate it in the opposite direction.
//If you want to run the motor, type 'go:'.
//The angle is a bit dodgy for <20degrees.

byte stepPin = 9;
byte dirPin = 8;
byte enablePin = 10;
int count=1;
boolean direct=HIGH;

void function(int count, boolean direct)
{
int j; 
// set the enablePin low so that we can now use our stepper driver.
digitalWrite(enablePin, LOW);
delayMicroseconds(10);
// wait a few microseconds for the enable to take effect
// (That isn't in the spec sheet I just added it for sanity.)

// we set the direction pin in an arbitrary direction.
digitalWrite(dirPin, direct);
digitalWrite(stepPin, HIGH);

Serial.println("Motor Running");
delayMicroseconds(500);
Serial.println(count);

for (j=0; j<=count;j++) {
digitalWrite(stepPin, LOW);
delayMicroseconds(5);
digitalWrite(stepPin, HIGH);
delayMicroseconds(50);
}
}

void setup()
{
pinMode(13, OUTPUT);
pinMode(12, OUTPUT);
pinMode(11, OUTPUT);
digitalWrite(13, HIGH);
digitalWrite(12, HIGH);
digitalWrite(11, HIGH);

// We set the enable pin to be an output
pinMode(enablePin, OUTPUT);
// then we set it HIGH so that the board is disabled until we
// get into a known state.
digitalWrite(enablePin, HIGH);
Serial.begin(9600);
Serial.println("Starting stepper exerciser.");
pinMode(stepPin, OUTPUT);
pinMode(dirPin, OUTPUT);
count=1000;
direct=HIGH;
}



void loop() 
{
  String str;
  if (Serial.available()>0)
  {str = Serial.readStringUntil(':');
//    char ch = Serial.read(); //type 'x' to get the stepper motor to run
  //  in += ch;
  }
  if ( !strcmp(str.c_str(),"dir0") ) {direct = LOW;
    Serial.println("Direction is LOW");}
  if ( !strcmp(str.c_str(),"dir1") ) {direct = HIGH;
    Serial.println("Direction is HIGH");}
  if ( !strcmp(str.c_str(),"go") ) {
    for (int j=0;j<=30;j++) {function(count, direct);
  delay(1000);}}
  if (!strcmp(str.substring(0,3).c_str(),"rot") ) { 
    float deg = atof(str.substring(3).c_str());
    Serial.print("Angle in degrees: ");
    Serial.println(deg);
    count = deg *39.54+94.11;  
    if (count<0) { 
      count = -count;
      direct = !direct;}
  }
}
