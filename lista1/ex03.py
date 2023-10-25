"""3. Ler uma temperatura em graus Celsius e apresentá-la convertida em graus
Fahrenheit. A fórmula de conversão é: F=(9*C+160) / 5, sendo F a temperatura em
Fahrenheit e C a temperatura em Celsius.
"""

c = float(input('Digite a temperatura em graus Celsius: '))

f = (9*c+160)/5

print(f'A temperatura de {c}⁰C (Celsius) é equivalente a {f}⁰F (Fahrenheit)')