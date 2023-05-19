import turtle as tr
import random

# Membuat layar
s = tr.Screen()
s.setup(800, 600)
s.bgcolor('white')

# Membuat kura-kura pemain
player = tr.Turtle()
player.shape('turtle')
player.shapesize(2)  # Mengubah ukuran kura-kura menjadi dua kali lipat lebih besar
player.color('green')
player.penup()

# Membuat makanan
foods = []  # List untuk menyimpan makanan

for _ in range(5):  # Membuat 5 makanan
    food = tr.Turtle()
    food.shape('circle')
    food.color('red')
    food.penup()
    food.goto(random.randint(-380, 380), random.randint(-280, 280))
    foods.append(food)  # Menambahkan makanan ke dalam list

# Fungsi untuk menggerakkan kura-kura pemain
def move_forward():
    player.forward(10)

# Fungsi untuk mengubah arah kura-kura pemain ke kiri
def turn_left():
    player.left(30)

# Fungsi untuk mengubah arah kura-kura pemain ke kanan
def turn_right():
    player.right(30)

# Fungsi untuk memeriksa jika kura-kura pemain bertabrakan dengan makanan
def check_collision():
    for food in foods:  # Memeriksa setiap makanan dalam list
        if player.distance(food) < 20:
            food.goto(random.randint(-380, 380), random.randint(-280, 280))

# Menghubungkan tombol-tombol dengan fungsi-fungsi
s.onkey(move_forward, 'Up')
s.onkey(turn_left, 'Left')
s.onkey(turn_right, 'Right')

s.listen()  # Mengaktifkan input dari keyboard

# Game loop
while True:
    player.forward(1)  # Menggerakkan kura-kura pemain secara terus-menerus
    check_collision()  # Memeriksa tabrakan dengan makanan

    # Mengecek batasan layar
    if player.xcor() > 400 or player.xcor() < -400 or player.ycor() > 300 or player.ycor() < -300:
        player.goto(0, 0)  # Mengembalikan kura-kura pemain ke posisi awal

s.mainloop() 
