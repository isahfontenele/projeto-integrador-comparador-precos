document.addEventListener("DOMContentLoaded", () => {
    const enviarBtn = document.getElementById("enviarBtn");
    const emailInput = document.getElementById("email");
    const successMessage = document.getElementById("successMessage");

    enviarBtn.addEventListener("click", async () => {
        console.log("Botão 'Enviar' foi clicado!"); // 📌 Teste no console

        const email = emailInput.value.trim();

        // Limpa mensagens anteriores
        successMessage.textContent = "";

        // 📌 Se o campo estiver vazio, ainda mostramos a mensagem
        if (!email) {
            successMessage.textContent = "Se o e-mail estiver cadastrado, você receberá uma mensagem de recuperação.";
            return;
        }

        try {
            const response = await fetch("https://comparadorapi-cfegcpfyc2grbhbk.brazilsouth-01.azurewebsites.net/accounts/forgot-password", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ email: email })
            });

            console.log("Resposta da API:", response.status); // 📌 Teste no console

            // 📌 Independentemente do resultado, exibe a mensagem solicitada
            successMessage.textContent = "Se o e-mail estiver cadastrado, você receberá uma mensagem de recuperação.";
        } catch (error) {
            console.error("Erro na requisição:", error);
            successMessage.textContent = "Se o e-mail estiver cadastrado, você receberá uma mensagem de recuperação.";
        }
    });
});
