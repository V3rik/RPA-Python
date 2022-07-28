#!/usr/bin/env python
# coding: utf-8

# In[2]:


#comando para baixar e instalar bibliotecas:

get_ipython().system('pip install pyautogui')


# In[ ]:


# passo a passo para se abrir o whatsapp web.

# 1 passo - apertar tecla (win).
# 2 passo - Escrever opera.
# 3 passo - apertar a tecla enter.
# 4 passo - Abrir whatsappweb.
# 5 passo - pesquisar agatha.
# 6 passo - Selecionar contato.
# 7 passo - digitar menssagem "oi tudo bem?"


# In[34]:


#importar biblioteca pyautogui
import pyautogui

#importando biblioteca time.
import time





                                                  #execução
    
    
    
#comando para digitar o nome do contato.
contato = input ("Para qual contato devo enviar menssagem ")






    
    #abrir navegador
    
#precionar a tecla (win)  
pyautogui.press("win")


#digitar opera
pyautogui.write("opera")


#precionar tecla (enter)
pyautogui.press("enter")

    #abrir navegador
    
    
    
   



    #abrir Whatsapp
    
#aguardar 2 segundos
time.sleep(2)

    
#clicar na posição indicada
pyautogui.click(x=18,y=246)


#Aguardar 5 segundos até o wpp web carregar.
time.sleep(10)


#clicar na posição de pesquisa.
pyautogui.click(x=125, y=115)


#pesquisar nome do contato.
pyautogui.write(contato) #OBS: utilizamos de uma variavel chamada contato onde podemos escrever o nome do contato.


#Aguardar 3 segundos até o wpp web carregar.
time.sleep(3)

    #abrir Whatsapp
    
    
    
    


    
    #digitar texto    

#clciar no primeiro contato
pyautogui.click(x=163, y=255)


#Aguardar 1 segundos até o wpp web carregar.
time.sleep(1)


#clicar na caixa de texto
pyautogui.click(x=351, y=1125)



#Aguardar 1 segundos até o wpp web carregar.
time.sleep(1)



#Criando a variavel que vai carregar nosso texto:
texto = f"""
Olá tudo bem? você acaba de receber uma menssagem do bot amigo!

"""

#Vai escrever a variavel texto.
pyautogui.write(texto)


#Aguardar 1 segundos até o wpp web carregar.
time.sleep(1)

#precionar tecla (enter)
pyautogui.press("enter")

    #digitar texto  





#OBS: note que a letra f antes das aspas representa que o texto deve ser formatado da seguinte forma.

    #digitar texto   



# In[ ]:





# In[ ]:





# In[35]:


#aguarda 5 segundos.
import time
import pyautogui

time.sleep(5)

pyautogui.position()


# In[ ]:




