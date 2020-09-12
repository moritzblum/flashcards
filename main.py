import random

import tkinter as tk

import cards


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
        self.front = tk.Text(self, height=4, width=50, bg="grey")
        self.front.insert(tk.END, "")
        self.front.pack()

        tk.Label(self, text="Back:",).pack()
        self.back = tk.Text(self, height=4, width=50, bg="grey")
        self.back.insert(tk.END, "")
        self.back.pack()

        tk.Button(self, text="add", command=lambda: self.add()).pack()
        tk.Button(self, text="to start page", command=lambda: master.switch_frame(StartPage)).pack()

    def add(self):
        front = self.front.get(1.0, tk.END)
        back = self.back.get(1.0, tk.END)
        self.card_manager.create_card(front, back)
        self.front.delete(1.0, tk.END)
        self.back.delete(1.0, tk.END)


class Train(tk.Frame):
    def __init__(self, master, card_manager):
        self.card_manager = card_manager
        self.current_card = random.choice(card_manager.cards)

        tk.Frame.__init__(self, master)
        tk.Label(self, text="Train",).pack()


        tk.Label(self, text="Front:",).pack()
        self.front = tk.Text(self, height=4, width=50, bg="grey")
        self.front.insert(tk.END, self.current_card[0])
        self.front.pack()

        tk.Label(self, text="Answer:", ).pack()
        self.user_input = tk.Text(self, height=4, width=50, bg="grey")
        self.user_input.insert(tk.END, "")
        self.user_input.pack()

        tk.Label(self, text="Solution:").pack()
        self.back = tk.Text(self, height=4, width=50)
        self.back.insert(tk.END, "")
        self.back.pack()

        tk.Button(self, text="show", command=lambda: self.back.insert(tk.END, self.current_card[1])).pack()
        tk.Button(self, text="right", command=lambda: self.next_card(True)).pack()
        tk.Button(self, text="wrong", command=lambda: self.next_card(False)).pack()
        tk.Button(self, text="to start page", command=lambda: master.switch_frame(StartPage)).pack()

    def next_card(self, right):
        # clear text fields
        self.front.delete(1.0, tk.END)
        self.user_input.delete(1.0, tk.END)
        self.back.delete(1.0, tk.END)

        # if answer right, don't show this card again in this session
        if right:
            card_manager.cards.remove(self.current_card)

        # sample new card
        if len(card_manager.cards) > 0:
            self.current_card = random.choice(card_manager.cards)
            self.front.insert(tk.END, self.current_card[0])


if __name__ == "__main__":
    card_manager = cards.CardManager()
    app = Flashcards(card_manager)
    app.mainloop()