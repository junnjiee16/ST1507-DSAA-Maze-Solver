from application import Application

app = Application("PIZZA RUNNERS", "Lim Jun Jie, Timothy Chia", "DAAA/FT/2B/02")

if __name__ == "__main__":
    app.useFile("test_files/map1.txt")
    app.startProgram(700, 500)
