# Auto Clicker em Python

Um programa de auto click completo desenvolvido em Python que permite automatizar cliques do mouse com várias configurações.

## Funcionalidades

- ✅ Configuração de intervalo entre cliques
- ✅ Definição de posição específica ou posição atual do mouse
- ✅ Diferentes tipos de clique (esquerdo, direito, duplo, meio)
- ✅ Interface de linha de comando intuitiva
- ✅ Controle de parada com tecla ESC
- ✅ Contador de cliques e tempo decorrido
- ✅ Threading para não travar a interface

## Instalação

1. **Instale as dependências:**
   ```bash
   pip install -r requirements_auto_click.txt
   ```

2. **Ou instale manualmente:**
   ```bash
   pip install pyautogui keyboard
   ```

## Como Usar

1. **Execute o programa:**
   ```bash
   python auto_click.py
   ```

2. **Configure as opções:**
   - **Intervalo**: Tempo entre cliques (em segundos)
   - **Posição**: Pressione 'p' para definir posição atual ou 'Enter' para usar posição dinâmica
   - **Tipo de clique**: Escolha entre esquerdo, direito, duplo ou meio

3. **Inicie o auto click:**
   - Selecione a opção 5 no menu
   - O programa começará a clicar automaticamente

4. **Para parar:**
   - Pressione **ESC** para parar o auto click
   - Ou mova o mouse para o **canto superior esquerdo** da tela (failsafe)

## Configurações de Segurança

- **FAILSAFE**: Mova o mouse para o canto superior esquerdo para parar o programa
- **PAUSE**: Pausa de 0.1 segundos entre comandos para estabilidade

## Tipos de Clique Disponíveis

1. **Clique Esquerdo**: Clique normal do botão esquerdo
2. **Clique Direito**: Clique do botão direito (menu de contexto)
3. **Clique Duplo**: Dois cliques rápidos
4. **Clique do Meio**: Clique do botão do meio (scroll)

## Exemplos de Uso

### Exemplo 1: Clique simples a cada 2 segundos
- Intervalo: 2.0
- Tipo: Clique esquerdo
- Posição: Atual

### Exemplo 2: Clique direito em posição fixa
- Intervalo: 1.5
- Tipo: Clique direito
- Posição: (500, 300)

### Exemplo 3: Clique duplo para jogos
- Intervalo: 0.5
- Tipo: Clique duplo
- Posição: Atual

## Recursos Técnicos

- **Threading**: Execução em thread separada para não travar a interface
- **Tratamento de Erros**: Captura e exibe erros durante a execução
- **Logging**: Mostra contador de cliques e tempo decorrido
- **Configuração Dinâmica**: Permite alterar configurações durante a execução

## Compatibilidade

- ✅ Windows
- ✅ macOS
- ✅ Linux

## Avisos Importantes

⚠️ **Use com responsabilidade!**
- Este programa pode ser usado para automação legítima
- Não use para trapacear em jogos online
- Sempre teste em ambiente seguro primeiro
- O failsafe (canto superior esquerdo) é sua proteção principal

## Solução de Problemas

### Erro de permissão no Windows:
```bash
# Execute como administrador ou use:
pip install --user pyautogui keyboard
```

### Mouse não responde:
- Verifique se o programa tem permissões de administrador
- Teste o failsafe movendo o mouse para o canto superior esquerdo

### Programa trava:
- Use Ctrl+C para forçar a parada
- O failsafe sempre funciona como backup

## Licença

Este projeto é de código aberto e pode ser usado livremente para fins educacionais e de automação legítima. 