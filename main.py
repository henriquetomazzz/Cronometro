from tkinter import *
import tkinter 

#cores
cor1 = "#0a0a0a" #preta
cor2 = "#fafcff" #branca 
cor3 = "#21c25c" #verde
cor4 = "#eb463b" #vermelha
cor5 = "#dedcdc" #cinza
cor6 = "#3080f0" #azul

#configurando a janela
janela = Tk()
janela.title("")
janela.geometry('300x180')
janela.configure(bg=cor1)
janela.resizable(width=FALSE, height=FALSE)

#definindo variaveis globais 
global tempo
global rodar
global contador
tempo = "00:00:10"
rodar = False
contador = -5

def iniciar():
  global tempo
  global contador

  if rodar:
    if contador <= -1:
      inicio = "Começando em ", str(contador)
      label_tempo['text'] = inicio
      label_tempo['font'] = 'Arial 10'

  else:
    print('Satisfeita')
    contador += 1


#criando labels 
label_app = Label(janela, text="cronômetro", fon=('Arial 10'), bg=cor1, fg=cor2)
label_app.place(x=20, y=5)

label_tempo = Label(janela, text=tempo, fon=('Times 50 bold'), bg=cor1, fg=cor6)
label_tempo.place(x=20, y=30)

#criando botões
botao_iniciar = Button(janela, text="Iniciar", width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_iniciar.place(x=20, y=130)

botao_pausar = Button(janela, text="Pausar", width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_pausar.place(x=105, y=130)

botao_reiniciar = Button(janela, text="Reiniciar", width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_reiniciar.place(x=190, y=130)

janela.mainloop()