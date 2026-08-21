<?php

$i=1;

while($i <= 10){
    echo "<h3>$i</h3>";
    $i++;
}
echo "<hr>";
$filmes = ["missao impossivel","um sonho de liberdade","matrix","mid90","topgun"];

$i = 1;
$i=0;
while($i < 5){
    echo $i+1 . " -  $filmes[$i] <br>";
    $i++;
}
$i=10;
while($i>0){
    echo "$i - ";
    $i--;
}
echo"<br>";
$i=count($filmes) - 1;
while($i>=0){
    echo $i+1 . " - $filmes[$i]<br>";
    $i--;
}

/*foreach - ideal para arrays*/
echo "<hr>";
foreach($filmes as $key => $filme){
    $key = $key + 1;
    echo "<p> $key - $filme</p>";
}


echo "<hr>";
$alunos = [
    [
        "nome" => "roblox",
        "matricula" => "1345",
        "idade" => 21
    ],
    [
        "nome" => "ana beatriz",
        "matricula" => "54561",
        "idade" => 25
    ],
    [
        "nome" => "maryane",
        "matricula" => "4894986",
        "idade" => 23
    ]
];


for($i=0;$i<3;$i++){
    echo $alunos[$i]['nome'] . "<br>";
}

echo "<hr>";
$i = 0;
while($i < count($alunos)){
    $nome = $alunos[$i]['nome'];
    $idade = $alunos[$i]['idade'];
    $matricula = $alunos[$i]['matricula'];
    echo "o aluno $nome de matricula $matricula possui $idade anos. <br>";
    $i++;
}


echo "<hr>";
echo "<h2>mostrando daods com foreach</h2>";
foreach($alunos as $aluno){
    echo "o aluno $aluno[nome] de matricula $aluno[matricula] possui $aluno[idade] anos. <br>";
}


echo "<hr>";
echo "<hr>";
echo "<hr>";
$idade="12";
if ($idade >=18){
    echo "<p>entrada autorizada!</p>";
}else{
    echo "<p>entrada somente para maiores de 18 anos</p>";
}


echo "<hr>";
$aluno = "Ricardo";

if($aluno = "Ricardo"){
    echo "passar na coordenação";
}else{
    echo "<p>entrada autorizada!</p>";
}


echo "<hr>";
if($aluno == "Ricardo" or $aluno=="Giovane" || $aluno=="Guilherme"){
    echo "passar na coordenação";
}else{
    echo "<p>entrada autorizada!</p>";
}

echo "<hr>";
$login="admin";
$senha=12345;
if($login == "admin" and $senha === 12345){
    echo "bem vindo";
}else{
    echo "invalido";
}

echo "<hr>";
$nota1 = 5;
$nota2 = 8;
$nota3 = 10;

$media = ($nota1 + $nota2 + $nota3)/3;
if($media >= 7){
    echo "aprovado media: $media";
}elseif($media<=5){
    echo "reprovado media: $media" ;
}else{
    echo "recuperação media: $media";
}





?>