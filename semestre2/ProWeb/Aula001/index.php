<?php

$aluno = "Model";//String
$idade = 21; //int
$altura = 1.84; //float
$matriculado = true; //true - false (boolean)

echo 'OLA, $aluno BEM VINDO AS AULAS DE php!<br>';

echo "OLA, $aluno BEM VINDO AS AULAS DE php!";

$x= "20";
$y= 5.3;
$soma = $x + $y;
echo $soma;

//concatenar(juntar strings)
$nome= "Gabriel ";
$sobrenome="Madel";
echo $nome;

$nome .= "Model";
echo "<h2>$nome<h2>";

//CONSTANTE

define("CURSO", "programação com PHP");
echo CURSO;
//NÃO PERMITE MUDAR O VALOR.
//define("CURSO", "HTML E CSS");

const TESTE = "Novo";
echo  "<br>" . TESTE;
?>