This is a silly project to have an arduino trigger a computer over
serial to do some action. Primarily, this was used with a reed switch
on a door, to surprise friends with the Seinfeld theme song when they
walked in for a Festivus party.

i cant find the arduino code, but its something like this:
int analogPin = 5;     // potentiometer wiper (middle terminal) connected to analog pin 3
                       // outside leads to ground and +5V
int val = 0;           // variable to store the value read

void setup()
{
  Serial.begin(9600);              //  setup serial
}

void loop()
{
  val = analogRead(analogPin);     // read the input pin
  //if (val<1022){
  Serial.println(val);             // debug value
  
 // }
}
