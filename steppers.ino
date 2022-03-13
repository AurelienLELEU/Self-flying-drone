#include <AccelStepper.h>
const int stepsPerRevolution = 2048;
AccelStepper verStepper(AccelStepper::FULL4WIRE, 2, 4, 3, 5);
AccelStepper horStepper(AccelStepper::FULL4WIRE, 8, 10, 9, 11);

String hor;
String ver;
String hors;
String vers;

void setup() {
  horStepper.setMaxSpeed(150.0);
  verStepper.setMaxSpeed(100.0);
  horStepper.setAcceleration(5000.0);
  verStepper.setAcceleration(5000.0);
  horStepper.moveTo(100);
  verStepper.moveTo(100);
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void loop() {
  horizontal();
  vertical();
  hors = Serial.readStringUntil('x');
  vers = Serial.readStringUntil('y');
  if ((hors == "+") || (hors == "-") || (hors == "=")){hor = hors;ver = vers;}
}

void horizontal(){
  if (hor == "+"){
    horStepper.moveTo(horStepper.currentPosition()+25);
    horStepper.run();
  }
  if (hor == "-"){
    horStepper.moveTo(horStepper.currentPosition()-25);
    horStepper.run();
  }
}

void vertical(){
  if (ver == "+"){
    verStepper.moveTo(verStepper.currentPosition()+25);
    verStepper.run();
  }
  if (ver == "-"){
    verStepper.moveTo(verStepper.currentPosition()-25);
    verStepper.run();
  }
}
