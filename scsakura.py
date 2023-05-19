import turtle as tr

s = tr.Screen()
tr.setup(800, 800)
s.bgcolor('#FFFFFF')  # Warna latar belakang

def draw_branch(length):
    if length < 5:
        return

    tr.pensize(length / 10)  # Menyesuaikan ketebalan garis dengan panjang cabang
    tr.forward(length)
    tr.right(30)
    draw_branch(length * 0.7)  # Menggambar cabang anak di sisi kanan
    tr.left(60)
    draw_branch(length * 0.7)  # Menggambar cabang anak di sisi kiri
    tr.right(30)
    tr.backward(length)


tr.speed(0)
tr.penup()
tr.goto(0, -300)  # Posisi awal pohon
tr.pendown()
tr.left(90)  # Menghadap ke atas

tr.color('#FF69B4')  # Warna bunga sakura
draw_branch(100)  # Panjang cabang awal

s.exitonclick()


