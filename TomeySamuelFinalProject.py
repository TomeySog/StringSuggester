"""Samuel Tomey
SDEV140 Final Project
String Suggester takes which guitar you play and your preferable string gauge to give you a generally good string set recomendation.
"""
#About 50 lines of actual code
import tkinter as tk
from tkinter import PhotoImage
from breezypythongui import EasyFrame

class StringReplacementAssistant(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="String Replacement Assistant")

        # Logo and header text
        self.logoImage = tk.PhotoImage(file="logo.png")  
        self.logoLabel = tk.Label(self, image=self.logoImage)
        self.logoLabel.grid(row=0, column=0, sticky="W")

        self.addLabel(text="Input your preferences and guitar type to get a popularly recommended string set.", row=1, column=0, columnspan=2, sticky="NSEW")

        # String Thickness drop down menu
        self.addLabel(text="Choose your string thickness:", row=2, column=0)
        self.stringThicknessVar = tk.StringVar(self)
        self.stringThicknessChoices = ["Light", "Medium", "Heavy"]
        self.stringThicknessMenu = tk.OptionMenu(self, self.stringThicknessVar, *self.stringThicknessChoices)
        self.stringThicknessMenu.grid(row=3, column=0)

        # Guitar Type drop down menu
        self.addLabel(text="Select your guitar type:", row=4, column=0)
        self.guitarTypeVar = tk.StringVar(self)
        self.guitarTypeChoices = ["Acoustic (six string)", "Electric (six string)", "Electric Bass (four string)"]
        self.guitarTypeMenu = tk.OptionMenu(self, self.guitarTypeVar, *self.guitarTypeChoices)
        self.guitarTypeMenu.grid(row=5, column=0)

        # Recommendation label for the text
        self.recommendationLabel = tk.Label(self, text="", fg="green")
        self.recommendationLabel.grid(row=6, column=0, columnspan=2, sticky="NSEW")

        # Placeholder for the recommendation image label
        self.recommendationImageLabel = tk.Label(self)
        self.recommendationImageLabel.grid(row=7, column=0, columnspan=2, sticky="NSEW")

        # Buttons and callbacks
        self.addButton(text="Get Recommendation", row=8, column=0, command=self.showRecommendation)
        self.addButton(text="Reset", row=8, column=1, command=self.resetSelections)
        self.addButton(text="Exit", row=8, column=2, command=self.quit)

    def showRecommendation(self):
        recommendation, image_file = self.get_recommendation(self.stringThicknessVar.get(), self.guitarTypeVar.get())
        if recommendation:
            # Display the recommendation text
            self.recommendationLabel.configure(text=recommendation)
            
            # Updating the recomendation placeholder image
            self.recommendationImage = tk.PhotoImage(file=image_file)
            self.recommendationImageLabel.configure(image=self.recommendationImage)
            self.recommendationImageLabel.image = self.recommendationImage
        else:
            self.recommendationLabel.configure(text="Please correct all selections.")
            self.recommendationImageLabel.configure(image="")

            # Output images
    def get_recommendation(self, string_thickness, guitar_type):
        recommendations = {
        ("Light", "Acoustic (six string)"): ("D'Addario EJ16 (.012-.053 gauge)", "DAddario_EJ16.png"),
        ("Medium", "Acoustic (six string)"): ("Ernie Ball Earthwood (.013-.056 gauge)", "ErnieBall_Earthwood.png"),
        ("Heavy", "Acoustic (six string)"): ("D'Addario EJ18 (.014-.059 gauge)", "DAddario_EJ18.png"),
        ("Light", "Electric (six string)"): ("D'Addario EXL120 (.009-.042 gauge)", "DAddario_EXL120.png"),
        ("Medium", "Electric (six string)"): ("Ernie Ball Regular Slinky (.010-.046 gauge)", "ErnieBall_RegularSlinky.png"),
        ("Heavy", "Electric (six string)"): ("Stringjoy Husky (.011-.052 gauge)", "Stringjoy_Husky.png"),
        ("Light", "Electric Bass (four string)"): ("Ernie Ball Extra Slinky (.040-.095 gauge)", "ErnieBall_ExtraSlinky.png"),
        ("Medium", "Electric Bass (four string)"): ("Elixir 14077 (.045-.105 gauge)", "Elixir_14077.png"),
        ("Heavy", "Electric Bass (four string)"): ("D'Addario EXL230 (.055-.110 gauge)", "DAddario_EXL230.png"),
    }
        return recommendations.get((string_thickness, guitar_type), (None, None))
    
    def resetSelections(self):
        # Reset the dropdown selection
        self.stringThicknessVar.set('')
        self.guitarTypeVar.set('')

if __name__ == "__main__":
    app = StringReplacementAssistant().mainloop()