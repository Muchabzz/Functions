import turtle
from figures import draw_square

window = turtle.Screen()
window.bgcolor("lightgreen")

draw_square(100)  #100 to jest lenght

window.mainloop() #nie zamykaj okna, czekaj aż użytkownik je zamknie
