import pyautogui as pyag
import pandas as pd
import time

def clicar_no_botao_importacao():
    botao_import = None  # Inicialize como None para entrar no loop
    while botao_import is None:  # Continue enquanto o botão não for encontrado
        try:
            botao_import = pyag.locateCenterOnScreen('importa.png', confidence=0.8)
            if botao_import:
                pyag.moveTo(botao_import, duration=2)
                pyag.click(botao_import)
                print("Botão import encontrado e clicado.")
                break  # Sai do loop após clicar no botão
            else:
                print("Botão não encontrado. Tentando novamente...")
                time.sleep(2)
        except Exception as e:
            print(f"Ocorreu um erro ao encontrar o botão import: {str(e)}")
            time.sleep(2)


def clicar_no_botao_nao():
    tentativas = 0
    max_tentativas = 1000
    while tentativas < max_tentativas:
        try:
            botao_nao = pyag.locateCenterOnScreen('bot-nao.png', confidence=0.9)
            if botao_nao:
                pyag.moveTo(botao_nao, duration=2)
                pyag.click(botao_nao, clicks=2)
                print("Botão import encontrado e clicado.")
                return True  # Retorna True indicando sucesso
            else:
                print("Botão não encontrado. Tentando novamente...")
                tentativas += 1
        except Exception as e:
            print(f"Ocorreu um erro ao encontrar botao nao: {str(e)}")
            tentativas += 1

    print("Número máximo de tentativas atingido sem encontrar o botão.")
    return False  # Retorna False indicando falha


def clicar_no_botao_nao2():
    tentativas = 0
    max_tentativas = 350
    while tentativas < max_tentativas:
        try:
            botao_nao = pyag.locateCenterOnScreen('bot-naao.png', confidence=0.8)
            if botao_nao:
                pyag.moveTo(botao_nao, duration=2)
                pyag.click(botao_nao, clicks=2)
                print("Botão nao2 encontrado e clicado.")
                return True  # Retorna True indicando sucesso
            else:
                print("Botão não encontrado. Tentando novamente...")
                tentativas += 1
        except Exception as e:
            print(f"Ocorreu um erro ao encontrar botao nao 2: {str(e)}")
            tentativas += 1

    print("Número máximo de tentativas atingido sem encontrar o botão.")
    return False  # Retorna False indicando falha


def verificar_imagens_e_executar_fluxo():
    max_tentativas = 300000
    tentativas = 0
    while tentativas < max_tentativas:
        if tentar_acionar_fluxo('reg-import.png', seguir_fluxo_a):
            break
        if tentar_acionar_fluxo('cap-certa.png', seguir_fluxo_b):
            break
        tentativas += 1
    else:
        print("Número máximo de tentativas atingido sem encontrar as imagens.")

def tentar_acionar_fluxo(imagem, funcao_fluxo):
    try:
        local_imagem = pyag.locateOnScreen(imagem, confidence=0.7)
        if local_imagem:
            pyag.moveTo(local_imagem, duration=2)
            print(f"Imagem encontrada para {funcao_fluxo.__name__}. Seguindo fluxo correspondente.")
            funcao_fluxo()
            return True
    except Exception as e:
        print(f"Erro ao procurar {imagem}: {e}")
    return False


