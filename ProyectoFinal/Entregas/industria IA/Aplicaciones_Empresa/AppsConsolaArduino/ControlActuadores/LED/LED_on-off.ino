/*String mensaje // Variable para guardar el mensaje recibido por serial*/

void setup()
{
  // Inicializamos el puerto del LED y el Serial:

  pinMode(13, OUTPUT);

  Serial.begin(9600);

  Serial.println("Ingrese 'encender' para encender el LED o 'apagar' para apagarlo ");
}

void loop()
{

  if (Serial.available())
  {
    String mensaje = Serial.readString(); // Leemos el serial

    if (mensaje == "encender")
    {
      digitalWrite(13, HIGH); // Encendemos el LED
    }
    else if (mensaje == "apagar")
    {
      digitalWrite(13, LOW); // Apagamos el LED
    }
  }
}
