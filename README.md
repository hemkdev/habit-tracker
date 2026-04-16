# Rastreador de Hábitos em Terminal

## Sobre

O **Habit Tracker** é uma aplicação de linha de comando desenvolvida em Python para ajudar usuários a registrar e acompanhar seus hábitos diários. Ele permite gerenciar seu hábitos de maneira simples,adicionando, excluindo, listando e marcando hábitos como concluídos para o dia atual. Os dados dos são armazenados em um arquivo JSON, garantindo persistência e facilidade de uso sem a necessidade de um banco de dados complexo. A interface é simples e baseada em texto, ideal para quem busca uma ferramenta leve e eficiente para gerenciamento de hábitos.

## Requisitos

Para executar este projeto, você precisará de:

*   **Python 3.x:** Certifique-se de ter o Python 3 instalado em seu sistema.

## Como Iniciar

Siga os passos abaixo para configurar e executar o projeto localmente:

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/hemkdev/habit-tracker.git
    cd habit-tracker
    ```

2.  **Execute a aplicação:**

    ```bash
    python3 main.py
    ```

    A aplicação será iniciada no terminal, apresentando um menu de opções.

## Uso

Ao executar `main.py`, você verá um menu com as seguintes opções:

*   **Adicionar Hábito:** Permite inserir um novo hábito na sua lista.
*   **Listar Hábitos:** Exibe todos os hábitos registrados e o número de dias em que foram concluídos.
*   **Marcar Hábito Concluído:** Permite marcar um hábito específico como concluído para a data atual.
    **Excluir Hábito** Permite excluir um hábito de sua lista.
*   **Sair:** Encerra a aplicação.

Os dados são salvos automaticamente no arquivo `habitos.json` criado na mesma pasta do script.

## Contribuições

Contribuições são bem-vindas! Se você tiver ideias para novas funcionalidades (como adicionar datas específicas para conclusão, gráficos de progresso, ou uma interface mais interativa), encontrar bugs ou quiser otimizar o código, por favor, siga estas diretrizes:

*   Faça um *fork* do repositório.
*   Crie uma nova *branch* para suas alterações (`git checkout -b feature/nova-funcionalidade`).
*   Implemente suas alterações e faça *commits* claros e descritivos.
*   Envie suas alterações para o seu *fork* (`git push origin feature/nova-funcionalidade`).
*   Abra um *Pull Request* para o repositório principal, descrevendo detalhadamente as modificações propostas.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações. (Nota: O arquivo LICENSE não foi fornecido no repositório original, mas é uma boa prática incluí-lo.)
