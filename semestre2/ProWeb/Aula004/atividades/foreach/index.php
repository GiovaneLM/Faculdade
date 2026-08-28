<?php 
    $alunos = [
        [
            "nome" => "Aluno1",
            "curso" => "Curso1",
            "nota" => "7"
        ],
        [
            "nome" => "Aluno2",
            "curso" => "Curso2",
            "nota" => "8"
        ],
        [
            "nome" => "Aluno3",
            "curso" => "Curso3",
            "nota" => "9"
        ],
        [
            "nome" => "Aluno4",
            "curso" => "Curso4",
            "nota" => "10"
        ],
        [
            "nome" => "Aluno5",
            "curso" => "Curso5",
            "nota" => "6"
        ],
    ];

foreach ($alunos as $aluno){
    echo "O aluno " . $aluno['nome'] . " do Curso " . $aluno['curso'] . " tirou nota " . $aluno['nota'] . "<br>";
}
?>