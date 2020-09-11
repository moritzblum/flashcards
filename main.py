import tkinter as tk


class Flashcards(tk.Tk):

    def __init__(self, card_manager):
        tk.Tk.__init__(self)
        self.card_manager = card_manager

        self._frame = None
        self.switch_frame(StartPage)


    def switch_frame(self, frame_class):
        new_frame = frame_class(self, self.card_manager)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master, card_manager):
        self.card_manager = card_manager

        tk.Frame.__init__(self, master)
        tk.Label(self, text="Flashcards").pack()
        tk.Button(self, text="Add Cards",
                  command=lambda: master.switch_frame(Add_Cards)).pack()
        tk.Button(self, text="Train",
                  command=lambda: master.switch_frame(Train)).pack()

class Add_Cards(tk.Frame):
    def __init__(self, master, card_manager):
        self.card_manager = card_manager

        tk.Frame.__init__(self, master)
        tk.Label(self, text="Add Cards",).pack()

        tk.Label(self, text="Front:",).pack()
        front = tk.Text(self, height=4, width=50)
        front.insert(tk.END, "")
        front.pack()

        tk.Label(self, text="Back:",).pack()
        back = tk.Text(self, height=4, width=50)
        back.insert(tk.END, "")
        back.pack()

        tk.Button(self, text="add", command=lambda: self.card_manager.create_card()).pack()
        tk.Button(self, text="to start page", command=lambda: master.switch_frame(StartPage)).pack()




class Train(tk.Frame):
    def __init__(self, master, card_manager):
        self.card_manager = card_manager

        tk.Frame.__init__(self, master)
        tk.Label(self, text="Train").pack()
        tk.Button(self, text="to start page", command=lambda: master.switch_frame(StartPage)).pack()



class Card_Manager():
    def __init__(self):
        pass

    def create_card(self):
        print("card created")

if __name__ == "__main__":
    card_manager = Card_Manager()

    app = Flashcards(card_manager)
    app.mainloop()