def seguir_fluxo_a():
    print("Executando ações do Fluxo A.")
        # Execute as ações necessárias para o Fluxo A aqui.
        # Garanta que a função termine de maneira limpa após concluir as tarefas.
    botao_erro_encontrado = False
    while not botao_erro_encontrado:
            try:
                botao_erro = pyag.locateCenterOnScreen('bot-erro.png', confidence=0.7)
                if botao_erro:
                    pyag.moveTo(botao_erro, duration=2)
                    pyag.click(botao_erro)
                    print("Botão encontrado e clicado.")
                    botao_erro_encontrado = True
                    break  # Sai do loop uma vez que o botão foi encontrado e clicado
                else:
                    print("Botão não encontrado. Tentando novamente...")
                    time.sleep(2)  # Espera 2 segundos antes de tentar novamente

            except Exception as e:
                print(f"Ocorreu um erro ao encontrar botao erro: {str(e)}")
                time.sleep(2)  # Espera antes de tentar novamente para evitar sobrecarga

    print("Processo concluído.")  # Mensagem após sair do loop

    botao_x_encontrado = False
    while not botao_x_encontrado:
        try:
            botao_x = pyag.locateCenterOnScreen('botao-x.png', confidence=0.9)
            if botao_x:
                pyag.moveTo(botao_x, duration=2)
                pyag.click(botao_x)
                print("Botão encontrado e clicado.")
                botao_x_encontrado = True
                break  # Sai do loop uma vez que o botão foi encontrado e clicado
            else:
                print("Botão não encontrado. Tentando novamente...")
                time.sleep(2)  # Espera 2 segundos antes de tentar novamente

        except Exception as e:
            print(f"Ocorreu um erro ao encontrar botao-x: {str(e)}")
            time.sleep(2)  # Espera antes de tentar novamente para evitar sobrecarga

    print("Processo concluído.")  # Mensagem após sair do loop
    # Executar a função principal

    # Loop que continua até que o botão seja encontrado
    botao_fecha_aba = False
    while not botao_fecha_aba:
        try:
            botao_f_aba = pyag.locateCenterOnScreen('bot-fecha-aba.png', confidence=0.9)
            if botao_f_aba:
                pyag.moveTo(botao_f_aba, duration=2)
                pyag.click(botao_f_aba)
                print("Botão encontrado e clicado.")
                botao_fecha_aba = True
                break  # Sai do loop uma vez que o botão foi encontrado e clicado
            else:
                print("Botão não encontrado. Tentando novamente...")
                time.sleep(2)  # Espera 2 segundos antes de tentar novamente

        except Exception as e:
            print(f"Ocorreu um erro ao encontrar o botao fecha aba: {str(e)}")
            time.sleep(2)  # Espera antes de tentar novamente para evitar sobrecarga

    print("Processo concluído.")  # Mensagem após sair do loop


    # Loop que continua até que o botão seja encontrado
    botao_sim_encontrado = False
    while not botao_sim_encontrado:
        try:
            botao_sim = pyag.locateCenterOnScreen('bot-sim.png', confidence=0.7)
            if botao_sim:
                pyag.moveTo(botao_sim, duration=2)
                pyag.click(botao_sim, clicks=2)
                print("Botão encontrado e clicado.")
                botao_sim_encontrado = True
                break  # Sai do loop uma vez que o botão foi encontrado e clicado
            else:
                print("Botão não encontrado. Tentando novamente...")
                time.sleep(2)  # Espera 2 segundos antes de tentar novamente

        except Exception as e:
            print(f"Ocorreu um erro ao encontrar botao deseja sair: {str(e)}")
            time.sleep(2)  # Espera antes de tentar novamente para evitar sobrecarga

    print("Processo concluído.")  # Mensagem após sair do loop


def seguir_fluxo_b():
    print("Executando ações do Fluxo B.")
    # Aqui você colocaria o código para interagir com elementos ou executar tarefas específicas do Fluxo B
    # O código para seguir o fluxo B está aqui.
    botao_certo_encontrado = False
    while not botao_certo_encontrado:
            try:
                botao_certo = pyag.locateCenterOnScreen('bot-certo.png', confidence=0.7)
                if botao_certo:
                    pyag.moveTo(botao_certo, duration=2)
                    pyag.click(botao_certo)
                    print("Botão encontrado e clicado.")
                    botao_certo_encontrado = True
                    break  # Sai do loop uma vez que o botão foi encontrado e clicado
                else:
                    print("Botão não encontrado. Tentando novamente...")
                    time.sleep(2)  # Espera 2 segundos antes de tentar novamente

            except Exception as e:
                print(f"Ocorreu um erro ao encontrar botao certo: {str(e)}")
                time.sleep(2)  # Espera antes de tentar novamente para evitar sobrecarga

    print("Processo concluído.")  # Mensagem após sair do loop

def repetir_envio_notas(numero_repeticoes):
    for _ in range(numero_repeticoes):
        time.sleep(3)
        pyag.press('enter')

 
def processar_empresas(porfora_csv, delimiter=';'):
    # Carrega os dados do CSV
    df = pd.read_csv(porfora_csv, delimiter=';')

    # Itera sobre cada linha do DataFrame
    for index, row in df.iterrows():
        numero_empresa = row['codigo']
        caminho_pasta = row['caminhos']
        
        pyag.click(x=781, y=147) # clicando em integração
        time.sleep(3)
        pyag.click(x=917, y=323) # clicando em CFE
        time.sleep(5)
        pyag.hotkey('shift', 'tab')
        time.sleep(3)
        pyag.write(str(numero_empresa)) # empresa
        time.sleep(3)
        pyag.press('enter')
        time.sleep(3)
        pyag.write('259')
        time.sleep(2)
        pyag.press('enter')
        time.sleep(3)
        pyag.write('5949000')
        time.sleep(3)
        # data inicio
        pyag.write('01')
        time.sleep(3)
        pyag.write('07')
        time.sleep(3)
        pyag.write('2024')
        time.sleep(3)
        # data final
        pyag.write('31')
        time.sleep(3)
        pyag.write('07')
        time.sleep(3)
        pyag.write('2024')
        time.sleep(3)
        pyag.write(caminho_pasta) # caminho da empresa
        time.sleep(3)
        print(f'Iniciando empresa: str({numero_empresa})')
        time.sleep(3)
        pyag.press('enter')


        repetir_envio_notas(1)
        #clicar_no_botao_nao()
        clicar_no_botao_importacao()
        verificar_imagens_e_executar_fluxo()
        clicar_no_botao_nao2() 


#processar_empresas('C:\\Users\\gabriel.mf\\Downloads\\automacao\\porfora.csv')
processar_empresas('C:\\Users\\gabriel.mf\\Downloads\\automacao\\porfora.csv')