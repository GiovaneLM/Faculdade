<?php 
$database = strtotime('2026-01-01');
$maisdezdias = strtotime('+10 days', $database);
echo 'sem formatar com date :';
echo "<br>";
echo $database;
echo "<br>";
echo $maisdezdias;
echo "<br>";
echo 'com formataçao do date:';
echo "<br>";
echo date('d/m/y',$database);
echo "<br>";
echo date('d/m/Y', $maisdezdias);
?>