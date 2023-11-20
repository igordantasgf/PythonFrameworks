<?php
// Lógica para enviar a mensagem via rota de API (substitua esta lógica pela sua implementação real)
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $message = $_POST["message"];
    
    // Faça a chamada da API ou a lógica de armazenamento aqui

    // Redirecionar de volta para a página principal
    header("Location: index.php");
    exit();
}
?>
