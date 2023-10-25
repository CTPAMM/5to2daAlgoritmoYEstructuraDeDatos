#include <Servo.h>

#define SER 5 // Pin para el servo

Servo servo; // Objeto servo

int mensaje; // Variable para guardar el mensaje recibido por serial


void setup()
{
   // Inicializamos el servo y el Serial:

   servo.attach(SER);

   Serial.begin(9600);
}


void loop()
{
   if (Serial.available() > 0)
   {
      mensaje = Serial.parseInt(); // Leemos el serial

      servo.write(mensaje); // Movemos el servo

      delay(50);
   }
}