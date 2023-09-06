<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $arquivo = $_FILES['arquivo'];

    $nome = $arquivo['name'];
    $temporario = $arquivo['tmp_name'];
    $destino = '/download/' . $nome;

    if (move_uploaded_file($temporario, $destino)) {
        echo 'Arquivo enviado com sucesso.';
    } else {
        echo 'Erro ao enviar o arquivo.';
    }
}
?>
