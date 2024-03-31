import threading
import PIL
import customtkinter
import sorting


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class ToplevelWindow0(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x500")

        ImageHome0 = customtkinter.CTkImage(dark_image=PIL.Image.open("Assets\ImgOfMe.png"), size=(150, 160))

        self.label0 = customtkinter.CTkLabel(self, text="DEVELOPER PROFILE: ",   font=customtkinter.CTkFont(family="IBM Plex Sans", size=20))
        self.label0.place(x=40, y=20)

        self.Frame0Img0 = customtkinter.CTkLabel(self,
                                                 text=" ",
                                                 image=ImageHome0,
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=25),
                                                 fg_color="white",
                                                 corner_radius=5)
        self.Frame0Img0.place(x=50, y=90)

        self.label1 = customtkinter.CTkLabel(self, text="Name: Rizvi Ahmed Abbas ",
                                            font=customtkinter.CTkFont(family="IBM Plex Sans", size=18))
        self.label1.place(x=280, y=90)
        self.label1 = customtkinter.CTkLabel(self, text="Age: 20",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=15))
        self.label1.place(x=280, y=120)
        self.label1 = customtkinter.CTkLabel(self, text="Engineer: Software Engineering",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=15))
        self.label1.place(x=280, y=150)
        self.label1 = customtkinter.CTkLabel(self, text="Domain: Full-Stack Web Development,",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=15))
        self.label1.place(x=280, y=180)
        self.label1 = customtkinter.CTkLabel(self, text="Mobile Developments, AI&ML",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=15))
        self.label1.place(x=280, y=200)


        self.textbox = customtkinter.CTkTextbox(self, width=500, height=150)
        self.textbox.grid(row=0, column=1, padx=(50, 0), pady=(300, 0), sticky="nsew")
        self.textbox.insert("0.0",
                            "About MySelf\n\n" + "Hello, My Name is Rizvi Ahmed Abbas im a student of Computer "
                                                 "Engieering in PVPPCOE college, im a developer and Leader of this "
                                                 "project, our project is Based on AI Machine Vision (is Subset of "
                                                 "Machine Learning) This NexTech Hackathon Project is a All-rounder "
                                                 "AI Machine vision modules (Application)That is Integrated in One "
                                                 "Desktop Application, The goal of this Project is to integrated all "
                                                 "Vision program into one application, All Vision program can be use "
                                                 "in on Application \n\n")
        self.textbox.configure(state="disabled")  # configure textbox to be read-only



class ToplevelWindow1(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x500")

        ImageHome0 = customtkinter.CTkImage(dark_image=PIL.Image.open("Assets/adv_pic.png"), size=(150, 160))

        self.label0 = customtkinter.CTkLabel(self, text="DEVELOPER PROFILE: ",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=20))
        self.label0.place(x=40, y=20)

        self.Frame0Img0 = customtkinter.CTkLabel(self,
                                                 text=" ",
                                                 image=ImageHome0,
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=25),
                                                 fg_color="white",
                                                 corner_radius=5)
        self.Frame0Img0.place(x=50, y=90)

        self.label1 = customtkinter.CTkLabel(self, text="Name: Advaitya Jadhav",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=18))
        self.label1.place(x=280, y=90)
        self.label1 = customtkinter.CTkLabel(self, text="Age: 20 ",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=15))
        self.label1.place(x=280, y=120)
        self.label1 = customtkinter.CTkLabel(self, text="Engineer: Software Engineering",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=15))
        self.label1.place(x=280, y=150)
        self.label1 = customtkinter.CTkLabel(self, text="Domain: Full-Stack Development on Desktop/Android applications,",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=15))
        self.label1.place(x=280, y=180)
        self.label1 = customtkinter.CTkLabel(self, text="Game developer, AI & ML",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=15))
        self.label1.place(x=280, y=200)

        self.textbox = customtkinter.CTkTextbox(self, width=500, height=150)
        self.textbox.grid(row=0, column=1, padx=(50, 0), pady=(300, 0), sticky="nsew")
        self.textbox.insert("0.0",
                            "About MySelf\n\n" + "Hello, I'm a developer My name is Advaitya Jadhav, student of Computer"
                                                 "Engieering in PVPPCOE college, im a developer and Leader of this "
                                                 "project, our project is Based on AI Machine Vision (is Subset of "
                                                 "Machine Learning) This NexTech Hackathon Project is a All-rounder "
                                                 "AI Machine vision modules (Application)That is Integrated in One "
                                                 "Desktop Application, The goal of this Project is to integrated all "
                                                 "Vision program into one application, All Vision program can be use "
                                                 "in on Application \n\n")
        self.textbox.configure(state="disabled")  # configure textbox to be read-only


