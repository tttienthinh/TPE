from tkinter import *
from threading import Thread


class interface(Thread):

    def __init__(self):
        self.redefine_value()
        self.mainloop = False

        self.x, self.y, self.z = None, None, None

        self.bras = None
        self.yeux_change_bool = False
        self.myoware_1_change_bool = False
        self.myoware_2_change_bool = False
        self.myoware_1_pince_bool = False
        self.myoware_2_pince_bool = False
        self.running = False
        self.newdata_coordonnees = False
        self.newdata_pince = False
        self.mode_3D = True
        self.mode_RD = False
        self.mode_changed = False

        self.thread = True
        self.run()
        """Thread.__init__(self)
        self.start()"""

    def __del__(self):
        self.join()

    def run(self):
        self.fenetre = Tk()
        self.fenetre.title("3D")
        self.fenetre_x, self.fenetre_y = self.fenetre.winfo_screenwidth(), self.fenetre.winfo_screenheight()
        print("X = {}\nY = {}".format(self.fenetre_x, self.fenetre_y))
        # create EEG LabelFrame
        lf_eeg = LabelFrame(self.fenetre, text="EEG", padx=200, pady=42)
        lf_eeg.place(x=10, y=10)
        self.init_EEG(lf_eeg)

        # create EMG LabelFrame
        lf_emg = LabelFrame(self.fenetre, text="EMG", padx=200, pady=45)
        lf_emg.place(x=695, y=10)
        self.init_EMG(lf_emg)

        # create Run Refresh bouton
        self.init_RUN()
        #create finish button
        self.init_CLOSE()

        # create ARM LabelFrame
        lf_arm = LabelFrame(self.fenetre, borderwidth=3, text="Bras", padx=365, pady=70)
        lf_arm.place(x=10, y=350)
        self.init_ARM(lf_arm)

        # create choix d'utilisation
        lf_choix = LabelFrame(self.fenetre, borderwidth=3, text="Choix")
        lf_choix.place(x=1000, y=450)
        self.init_CHOIX(lf_choix)


        # Launch the WINDOW
        self.fenetre.geometry("{}x{}+0+0".format(self.fenetre_x, self.fenetre_y))
        self.fenetre.mainloop()
        self.thread = False
        print("outside")


    def init_EEG(self, lf_eeg):
        # signal frame
        self.eeg_frame_signal = Frame(lf_eeg, borderwidth=2, relief=FLAT)
        self.eeg_frame_signal.pack()
        # signal text
        self.eeg_signal_text = Label(self.eeg_frame_signal, text="Signal :", fg= "#34495E")
        self.eeg_signal_text.config(font=("Arial", 15))
        self.eeg_signal_text.pack(side=LEFT)
        # signal data
        self.eeg_signal_value = StringVar()
        self.eeg_signal_value.set("None")
        self.eeg_signal_data = Label(self.eeg_frame_signal, textvariable=self.eeg_signal_value, fg= "#34495E")
        self.eeg_signal_data.config(font=("Arial", 15))
        self.eeg_signal_data.pack()
        # attention frame
        self.eeg_frame_attention = Frame(lf_eeg, borderwidth=2, relief=FLAT)
        self.eeg_frame_attention.pack()
        # attention text
        self.eeg_attention_text = Label(self.eeg_frame_attention, text="Attention :", fg= "#34495E")
        self.eeg_attention_text.config(font=("Arial", 15))
        self.eeg_attention_text.pack(side=LEFT)
        # attention data
        self.eeg_attention_value = StringVar()
        self.eeg_attention_value.set("None")
        self.eeg_attention_data = Label(self.eeg_frame_attention, textvariable=self.eeg_attention_value, fg= "#34495E")
        self.eeg_attention_data.config(font=("Arial", 15))
        self.eeg_attention_data.pack()

        # meditation frame
        self.eeg_frame_meditation = Frame(lf_eeg, borderwidth=2, relief=FLAT)
        self.eeg_frame_meditation.pack()
        # meditation text
        self.eeg_meditation_text = Label(self.eeg_frame_meditation, text="Meditation :", fg= "#34495E")
        self.eeg_meditation_text.config(font=("Arial", 15))
        self.eeg_meditation_text.pack(side=LEFT)
        # meditation data
        self.eeg_meditation_value = StringVar()
        self.eeg_meditation_value.set("None")
        self.eeg_meditation_data = Label(self.eeg_frame_meditation, textvariable=self.eeg_meditation_value, fg= "#34495E")
        self.eeg_meditation_data.config(font=("Arial", 15))
        self.eeg_meditation_data.pack()

        # yeux frame
        self.eeg_frame_yeux = Frame(lf_eeg, borderwidth=2, relief=FLAT)
        self.eeg_frame_yeux.pack()
        # yeux text
        self.eeg_yeux_text = Label(self.eeg_frame_yeux, text="Yeux :", fg= "#34495E")
        self.eeg_yeux_text.config(font=("Arial", 15))
        self.eeg_yeux_text.pack(side=LEFT, fill="both")
        # yeux data
        self.eeg_yeux_value = StringVar()
        self.eeg_yeux_value.set("None")
        self.eeg_yeux_data = Label(self.eeg_frame_yeux, textvariable=self.eeg_yeux_value, fg= "#34495E")
        self.eeg_yeux_data.config(font=("Arial", 15))
        self.eeg_yeux_data.pack()
        # yeux changement fonction text
        #self.eeg_yeux_change_text = Label(self.eeg_frame_yeux, text="Use for")
        #self.eeg_yeux_change_text.pack(side=LEFT)
        # yeux changement data fonction

        #self.eeg_frame_buttonChangerAxe = Frame(self.eeg_frame_buttonChangerAxe, borderwidth=2, relief=FLAT)
        #self.eeg_frame_buttonChangerAxe.pack(side=RIGHT)
        self.eeg_yeux_change_button_color = StringVar()
        self.eeg_yeux_change_button_color.set("#D6DBDF")
        self.eeg_yeux_change_button = Button(lf_eeg, text="changer Axe", command=self.yeux_change, bg=self.eeg_yeux_change_button_color.get(), fg= "#34495E")
        self.eeg_yeux_change_button.place(x=140,y=105)
        # button to train
        self.eeg_yeux_train_button = Button(lf_eeg, text="Train Yeux", command=self.train_yeux, bg="#D6DBDF", fg= "#34495E")
        self.eeg_yeux_train_button.place(x=210,y=105)
        #Utilisation text

    def init_EMG(self, lf_emg):
        # myoware_1 frame
        self.emg_frame_myoware_1 = Frame(lf_emg, borderwidth=2, relief=FLAT)
        self.emg_frame_myoware_1.pack()
        # myoware_1 text
        self.emg_myoware_1_text = Label(self.emg_frame_myoware_1, text="Myoware 1 :", fg= "#34495E")
        self.emg_myoware_1_text.config(font=("Arial",15))
        self.emg_myoware_1_text.pack(side=LEFT)
        # myoware_1 data
        self.emg_myoware_1_value = StringVar()
        self.emg_myoware_1_value.set("None")
        self.emg_myoware_1_data = Label(self.emg_frame_myoware_1, textvariable=self.emg_myoware_1_value, fg= "#34495E")
        self.emg_myoware_1_data.config(font=("Arial", 15))
        self.emg_myoware_1_data.pack()

        """
        # myoware_1 changement fonction text
        self.myoware_1_change_text = Label(self.emg_frame_myoware_1, text="Use for")
        self.myoware_1_change_text.pack(side=LEFT)
        """
        # myoware_1 changement AXE data fonction
        #Déjà, création d'une frame pour les boutons
        self.myoware_1_buttons = Frame(lf_emg, borderwidth=2, relief=FLAT)
        self.myoware_1_change_button_color = StringVar()
        self.myoware_1_buttons.pack()
        self.myoware_1_change_button_color.set("#D6DBDF")
        self.myoware_1_change_button = Button(self.myoware_1_buttons, text="change Axe", command=self.myoware_1_change,
                                             bg=self.myoware_1_change_button_color.get(), fg= "#34495E")
        self.myoware_1_change_button.grid(row=2)
        # myoware_1 changement PINCE data fonction
        self.myoware_1_pince_button_color = StringVar()
        self.myoware_1_pince_button_color.set("#D6DBDF")
        self.myoware_1_pince_button = Button(self.myoware_1_buttons, text="hand", command=self.myoware_1_pince,
                                             bg=self.myoware_1_pince_button_color.get(), fg= "#34495E")
        self.myoware_1_pince_button.grid(row=2, column=1)


        # myoware_2 frame
        self.emg_frame_myoware_2 = Frame(lf_emg, borderwidth=2, relief=FLAT)
        self.emg_frame_myoware_2.pack()
        # myoware_2 text
        self.emg_myoware_2_text = Label(self.emg_frame_myoware_2, text="Myoware 2 :", fg= "#34495E")
        self.emg_myoware_2_text.config(font=("Arial", 15))
        self.emg_myoware_2_text.pack(side=LEFT)
        # myoware_2 data
        self.emg_myoware_2_value = StringVar()
        self.emg_myoware_2_value.set("None")
        self.emg_myoware_2_data = Label(self.emg_frame_myoware_2, textvariable=self.emg_myoware_2_value, fg="#34495E")
        self.emg_myoware_2_data.config(font=("Arial", 15))
        self.emg_myoware_2_data.pack()

        # myoware_2 changement fonction text
        #self.myoware_2_change_text = Label(self.emg_frame_myoware_2, text="Use for")
        #self.myoware_2_change_text.pack(side=LEFT)

        #Création frame pour les boutons :
        self.myoware_2_buttons = Frame(lf_emg, borderwidth=2)
        self.myoware_2_buttons.pack()
        # myoware_2 changement AXE data fonction
        self.myoware_2_change_button_color = StringVar()
        self.myoware_2_change_button_color.set("#D6DBDF")
        self.myoware_2_change_button = Button(self.myoware_2_buttons, text="change Axe", command=self.myoware_2_change,
                                              bg=self.myoware_2_change_button_color.get(), fg="#34495E")
        self.myoware_2_change_button.grid(row=2)
        # myoware_2 changement PINCE data fonction
        self.myoware_2_pince_button_color = StringVar()
        self.myoware_2_pince_button_color.set("#D6DBDF")
        self.myoware_2_pince_button = Button(self.myoware_2_buttons, text="hand", command=self.myoware_2_pince,
                                              bg=self.myoware_2_change_button_color.get(), fg="#34495E")
        self.myoware_2_pince_button.grid(row=2, column=1)

    def init_RUN(self):
        self.run_bouton_color = StringVar()
        self.run_bouton_color.set("#34495E")
        self.run_bouton = Button(self.fenetre, text="Lancer le programme", command=self.refresh, padx=100, fg=self.run_bouton_color.get())
        self.run_bouton.place(x=250, y=290)

    def init_CLOSE(self):
        self.run_bouton_deconnexion = Button(self.fenetre, text="Déconnexion", command=self.fenetre.quit, padx=100, fg= "#E53935")
        self.run_bouton_deconnexion.place(x=700, y=290)

    def init_ARM(self, lf_arm):
        # create Position LabelFrame
        lf_pos = Frame(lf_arm, relief=FLAT)
        lf_pos.pack(side=LEFT, padx=1, pady=2)


        #self.pos_frame_X = Frame(lf_pos, borderwidth=2, relief=FLAT)
        #self.pos_frame_X.grid(row=1)
        #Frame Axe+Incrementation
        """
        self.AxeIncrementation = Frame(lf_pos, borderwidth=2, relief=FLAT)
        self.AxeIncrementation.grid(row=1)
        """

        # X frame
        self.pos_frame_X = Frame(lf_pos, borderwidth=2, relief=FLAT)
        self.pos_frame_X.pack()
        # X text
        self.pos_X_text = Label(self.pos_frame_X, text="X :", fg="#34495E")
        self.pos_X_text.config(font=("Arial", 15))
        self.pos_X_text.grid(row=1,column=1)
        # X data
        self.pos_X_value = StringVar()
        self.pos_X_value.set("None")
        self.pos_X_data = Label(self.pos_frame_X, textvariable=self.pos_X_value, fg= "#34495E")
        self.pos_X_data.config(font=("Arial", 15))
        self.pos_X_data.grid(row=1,column=2)

        # Y frame
        self.pos_frame_Y = Frame(lf_pos, borderwidth=2, relief=FLAT)
        self.pos_frame_Y.pack()
        # Y text
        self.pos_Y_text = Label(self.pos_frame_Y, text="Y :", fg= "#34495E")
        self.pos_Y_text.config(font=("Arial", 15))
        self.pos_Y_text.grid(row=2,column=1)
        # Y data
        self.pos_Y_value = StringVar()
        self.pos_Y_value.set("None")
        self.pos_Y_data = Label(self.pos_frame_Y, textvariable=self.pos_Y_value, fg= "#34495E")
        self.pos_Y_data.config(font=("Arial", 15))
        self.pos_Y_data.grid(row=2,column=2)

        # Z frame
        self.pos_frame_Z = Frame(lf_pos, borderwidth=2, relief=FLAT)
        self.pos_frame_Z.pack()
        # Z text
        self.pos_Z_text = Label(self.pos_frame_Z, text="Z :", fg= "#34495E")
        self.pos_Z_text.config(font=("Arial", 15))
        self.pos_Z_text.grid(row=3,column=1)
        # Z data
        self.pos_Z_value = StringVar()
        self.pos_Z_value.set("None")
        self.pos_Z_data = Label(self.pos_frame_Z, textvariable=self.pos_Z_value, fg= "#34495E")
        self.pos_Z_data.config(font=("Arial", 15))
        self.pos_Z_data.grid(row=3,column=2)


        # Frame Commandes Directes
        self.CommandeDirecte = Frame(lf_arm, borderwidth=1, relief=FLAT)
        self.CommandeDirecte.pack(side=LEFT)

        # load X
        self.pos_X_load_value = StringVar()
        self.pos_X_load_value.set("X")
        self.pos_X_load = Entry(self.CommandeDirecte, textvariable=self.pos_X_load_value, fg= "#34495E")
        self.pos_X_load.config(font=("Arial", 15))
        self.pos_X_load.pack()
        # load Y
        self.pos_Y_load_value = StringVar()
        self.pos_Y_load_value.set("Y")
        self.pos_Y_load = Entry(self.CommandeDirecte, textvariable=self.pos_Y_load_value, fg= "#34495E")
        self.pos_Y_load.config(font=("Arial", 15))
        self.pos_Y_load.pack()
        # load Z
        self.pos_Z_load_value = StringVar()
        self.pos_Z_load_value.set("Z")
        self.pos_Z_load = Entry(self.CommandeDirecte, textvariable=self.pos_Z_load_value, fg= "#34495E")
        self.pos_Z_load.config(font=("Arial", 15))
        self.pos_Z_load.pack()
        # Check position button
        self.arm_check_pos_load = Button(self.CommandeDirecte, text="Envoyer position", command=self.arm_check_position)
        self.arm_check_pos_load.pack()


        #Frame Axe+Incrementation
        self.AxeIncrementation = Frame(lf_arm, borderwidth=2, relief=FLAT)
        self.AxeIncrementation.pack(side=RIGHT, padx=1, pady=1)
        # Axe frame
        self.arm_frame_Axe = Frame(self.fenetre, borderwidth=2, relief=GROOVE)
        self.arm_frame_Axe.pack(side=TOP)
        # Axe text
        self.arm_Axe_text = Label(self.arm_frame_Axe, text="Axe :", fg= "#34495E")
        self.arm_Axe_text.config(font=("Arial", 15))
        self.arm_Axe_text.grid(row=2,column=1)
        # Axe data
        self.arm_Axe_value = StringVar()
        self.arm_Axe_value.set("None")
        self.arm_Axe_data = Label(self.arm_frame_Axe, textvariable=self.arm_Axe_value, fg= "#34495E")
        self.arm_Axe_data.config(font=("Arial", 15))
        self.arm_Axe_data.grid(row=2,column=2)


        # Incrementation frame
        self.arm_frame_Incrementation = Frame(lf_arm, borderwidth=2, relief=FLAT)
        self.arm_frame_Incrementation.pack(side=RIGHT)
        # Incrementation text
        #self.arm_Incrementation_text = Label(self.arm_frame_Incrementation, text="Incrementation : ")
        #self.arm_Incrementation_text.config(font=("Arial",15))
        #self.arm_Incrementation_text.pack(side=LEFT)
        # Incrementation data
        self.text_incrementation = Label(self.arm_frame_Incrementation, text="Actual incrementation :", fg="#34495E")
        self.text_incrementation.config(font=("Arial", 15))
        self.text_incrementation.pack()
        self.value_incrementation = StringVar()
        self.value_incrementation.set("1")
        self.data_incrementation = Label(self.arm_frame_Incrementation, textvariable=self.value_incrementation, fg="#34495E")
        self.data_incrementation.config(font=("Arial", 15))
        self.data_incrementation.pack()

        self.arm_Incrementation_value = StringVar()
        self.arm_Incrementation_value.set("Modifier l'incrémentation")
        self.arm_Incrementation_data = Entry(self.arm_frame_Incrementation, textvariable=self.arm_Incrementation_value, fg= "#34495E")
        self.arm_Incrementation_data.config(font=("Arial",10))
        self.arm_Incrementation_data.pack()

        # Check Incrementation
        self.arm_check_incrementation = Button(self.arm_frame_Incrementation, text="Envoyer", command=self.arm_check_incrementation, fg= "#34495E")
        self.arm_check_incrementation.pack()

        # Check Incrementation
        self.arm_check_pince = Button(self.arm_frame_Incrementation, text="PINCE",
                                               command=self.arm_pince, fg="#34495E")
        self.arm_check_pince.pack()

    def init_CHOIX(self, lf_choix):
        self.button_3D_color = StringVar()
        self.button_3D_color.set("#239B56")
        self.button_3D = Button(lf_choix, text="3D", command=self.choix_3D,
                                              bg=self.button_3D_color.get(), fg="#34495E")
        self.button_3D.pack()

        self.button_RD_color = StringVar()
        self.button_RD_color.set("#D6DBDF")
        self.button_RD = Button(lf_choix, text="RD", command=self.choix_RD,
                                bg=self.button_RD_color.get(), fg="#34495E")
        self.button_RD.pack()


    def refresh(self):
        if self.thread == True:
            self.run_bouton_color.set("#66BB6A")
            self.run_bouton.configure(fg=self.run_bouton_color.get())
            self.running = True

    def redefine_value(self):
        # Define every variable
        self.eeg_attention_new_value = "None"
        self.eeg_meditation_new_value = "None"
        self.eeg_yeux_new_value = "None"
        self.eeg_signal_new_value = "None"

        self.emg_myoware_1_new_value = "None"
        self.emg_myoware_2_new_value = "None"

        self.arm_new_Axe_value = "X"

    # buttons to select change Axe and Pince
    def yeux_change(self):
        if self.yeux_change_bool:
            self.eeg_yeux_change_button_color.set("#D6DBDF")
            self.eeg_yeux_change_button.configure(bg=self.eeg_yeux_change_button_color.get())
            self.yeux_change_bool = False
        else:
            self.eeg_yeux_change_button_color.set("#239B56")
            self.eeg_yeux_change_button.configure(bg=self.eeg_yeux_change_button_color.get())
            self.yeux_change_bool = True

            if self.myoware_1_change_bool:
                self.myoware_1_change_button_color.set("#D6DBDF")
                self.myoware_1_change_button.configure(bg=self.myoware_1_change_button_color.get())
                self.myoware_1_change_bool = False

            if self.myoware_2_change_bool:
                self.myoware_2_change_button_color.set("#D6DBDF")
                self.myoware_2_change_button.configure(bg=self.myoware_2_change_button_color.get())
                self.myoware_2_change_bool = False

    def myoware_1_change(self):
        if self.myoware_1_change_bool:
                self.myoware_1_change_button_color.set("#D6DBDF")
                self.myoware_1_change_button.configure(bg=self.myoware_1_change_button_color.get())
                self.myoware_1_change_bool = False
        else:
            self.myoware_1_change_button_color.set("#239B56")
            self.myoware_1_change_button.configure(bg=self.myoware_1_change_button_color.get())
            self.myoware_1_change_bool = True

            if self.yeux_change_bool:
                self.eeg_yeux_change_button_color.set("#D6DBDF")
                self.eeg_yeux_change_button.configure(bg=self.eeg_yeux_change_button_color.get())
                self.yeux_change_bool = False

            if self.myoware_2_change_bool:
                self.myoware_2_change_button_color.set("#D6DBDF")
                self.myoware_2_change_button.configure(bg=self.myoware_2_change_button_color.get())
                self.myoware_2_change_bool = False

            if self.myoware_1_pince_bool:
                self.myoware_2_pince()

    def myoware_2_change(self):
        if self.myoware_2_change_bool:
            self.myoware_2_change_button_color.set("#D6DBDF")
            self.myoware_2_change_button.configure(bg=self.myoware_2_change_button_color.get())
            self.myoware_2_change_bool = False
        else:
            self.myoware_2_change_button_color.set("#239B56")
            self.myoware_2_change_button.configure(bg=self.myoware_2_change_button_color.get())
            self.myoware_2_change_bool = True

            if self.myoware_1_change_bool:
                self.myoware_1_change_button_color.set("#D6DBDF")
                self.myoware_1_change_button.configure(bg=self.myoware_1_change_button_color.get())
                self.myoware_1_change_bool = False

            if self.yeux_change_bool:
                self.eeg_yeux_change_button_color.set("#D6DBDF")
                self.eeg_yeux_change_button.configure(bg=self.eeg_yeux_change_button_color.get())
                self.yeux_change_bool = False

            if self.myoware_2_pince_bool:
                self.myoware_1_pince()

    def myoware_1_pince(self):
        if self.myoware_1_pince_bool:
            self.myoware_1_pince_button_color.set("#D6DBDF")
            self.myoware_1_pince_button.configure(bg=self.myoware_1_pince_button_color.get())
            self.myoware_1_pince_bool = False
        else:
            self.myoware_1_pince_button_color.set("#239B56")
            self.myoware_1_pince_button.configure(bg=self.myoware_1_pince_button_color.get())
            self.myoware_1_pince_bool = True

            if self.myoware_2_pince_bool:
                self.myoware_2_pince_button_color.set("#D6DBDF")
                self.myoware_2_pince_button.configure(bg=self.myoware_2_pince_button_color.get())
                self.myoware_2_pince_bool = False
            if self.myoware_1_change_bool:
                self.myoware_2_change()

    def myoware_2_pince(self):
        if self.myoware_2_pince_bool:
            self.myoware_2_pince_button_color.set("#D6DBDF")
            self.myoware_2_pince_button.configure(bg=self.myoware_2_pince_button_color.get())
            self.myoware_2_pince_bool = False
        else:
            self.myoware_2_pince_button_color.set("#239B56")
            self.myoware_2_pince_button.configure(bg=self.myoware_2_pince_button_color.get())
            self.myoware_2_pince_bool = True

            if self.myoware_1_pince_bool:
                self.myoware_1_pince_button_color.set("#D6DBDF")
                self.myoware_1_pince_button.configure(bg=self.myoware_1_pince_button_color.get())
                self.myoware_1_pince_bool = False
            if self.myoware_2_change_bool:
                self.myoware_1_change()


    # button position
    def arm_check_position(self):
        new_data = True
        try:
            self.x = float(self.pos_X_load_value.get())
        except:
            print("X was not float")
            new_data = False

        try:
            self.y = float(self.pos_Y_load_value.get())
        except:
            print("Y was not float")
            new_data = False

        try:
            self.z = float(self.pos_Z_load_value.get())
        except:
            print("Z was not float")
            new_data = False

        if new_data:
            print("{}  {}  {}".format(self.x, self.y, self.z))
            self.pos_X_value.set(self.x)
            self.pos_Y_value.set(self.y)
            self.pos_Z_value.set(self.z)
            self.newdata_coordonnees = True

    # button incrementation
    def arm_check_incrementation(self):
        newdata = True
        try:
            data = float(self.arm_Incrementation_value.get())
        except:
            newdata = False
            print("Incrementation must be a float.")

        if newdata:
            self.value_incrementation.set(str(data))
        self.arm_Incrementation_value.set("")

    # button pince
    def arm_pince(self):
        self.newdata_pince = True

    # buttons select mode utilisation
    def choix_3D(self):
        self.button_3D_color.set("#239B56")
        self.button_3D.configure(bg=self.button_3D_color.get())
        self.mode_3D = True

        if self.mode_RD:
            self.button_RD_color.set("#D6DBDF")
            self.button_RD.configure(bg=self.button_RD_color.get())
            self.mode_RD = False

        self.fenetre.title("3D")
        self.mode_changed = True

    def choix_RD(self):
        self.button_RD_color.set("#239B56")
        self.button_RD.configure(bg=self.button_RD_color.get())
        self.mode_RD = True

        if self.mode_3D:
            self.button_3D_color.set("#D6DBDF")
            self.button_3D.configure(bg=self.button_3D_color.get())
            self.mode_3D = False

        self.fenetre.title("RD")
        self.mode_changed = True

    # Machine learning
    def train_yeux(self):
        train_window = Toplevel()

        # affichage valeure actuelle
        self.train_text = Label(train_window, text="Limite :", fg="#34495E")
        self.train_text.config(font=("Arial", 15))
        self.train_text.pack()

        self.train_value = StringVar()
        self.train_value.set("95")
        self.train_data = Label(train_window, textvariable=self.train_value, fg="#34495E")
        self.train_data.config(font=("Arial", 15))
        self.train_data.pack()


        # Modification manuelle
        self.set_train_value = StringVar()
        self.set_train_value.set("Modifier l'incrémentation")
        self.set_train_data = Entry(train_window, textvariable=self.set_train_value,
                                             fg="#34495E")
        self.set_train_data.config(font=("Arial", 10))
        self.set_train_data.pack()
        # Check Incrementation
        self.set_train_check = Button(train_window, text="Envoyer",
                                               command=self.value_train_checker, fg="#34495E")
        self.set_train_check.pack()

        # Modification Machine Learning
        self.automatic_train = Button(train_window, text="Automatic Train",
                                      command=self.automatic_trainer, fg="#34495E")
        self.automatic_train.pack()

    def value_train_checker(self):
        newdata = True
        try:
            data = float(self.set_train_value.get())
        except:
            newdata = False
            print("Value must be a float.")

        if newdata:
            self.train_value.set(str(data))
        self.set_train_value.set("")

    def automatic_trainer(self):
        print("contracter")
        print("décontrater")







if __name__ == "__main__":
    interface()



