import random
import flet as ft


def sorteio():
    lista = ["amuleto1.PNG", "carta1.PNG", "laranja1.PNG", "wild1.PNG", "fogo_de_artificio1.PNG",
             "saco_de_ouro1.PNG", "zovo_de_ouro1.PNG"]
    a = random.choice(lista)
    b = random.choice(lista)
    c = random.choice(lista)
    d = random.choice(lista)
    e = random.choice(lista)
    f = random.choice(lista)
    g = random.choice(lista)
    h = random.choice(lista)
    i = random.choice(lista)

    return [a, b, c, d, e, f, g, h, i]


sorte = sorteio()


def main(page: ft.Page):
    def button_clicked(e):
        global sorte
        sorte = sorteio()
        page.clean()
        retry = ft.IconButton(icon=ft.icons.ASSIGNMENT_RETURN, on_click=button_clicked)
        item1 = ft.Image(src=f"images/{sorte[0]}", width=100, height=100)
        item2 = ft.Image(src=f"images/{sorte[1]}", width=100, height=100)
        item3 = ft.Image(src=f"images/{sorte[2]}", width=100, height=100)
        item4 = ft.Image(src=f"images/{sorte[3]}", width=100, height=100)
        item5 = ft.Image(src=f"images/{sorte[4]}", width=100, height=100)
        item6 = ft.Image(src=f"images/{sorte[5]}", width=100, height=100)
        item7 = ft.Image(src=f"images/{sorte[5]}", width=100, height=100)
        item8 = ft.Image(src=f"images/{sorte[7]}", width=100, height=100)
        item9 = ft.Image(src=f"images/{sorte[8]}", width=100, height=100)
        page.add(
            ft.Row(controls=[titulo],
                   vertical_alignment=ft.CrossAxisAlignment.CENTER,
                   alignment=ft.MainAxisAlignment.CENTER),
            # literal jogo
            ft.Row(controls=[item1, item2, item3],
                   vertical_alignment=ft.CrossAxisAlignment.CENTER,
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(controls=[item4, item5, item6],
                   vertical_alignment=ft.CrossAxisAlignment.CENTER,
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(controls=[item7, item8, item9],
                   vertical_alignment=ft.CrossAxisAlignment.CENTER,
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(controls=[retry],
                   vertical_alignment=ft.CrossAxisAlignment.CENTER,
                   alignment=ft.MainAxisAlignment.CENTER),

        )


    page.title = "jogo do patinho"
    page.theme_mode = "light"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text("Fortune Duck", size=50)

    global sorte
    retry = ft.IconButton(icon=ft.icons.ASSIGNMENT_RETURN, on_click=button_clicked)
    item1 = ft.Image(src=f"images/{sorte[0]}", width=100, height=100)
    item2 = ft.Image(src=f"images/{sorte[1]}", width=100, height=100)
    item3 = ft.Image(src=f"images/{sorte[2]}", width=100, height=100)
    item4 = ft.Image(src=f"images/{sorte[3]}", width=100, height=100)
    item5 = ft.Image(src=f"images/{sorte[4]}", width=100, height=100)
    item6 = ft.Image(src=f"images/{sorte[5]}", width=100, height=100)
    item7 = ft.Image(src=f"images/{sorte[5]}", width=100, height=100)
    item8 = ft.Image(src=f"images/{sorte[7]}", width=100, height=100)
    item9 = ft.Image(src=f"images/{sorte[8]}", width=100, height=100)

    page.add(
        ft.Row(controls=[titulo],
               vertical_alignment=ft.CrossAxisAlignment.CENTER,
               alignment=ft.MainAxisAlignment.CENTER),
        # literal jogo
        ft.Row(controls=[item1, item2, item3],
               vertical_alignment=ft.CrossAxisAlignment.CENTER,
               alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[item4, item5, item6],
               vertical_alignment=ft.CrossAxisAlignment.CENTER,
               alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[item7, item8, item9],
               vertical_alignment=ft.CrossAxisAlignment.CENTER,
               alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[retry],
               vertical_alignment=ft.CrossAxisAlignment.CENTER,
               alignment=ft.MainAxisAlignment.CENTER),

    )


# def bets():

# if a == b and a == c:
# print("vc ganhou, infeliz")
# prize = bet * 1.5
# result = money - bet + prize
# print(result)
# return result

# else:
# print("vc se fudeu kkkkkk")
# result = money - bet
# print(result)
# return result


ft.app(main)
# sla = 1
# money = float(input("quanto reais vc quer depositar: "))
# while sla == 1:
# bet = float(input("quanto vc quer apostar: "))
# if bet > money:
# print("vc tá doido home apostando mais do que tem kkkkkk")
# sla = 2
# else:
# money = bets()
# sla = int(input("você quer continuar apostando? 1 = sim 2 = não:"))
