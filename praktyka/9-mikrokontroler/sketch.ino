// Демо Д6. Відчути → вирішити → діяти: нічник
// Схема: 5V → фоторезистор → A0 → резистор 10 кОм → GND   (дільник напруги)
//        пін 9 (~) → 220 Ом → світлодіод → GND
// Більше світла → менший опір фоторезистора → більше n

const int SENSOR = A0;
const int LED = 9;

const bool PROPORTSIYNO = true; // false — поріг (релейно), true — плавно (як П-регулятор)
const int PORIH = 514;           // для релейного режиму

// калібрування: що показує n у Serial Monitor при найтемнішому і найсвітлішому
const int NMIN = 54;              // замінити своїми числами
const int NMAX = 974;

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int n = analogRead(SENSOR);                        // 1. відчути (АЦП)

  int pwm;                                           // 2. вирішити
  if (PROPORTSIYNO) {
    pwm = map(n, NMIN, NMAX, 255, 0);                // темніше → яскравіше
    pwm = constrain(pwm, 0, 255);
  } else {
    pwm = (n < PORIH) ? 255 : 0;
  }

  analogWrite(LED, pwm);                             // 3. діяти (ШІМ)

  Serial.print("n = ");
  Serial.print(n);
  Serial.print("   pwm = ");
  Serial.println(pwm);

  delay(100);                                        // крок до наступного «кадру»
}