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
global limitador

limitador = 59
tempo = "00:00:00"
rodar = False
contador = -5

#função iniciar
def iniciar():
  global tempo
  global contador
  global limitador

  if rodar:
    if contador <= -1:
      inicio = 'Começando em ', str(contador)
      label_tempo['text'] = inicio
      label_tempo['font'] = 'Arial 10'

#rodando cronômetro
  else:
     label_tempo['font'] = 'Times 50 bold'
     temporario = str(tempo)
     h, m, s = map(int, temporario.split(":"))
     h = int(h)
     m = int(m)
     s = int(contador)

     if (s>=limitador):
       contador = 0
       m+=1
       
     s = str(0) + str(s)
     m = str(0) + str(m)
     h = str(0) + str(h)
     
     #atualizando os valores
     temporario = str(h[-2:]) + ":" + str(m[-2:]) + ":" + str(s[-2:])
     label_tempo['text'] = temporario
     tempo = temporario

  label_tempo.after(1000, iniciar)
  contador += 1

#função para dar inicio
def start():
  global rodar
  rodar = True 
  iniciar()

#função para pausar
def pausar():
  global rodar 
  rodar = False

#função para reiniciar
def reiniciar():
  global contador
  global tempo

  #reiniciando o contador
  contador = 0

  #reiniciando o tempo
  tempo = "00:00:00"
  label_tempo = tempo

#criando labels 
label_app = Label(janela, text="cronômetro", fon=('Arial 10'), bg=cor1, fg=cor2)
label_app.place(x=20, y=5)

label_tempo = Label(janela, text=tempo, fon=('Times 50 bold'), bg=cor1, fg=cor6)
label_tempo.place(x=20, y=30)

#criando botões
botao_iniciar = Button(janela, command=start, text="Iniciar", width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_iniciar.place(x=20, y=130)

botao_pausar = Button(janela, command=pausar, text="Pausar", width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_pausar.place(x=105, y=130)

botao_reiniciar = Button(janela, command=reiniciar, text="Reiniciar", width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_reiniciar.place(x=190, y=130)

janela.mainloop()