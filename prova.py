import os
from time import sleep 
q1 = {
    "v_questão":"10", "gabarito":"c", "enunciado":"Sejam x1, x2 e x3 raízes da equação x3 − ax − 16 = 0. Sendo a um número real, o valor de x1³ + x2³ + x3³ é igual a:",
    "a1":"32 - a", "a2":"48 - 2a", "a3":"48", "a4":"48 + 2a"}
q2 = {
    "v_questão":"10", "gabarito":"b", "enunciado":"Um hexágono regular está inscrito em um círculo de raio R. São sorteados 3 vértices distintos do hexágono, a saber: A, B e C. Seja r o raio do círculo inscrito ao triângulo ABC. Qual a probabilidade de que r = R/2 ?",
    "a1":"0", "a2":"1/10", "a3":"3/5", "a4":"1/20"}
q3 = {
    "v_questão":"10", "gabarito":"a", "enunciado":"Seja um triângulo ABC com lados a, b e c opostos aos ângulos A, B e C, respectivamente. Os lados a, b e c formam uma progressão aritmética nesta ordem. Determine a relação correta entre as funções trigonométricas dos ângulos dos vértices desse triângulo.",
    "a1":"2sen(A + C) = sen(A) + sen(C)", "a2":"2cos(A + C) = cos(A) + cos(C)", "a3":"2sen(A - C) = sen(A) - sen(C)", "a4":"2cos(A - C) = cos(A) - cos(C)"}
q4 = {
    "v_questão":"20", "gabarito":"d", "enunciado":"Escolha a alternativa que apresenta as substâncias relacionadas em ordem crescente de solubilidade em água, a 25 ºC e 1 atm: ", "a1":"Bromo < dissulfeto de carbono < butanol < etanol < brometo de potássio.",
    "a2":"Metano < neopentano < dietilcetona < t-butanol < n-butanol.", "a3":"Hidróxido de alumínio < carbonato de cálcio < carbonato de magnésio < nitrato de prata < sulfato de bário.", "a4":"Isobutano < p-diclorobenzeno < o-diclorobenzeno < o-nitrofenol < p-nitrofenol"}
q5 = {
    "v_questão":"5", "gabarito":"b", "enunciado":"Assinale a alternativa correta: ", "a1":"A estrutura primária de uma proteína é definida pela ordem em que os aminoácidos adenina, timina, citosina e guanina se ligam entre si.", "a2":"A estrutura secundária de uma proteína é definida por conformações locais de sua cadeia principal que assumem padrões específicos, tais como hélices α e folhas β.", 
    "a3":"A estrutura terciária de uma proteína é definida pelo modo conforme duas ou mais cadeias polipeptídicas se agregam entre si.", "a4":"As enzimas são proteínas que atuam como catalisadores biológicos e que se caracterizam pela sua capacidade de reagir, simultaneamente, com milhares de substratos de grande diversidade estrutural."}
n=0
prova = []
gab=['c','b','a','d','b']
marcadores=[]
prova.append(q1)
prova.append(q2)
prova.append(q3)
prova.append(q4)
prova.append(q5)

for i,q in enumerate(prova):
    os.system("cls")
    print(i+1,")",q["enunciado"])
    print("a)",q["a1"],"\nb)",q["a2"],"\nc)",q["a3"],"\nd)",q["a4"],"\n")
    marcadores.append(input("Digite a letra da resposta escolhida (Apenas letras minúsculas) : "))
    sleep(1)
os.system("cls")
print("----- GABARITO ------")
for i in range(len(prova)):
    if marcadores[i]==gab[i]: 
        print("Questão:",i+1,"correta")
        n=n+int(prova[i]["v_questão"])
    else: print("Questão:",i+1,"incorreta. Alternativa correta:",gab[i],")")

print("---------------------\nSua nota foi:",n,"\n")



