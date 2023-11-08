# Regras do Jogo

## Objetivo
O objetivo do jogo é organizar os quadrados coloridos de modo que cada pilha contenha quadrados de uma única cor.

## Como Jogar
- Clique em um quadrado para selecioná-lo.
- Clique em uma pilha para mover o quadrado selecionado para essa pilha, se houver espaço disponível.
- Você só pode mover quadrados para pilhas que tenham espaço para mais quadrados (até 3 por pilha).
- O jogo termina quando todas as pilhas estiverem organizadas com quadrados da mesma cor.

## Regras
- Cada pilha pode conter no máximo 3 quadrados.
- Se a pilha estiver cheia, você deve mover um quadrado para outra pilha antes de adicionar um novo.
- A última pilha (por exemplo, Stack5 em um jogo com 5 pilhas) é usada como área de transferência e também deve conter quadrados da mesma cor para completar o jogo.
- A barra de status na parte inferior da tela indicará quando o objetivo for alcançado.

## Dicas
- Planeje seus movimentos com antecedência.
- Use a pilha de transferência (última pilha) para temporariamente armazenar quadrados enquanto organiza as outras pilhas.

## Níveis de Dificuldade
- O jogo pode ser jogado em diferentes níveis de dificuldade. O nível de dificuldade padrão é com 5 pilhas.
- Em níveis de dificuldade mais altos, o número de pilhas aumenta, adicionando mais complexidade ao jogo.

## Configuração do Nível de Dificuldade
- Para alterar o nível de dificuldade, ajuste o número de pilhas e quadrados por pilha ao iniciar o jogo.
- Por exemplo, ao chamar `setup_stacks(num_stacks=6, num_squares_per_stack=3)`, o jogo iniciará com 6 pilhas.

Boa sorte e divirta-se!
