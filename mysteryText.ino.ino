#include <Servo.h>

Servo servoRight;
Servo servoLeft;

void setup() {
  pinMode(13, OUTPUT);
  pinMode(2, OUTPUT);
  servoLeft.attach(13);
  servoRight.attach(12);
}


void loop() {
  /*for(pos = 0; pos <= 180; pos +=1){
    servoLeft.write(pos);
    servoRight.write(-pos);
    delay(15);
  }*/

  servoLeft.write(180);
  servoRight.write(180);
  digitalWrite(13, HIGH);
  digitalWrite(2, HIGH);
  delay(420);
  digitalWrite(13, LOW);
  digitalWrite(2, LOW);
  servoLeft.write(0);
  servoRight.write(0);
  digitalWrite(13, HIGH);
  digitalWrite(2, HIGH);
  delay(200);
  digitalWrite(13, LOW);
  digitalWrite(2, LOW);
  servoLeft.write(180);
  servoRight.write(180);
  digitalWrite(13, HIGH);
  digitalWrite(2, HIGH);
  delay(270);
  digitalWrite(13, LOW);
  digitalWrite(2, LOW);
  servoLeft.write(0);
  servoRight.write(0);
  digitalWrite(13, HIGH);
  digitalWrite(2, HIGH);
  delay(310);
  digitalWrite(13, LOW);
  digitalWrite(2, LOW);
  
}

  /* for(pos = 180; pos>=0; pos-=1) {
    servoLeft.write(-pos);
    servoRight.write(pos);
    delay(15);
  }
 
 /* for(int pos = 180; pos <= 0; pos-=1){
    servoLeft.write(pos);
    servoRight.write(pos);
  }
  */
  /*servoLeft.writeMicroseconds(2000);
  servoRight.writeMicroseconds(-2000);
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);*/
  
 /* digitalWrite(13, HIGH);   
  delay(1000);
  digitalWrite(2, HIGH);   
  delay(500);              
  digitalWrite(13, LOW);
  delay(100);
  digitalWrite(2, LOW);
  delay(100);
  digitalWrite(13, HIGH);
  delay(500);
  digitalWrite(2, HIGH);   
  delay(500);
  digitalWrite(13, LOW);
  delay(100);
  digitalWrite(2, LOW);
  delay(100);
  digitalWrite(13, HIGH);   
  delay(1000);
  digitalWrite(2, HIGH);   
  delay(500);              
  digitalWrite(13, LOW);
  delay(100);
  digitalWrite(2, LOW);
  delay(100);
  digitalWrite(13, HIGH);
  delay(500);
  digitalWrite(2, HIGH);   
  delay(500);
  digitalWrite(13, LOW);
  delay(100);
  digitalWrite(2, LOW);
  delay(100);
  digitalWrite(13, HIGH);   
  delay(1000);
  digitalWrite(2, HIGH);   
  delay(500);              
  digitalWrite(13, LOW);
  delay(100);
  digitalWrite(2, LOW);
  delay(100);
  digitalWrite(13, HIGH);
  delay(500);
  digitalWrite(2, HIGH);   
  delay(500);
  digitalWrite(13, LOW);
  delay(100);
  digitalWrite(2, LOW);
  delay(100);
*/




