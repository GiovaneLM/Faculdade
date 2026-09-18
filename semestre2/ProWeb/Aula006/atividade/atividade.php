<?php
$resultado = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $area = floatval($_POST["area"]);
    $ambiente = $_POST["ambiente"];
    $tabela = [
        9  => ["residencial" => 7000,  "comercial" => 7000],
        12 => ["residencial" => 7000,  "comercial" => 9000],
        15 => ["residencial" => 9000,  "comercial" => 12000],
        20 => ["residencial" => 12000, "comercial" => 16000],
        25 => ["residencial" => 15000, "comercial" => 20000],
        30 => ["residencial" => 18000, "comercial" => 24000],
        35 => ["residencial" => 21000, "comercial" => 28000],
        40 => ["residencial" => 24000, "comercial" => 32000],
        45 => ["residencial" => 27000, "comercial" => 36000],
        50 => ["residencial" => 30000, "comercial" => 40000],
        60 => ["residencial" => 36000, "comercial" => 48000],
        70 => ["residencial" => 42000, "comercial" => 56000]
    ];
    $btu = null;
    foreach ($tabela as $metros => $valores) {
        if ($area <= $metros) {
            $btu = $valores[$ambiente];
            break;
        }
    }
    if ($btu != null) {
        $resultado = "Para seu ambiente de {$area}m² é necessário um ar condicionado de {$btu} BTUs.";
    } else {
        $resultado = "Área maior que 70m².";
    }
}
?>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Calculadora de BTUs</title>
</head>
<body>
    <h1>Calculadora de BTUs</h1>
    <form method="POST">
        <label for="area">Área do ambiente (m²):</label>
        <input type="number" name="area" id="area" step="1" min="1" required>
        <br><br>
        <label for="ambiente">Tipo de ambiente:</label>
        <select name="ambiente" id="ambiente" required>
            <option value="">Selecione</option>
            <option value="residencial">Residencial</option>
            <option value="comercial">Comercial</option>
        </select>
        <br><br>
        <button type="submit">Calcular</button>
    </form>
    <?php
        if ($resultado != "") {
            echo "<p>";
            echo $resultado;
            echo "</p>";
        }
    ?>
</body>
</html>