class ToplevelWindow2(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x500")

        ImageHome0 = customtkinter.CTkImage(dark_image=PIL.Image.open("Assets\Cubiad.png"), size=(150, 160))


        self.label0 = customtkinter.CTkLabel(self, text="DEVELOPER PROFILE: ",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=20))
        self.label0.place(x=40, y=20)

        self.Frame0Img0 = customtkinter.CTkLabel(self,
                                                 text=" ",
                                                 image=ImageHome0,
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=25),
                                                 fg_color="white",
                                                 corner_radius=5)
        self.Frame0Img0.place(x=50, y=90)

        self.label1 = customtkinter.CTkLabel(self, text="Name: Ubaid Mukadam",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=18))
        self.label1.place(x=280, y=90)
        self.label1 = customtkinter.CTkLabel(self, text="Age: 18 ",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=15))
        self.label1.place(x=280, y=120)
        self.label1 = customtkinter.CTkLabel(self, text="Engineer: Software Engineering",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=15))
        self.label1.place(x=280, y=150)
        self.label1 = customtkinter.CTkLabel(self, text="Domain: Full-Stack Web Development,",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=15))
        self.label1.place(x=280, y=180)
        self.label1 = customtkinter.CTkLabel(self, text="Mobile Developments, AI&ML",
                                             font=customtkinter.CTkFont(family="IBM Plex Sans", size=15))
        self.label1.place(x=280, y=200)

        self.textbox = customtkinter.CTkTextbox(self, width=500, height=150)
        self.textbox.grid(row=0, column=1, padx=(50, 0), pady=(300, 0), sticky="nsew")
        self.textbox.insert("0.0",
                            "About MySelf\n\n" + "Hello, My Name is Ubaid Mukadam im a student of Computer Engieering"
                                                 "in Abdul Razzak Kalsekar, im a developer and Member of this project "
                                                 "our project is Based on AI Machine Vision (is Subset of Machine Learning) "
                                                 "This Diloma Final Year Project is a All-rounder AI Machien vision modules (Appliaction"
                                                 ")That is Integrated in One Desktop Application, The goal of this Project"
                                                 "is to integrated all Visison program into one appliaction, All Vision program"
                                                 "can be use in on Appliocation\n\n")
        self.textbox.configure(state="disabled")  # configure textbox to be read-only


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.toplevel_window0 = None
        self.toplevel_window1 = None
        self.toplevel_window2 = None
        self.title("AI Machine Vision")
        self.geometry(f"{1100}x{580}")
        # Icon for TopLevel Window
        # self.after(201, lambda: self.iconbitmap("logo2.png"))

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # images
        ImageHome0 = customtkinter.CTkImage(dark_image=PIL.Image.open("Assets\AIExapmple.png"), size=(350, 280))
        ImageHome1 = customtkinter.CTkImage(dark_image=PIL.Image.open("Assets\insertionsort.png"), size=(350, 240))
        ImageHome1_1 = customtkinter.CTkImage(dark_image=PIL.Image.open("Assets\Bubble.png"), size=(300, 180))
        ImageHome2 = customtkinter.CTkImage(dark_image=PIL.Image.open("Assets\VirtualK.jpg"), size=(350, 280))
        ImageHome3 = customtkinter.CTkImage(dark_image=PIL.Image.open("Assets\Presentation.png"), size=(350, 240))
        ImageHome4 = customtkinter.CTkImage(dark_image=PIL.Image.open("Assets\quick.png"), size=(350, 240))
        ImageHome5 = customtkinter.CTkImage(dark_image=PIL.Image.open("Assets\Selection.png"), size=(350, 240))

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Developers",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.open_toplevel0,
                                                        text="Rizvi Ahmed Abbas")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.open_toplevel1,
                                                        text="Advaitya Jadhav")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        # self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.open_toplevel2,
        #                                                 text="Devepoler")
        # self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # TabsView
        self.Pages = customtkinter.CTkTabview(self, width=895, height=565,
                                              fg_color=("#bdbdc1", "#29292a"),
                                              corner_radius=15)  # 262628 alternate Color
        self.Pages.add(" Home ")
        self.Pages.add(" Insertion Sort ")
        self.Pages.add(" Bubble Sort ")
        self.Pages.add(" Quick Sort ")
        self.Pages.add(" Selection Sort ")
        self.Pages.place(x=190, y=3)
        self.Pages._segmented_button.grid(sticky="W")

        # TextBox Home
        self.textbox0 = customtkinter.CTkTextbox(self.Pages.tab(" Home "), width=370, height=180)
        self.textbox0.grid(row=0, column=1, padx=(480, 0), pady=(20, 0), sticky="nsew")
        self.textbox0.insert("0.0",
                            "About This Project\n\n" + "Our project is Based on AI Machine Vision (is Subset of Machine Learning) "
                                                 "This Diloma Final Year Project is a All-rounder AI Machien vision modules (Appliaction"
                                                 ")That is Integrated in One Desktop Application, The goal of this Project"
                                                 "is to integrated all Visison program into one appliaction, All Vision program"
                                                 "can be use in on Appliocation \n\n")
        self.textbox0.configure(state="disabled")  # configure textbox to be read-only

        # Labels Home Page
        self.HomeLabel0 = customtkinter.CTkLabel(self.Pages.tab(" Home "), text="Sorting ",
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=90),
                                                 fg_color="white", text_color="black", corner_radius=10)
        self.HomeLabel0.place(x=50, y=46)

        self.HomeLabel1 = customtkinter.CTkLabel(self.Pages.tab(" Home "), text="Visualizer",
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=30),
                                                 corner_radius=10)
        self.HomeLabel1.place(x=220, y=150)

        self.HomeLabel2 = customtkinter.CTkLabel(self.Pages.tab(" Home "), text=" Sorting Algorithm.",
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=40),
                                                 corner_radius=0)
        self.HomeLabel2.place(x=5, y=280)

        self.HomeLabel3 = customtkinter.CTkLabel(self.Pages.tab(" Home "),
                                                 text="All Sorting Algorithm"
                                                      "are Integrated in one Application. ",
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=19),
                                                 corner_radius=0)
        self.HomeLabel3.place(x=15, y=360)

        self.HomeLabel3 = customtkinter.CTkLabel(self.Pages.tab(" Home "),
                                                 text="Different Sorting Alogrithm Program Such as Insertion, Selection, Quick, and Bubble Sorting",
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=15),
                                                 corner_radius=0)
        self.HomeLabel3.place(x=15, y=395)
        self.HomeLabel4 = customtkinter.CTkLabel(self.Pages.tab(" Home "),
                                                 text="This Application, This App is Very User Friendly and easily "
                                                      "Understood by the User "
                                                      ",User can Start Different Modules of AI",
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=15),
                                                 corner_radius=0)
        self.HomeLabel4.place(x=15, y=420)
        self.HomeLabel5 = customtkinter.CTkLabel(self.Pages.tab(" Home "),
                                                 text="Sorting Visualizer"
                                                      "Appliaction(Progarms).",
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=15),
                                                 corner_radius=0)
        self.HomeLabel5.place(x=15, y=445)
        ################################Home###########################

        # Label Trainer
        self.HomeLabel__2 = customtkinter.CTkLabel(self.Pages.tab(" Insertion Sort "),
                                                 text=" Inserting Sorting ",
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=27),
                                                 corner_radius=0)
        self.HomeLabel__2.place(x=20, y=5)

        # Image Trainer
        self.HomeLabel__3 = customtkinter.CTkLabel(self.Pages.tab(" Insertion Sort "),
                                                 text=" ",
                                                 image=ImageHome1,
                                                 font=customtkinter.CTkFont(family="IBM Plex Sans", size=25),
                                                 corner_radius=0)
        self.HomeLabel__3.place(x=20, y=90)

        # Desktop Trainer
        self.button__1 = customtkinter.CTkButton(self.Pages.tab(" Insertion Sort "),
                                                corner_radius=100,
                                                text="Start",
                                                command=self.open_SitsUpsApp)
        self.button__1.place(x=110, y=350)


        # TextBox Trainer
        self.textbox2 = customtkinter.CTkTextbox(self.Pages.tab(" Insertion Sort "), width=350, height=240)
        self.textbox2 = customtkinter.CTkTextbox(self.Pages.tab(" Insertion Sort "), width=350, height=240)
        self.textbox2.grid(row=0, column=1, padx=(500, 0), pady=(20, 0), sticky="nsew")
        self.textbox2.insert("0.0",
                            "About This Project\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "
                                                       "sed diam nonumy eirmod tempor invidunt ut labore et dolore "
                                                       "magna aliquyam erat, sed diam voluptua.\n\n")
        self.textbox2.configure(state="disabled")  # configure textbox to be read-only
        ####################Trainer################

        # Label Trainer
        self.HomeLabel__2 = customtkinter.CTkLabel(self.Pages.tab(" Bubble Sort "),
                                                   text="Bubble Sorting",
                                                   font=customtkinter.CTkFont(family="IBM Plex Sans", size=27),
                                                   corner_radius=0)
        self.HomeLabel__2.place(x=20, y=5)

        # Image Trainer
        self.HomeLabel__3 = customtkinter.CTkLabel(self.Pages.tab(" Bubble Sort "),
                                                   text=" ",
                                                   image=ImageHome1_1,
                                                   font=customtkinter.CTkFont(family="IBM Plex Sans", size=25),
                                                   corner_radius=0)
        self.HomeLabel__3.place(x=20, y=90)

        # Desktop Trainer
        self.button__1 = customtkinter.CTkButton(self.Pages.tab(" Bubble Sort "),
                                                 corner_radius=100,
                                                 text="Start",
                                                 command=self.open_Biceps_PushApp)
        self.button__1.place(x=110, y=350)

        # TextBox Trainer
        self.textbox2 = customtkinter.CTkTextbox(self.Pages.tab(" Bubble Sort "), width=350, height=240)
        self.textbox2 = customtkinter.CTkTextbox(self.Pages.tab(" Bubble Sort "), width=350, height=240)
        self.textbox2.grid(row=0, column=1, padx=(500, 0), pady=(20, 0), sticky="nsew")
        self.textbox2.insert("0.0",
                             "About This Project\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "
                                                        "sed diam nonumy eirmod tempor invidunt ut labore et dolore "
                                                        "magna aliquyam erat, sed diam voluptua.\n\n")
        self.textbox2.configure(state="disabled")  # configure textbox to be read-only
        ####################Trainer################


    # Hand Sign
        # Label Presentation Controller
        self.HomeLabel___0 = customtkinter.CTkLabel(self.Pages.tab(" Quick Sort "),
                                                   text=" Quick Sorting ",
                                                   font=customtkinter.CTkFont(family="IBM Plex Sans", size=27),
                                                   corner_radius=0)
        self.HomeLabel___0.place(x=20, y=5)

        # Image Presentation Controller
        self.HomeLabel___1 = customtkinter.CTkLabel(self.Pages.tab(" Quick Sort "),
                                                   text=" ",
                                                   image=ImageHome4,
                                                   font=customtkinter.CTkFont(family="IBM Plex Sans", size=25),
                                                   corner_radius=0)
        self.HomeLabel___1.place(x=20, y=90)

        # Desktop Presentation Controller
        self.button____0 = customtkinter.CTkButton(self.Pages.tab(" Quick Sort "),
                                                 corner_radius=100,
                                                 text="Start",
                                                 command=self.open_HandSignDectectionApplication)
        self.button____0.place(x=110, y=400)

        # TextBox Presentation Controller
        self.textbox_0 = customtkinter.CTkTextbox(self.Pages.tab(" Quick Sort "), width=350, height=240)
        self.textbox_0 = customtkinter.CTkTextbox(self.Pages.tab(" Quick Sort "), width=350, height=240)
        self.textbox_0.grid(row=0, column=1, padx=(500, 0), pady=(20, 0), sticky="nsew")
        self.textbox_0.insert("0.0",
                             "About This Project\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "
                                                        "sed diam nonumy eirmod tempor invidunt ut labore et dolore "
                                                        "magna aliquyam erat, sed diam voluptua.\n\n")
        self.textbox_0.configure(state="disabled")  # configure textbox to be read-only

    # #######$$########

    ### Word

        # Hand Sign
        # Label Presentation Controller
        self.WordHomeLabel___0 = customtkinter.CTkLabel(self.Pages.tab(" Selection Sort "),
                                                    text=" Selection Sorting ",
                                                    font=customtkinter.CTkFont(family="IBM Plex Sans", size=27),
                                                    corner_radius=0)
        self.WordHomeLabel___0.place(x=20, y=5)

        # Image Presentation Controller
        self.WordHomeLabel___1 = customtkinter.CTkLabel(self.Pages.tab(" Selection Sort "),
                                                    text=" ",
                                                    image=ImageHome5,
                                                    font=customtkinter.CTkFont(family="IBM Plex Sans", size=25),
                                                    corner_radius=0)
        self.WordHomeLabel___1.place(x=20, y=90)

        # Desktop Presentation Controller
        self.WordButton____0 = customtkinter.CTkButton(self.Pages.tab(" Selection Sort "),
                                                       corner_radius=100,
                                                       text="Start",
                                                       command=self.open_HandSignWordDectectionApplication)
        self.WordButton____0.place(x=110, y=400)

        # TextBox Presentation Controller
        self.WordTextbox_0 = customtkinter.CTkTextbox(self.Pages.tab(" Selection Sort "), width=350, height=240)
        self.WordTextbox_0 = customtkinter.CTkTextbox(self.Pages.tab(" Selection Sort "), width=350, height=240)
        self.WordTextbox_0.grid(row=0, column=1, padx=(500, 0), pady=(20, 0), sticky="nsew")
        self.WordTextbox_0.insert("0.0",
                              "About This Project\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "
                                                         "sed diam nonumy eirmod tempor invidunt ut labore et dolore "
                                                         "magna aliquyam erat, sed diam voluptua.\n\n")
        self.WordTextbox_0.configure(state="disabled")  # configure textbox to be read-only

    # #######$$########'''

    # Methods
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def open_toplevel0(self):
        if self.toplevel_window0 is None or not self.toplevel_window0.winfo_exists():
            self.toplevel_window0 = ToplevelWindow0(self)  # create window if its None or destroyed
            self.toplevel_window0.grab_set()

    def open_toplevel1(self):
        if self.toplevel_window1 is None or not self.toplevel_window1.winfo_exists():
            self.toplevel_window1 = ToplevelWindow1(self)  # create window if its None or destroyed
            self.toplevel_window1.grab_set()


    def open_SitsUpsApp(self):
        g = sorting.main(1)
        t = threading.Thread(target=g.start)
        t.start()
    def open_Biceps_PushApp(self):
        g = sorting.main(2)
        t = threading.Thread(target=g.start)
        t.start()

    def open_HandSignDectectionApplication(self):
        g = sorting.main(3)
        t = threading.Thread(target=g.start)
        t.start()

    def open_HandSignWordDectectionApplication(self):
        g = sorting.main(4)
        t = threading.Thread(target=g.start)
        t.start()

if __name__ == "__main__":
    app = App()
    app.mainloop()
