//Variables
int potpin = 1; //Potentiometer pin (analog)
int val = 0; //to store the Potentiometer value
int randNumber1 = 0; //to store the random number
int randNumber2 = 0; //to store the random number

void setup()
{
  //set LED pins to output
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
}

void loop()
{
  randNumber1 = random(2, 12); //random number between 2 and 11
  randNumber2 = random(2, 12);
  val = analogRead(potpin); //read the Potentiometer value and store it
  
  if (val <= 900) //if the potentiometer is not turned all the way down, start lightshow
  {
    analogWrite(randNumber1, 255); //turn one of the LEDs on
    analogWrite(randNumber2, 255); //turn one of the LEDs on
    delay(val); //wait
    analogWrite(randNumber1, 0); //turn that same LED off
    analogWrite(randNumber2, 0); //turn that same LED off
    delay(val); //wait
  }
  else //if the potentiometer is all the way down, turn off all LEDs
  {
    for (int i=2; i < 12; i++){
      analogWrite(i, 0);
   } 
  }
} 
