#include <SPI.h>
#include <LoRa.h>

#define ss 15
#define rst 16
#define dio0 2
int counter = 0;

void setup() 
{
  Serial.begin(115200);
  LoRa.setPins(ss, rst, dio0);
    if (!LoRa.begin(433E6)) {
    Serial.println("Starting LoRa failed!");
    delay(100);
    while (1);
  }
}

void loop() 
{
  Serial.print("Sending packet: ");
  Serial.println(counter);

  // send packet
  LoRa.beginPacket();
  LoRa.print(F("Pkt No:"));
  LoRa.println(counter);
  LoRa.endPacket();

  counter++;
  delay(3000);
}
