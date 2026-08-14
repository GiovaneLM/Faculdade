<?php

// Array simples
$lanches = array("Pastel","Pizza","Hamburguer","HotDog","Xis","Churrasquinho");

// echo $lanches[0];
echo "Hoje pela manhã comi $lanches[0], $lanches[2] e comi $lanches[5]";
echo "<hr>";
print_r($lanches);  

// Vale a partir do php 5.6
$bebidas = array("vodka","fanta uva","suco","Água","Whisky","Café");

echo "<hr>";
print_r($bebidas);
echo "<h1>$bebidas[4]</h1>";

$aluno = [
    "nome" => "Roblox",
    "idade" => 21,
    "curso" =>["ADS","moda"]
];
echo "<hr>";
print_r($aluno);
echo"<h2>$aluno[nome],esta com $aluno[idade] anos. e esta matriculado no curso de " . $aluno['curso'][0] . $aluno['curso'][1] . "</h2>";


$funcionarios = [
    [
        "nome" => "ricardo",
        "setor" => "administrativo",
        "email" => "ricardo@email.com"
    ],
    [
        "nome" => "gustavo",
        "setor" => "financeiro",
        "email" => "gustavo@email.com"
    ],
    [
        "nome" => "ana da silva",
        "setor" => ["marketig","TI"],
        "email" => "ana@email.com"
    ]
];

echo "<pre>";
print_r($funcionarios);
echo "<pre>";

echo $funcionarios[1]['setor'];
echo "<br>";
echo $funcionarios[2]['email'];
echo "<br>";
echo $funcionarios[2]['setor'][0];
echo "<br>";
echo $funcionarios[2]['setor'][1];


//no php usamos o ponto (.) parta concatnar strings
echo "<p> A funcionaria ". $funcionarios[2]['nome'] . " possui o e-mail " . $funcionarios[2]['email'] . " e atua nos setores ". $funcionarios[2]['setor'][0]  . " e " . $funcionarios[2]['setor'][1] .   "</p>"; 

/*comandos de repetição(loopings)*/
/*
    -indice = de onde começa a repetição.(ponto de partida)
    -teste logico = logica para que o comando continue repetindo.
    -incremento = é o que ocorre com o indice a cada reptição
*/
//$i = $i + 1 é a mesma coisa que $i++
for ($i=0; $i < 10; $i++) { 
    echo "<p>$i</p>";
};

for ($i=0; $i < 100; $i+=5) { 
    echo "$i - ";
};

echo "<br>";
$bebidas = array("vodka","fanta uva","suco","Água","Whisky","Café");
for ($i=0; $i < 6; $i++) { 
    echo $bebidas[$i]."<br>";
};

$contar = count($bebidas);
for ($i=0; $i < $contar; $i++) { 
    echo $bebidas[$i]."<br>";
};
?>







<!DOCTYPE html>
<html lang="pt-br">
<head>
    <!-- Define o tipo de documento como HTML5 -->
    <meta charset="UTF-8"> <!-- Define a codificação de caracteres como UTF-8 -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- Configura o viewport para garantir que a página seja exibida corretamente em dispositivos móveis -->
    <title>Atividade 5</title> <!-- Define o título da página que será exibido na aba do navegador -->
</head>
<body>
    <!-- 5 – Crie um script que verifique números pares e ímpares, em ordem decrescente, de 1 a 50 -->
    <?php 
        // Loop for que inicia com $i=50 e decrementa até $i ser igual a 1
        for($i=50; $i>=1; $i--){
            // Verifica se o número é ímpar (se o resto da divisão por 2 não é igual a 0)
            if($i%2 != 0){
                // Exibe que o número é ímpar, seguido por uma quebra de linha
                echo "O numero " . $i . " é impar" . "<br>";
            } else {
                // Se o número não for ímpar, exibe que o número é par, seguido por uma quebra de linha
                echo "O numero " . $i . " é par" . "<br>";
            }
        }
    ?>
</body>
</html>