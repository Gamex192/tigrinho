import random
import flet as ft


def sorteio():
    lista = ["amuleto.PNG", "carta.PNG", "laranja.PNG", "wild.PNG", "fogo_de_artificio.PNG",
             "saco_de_ouro.PNG", "zovo_de_ouro.PNG"]
    a = random.choice(lista)

    return a


def main(page: ft.Page):
    def pagina():
        def item(a):
            return ft.Container(image_src=f"images/{sorteio()}", padding=50, margin=2)

        page.clean()
        item1 = item(0)
        item2 = item(1)
        item3 = item(2)
        item4 = item(3)
        item5 = item(4)
        item6 = item(5)
        item7 = item(6)
        item8 = item(7)
        item9 = item(8)
        page.add(
            # ft.Row(controls=[titulo],
            # vertical_alignment=ft.CrossAxisAlignment.CENTER,
            # alignment=ft.MainAxisAlignment.CENTER),
            # literal jogo
            ft.Container(
                bgcolor=ft.colors.WHITE,
                width=460,
                height=800,
                image_src="images/fundo.PNG",
                content=
                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            margin=ft.margin.only(bottom=80, top=175),
                            content=
                            ft.Column(controls=[
                                ft.Row(controls=[item1, item2, item3],
                                       vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                       alignment=ft.MainAxisAlignment.CENTER,
                                       spacing=25,
                                       ),
                                ft.Row(controls=[item4, item5, item6],
                                       vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                       alignment=ft.MainAxisAlignment.CENTER,
                                       spacing=25,
                                       ),
                                ft.Row(controls=[item7, item8, item9],
                                       vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                       alignment=ft.MainAxisAlignment.CENTER,
                                       spacing=25,
                                       ),
                            ])
                        ),
                        # isso é pra dá a Mer** do espassamento entr a bos** do botão e a roleta
                        ft.Row(
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                    ft.TextField(color=ft.colors.YELLOW,
                                                 scale=0.45,
                                                 text_size=30,
                                                 border_color="#721417")

                            ]
                        ),
                        # botão
                        ft.Row(
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Container(
                                    bgcolor=ft.colors.PURPLE,
                                    padding=40,
                                    content=ft.Text("  "),
                                    border_radius=90,
                                    margin=ft.margin.only(bottom=50),
                                    on_click=lambda e: button_clicked(),
                                )
                            ]
                        )

                    ]
                ),
            )

        )

    def button_clicked():
        pagina()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "jogo do patinho"
    page.theme_mode = "light"
    page.bgcolor = ft.colors.BLACK

    titulo = ft.Text("Fortune Duck", size=50)

    pagina()


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
