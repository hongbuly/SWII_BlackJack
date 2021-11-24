
fight_message = ["You lose!", "You win!", "Draw!", "Congratulations! \nBlack Jack!", "Burst!"]
style_sheet = ["""QMessageBox
            {
            background-color: white;
            font-family: 'Georgia';
            }
            """,
               """QLabel

                           {
                           font-size: 18px;
                           font-family: 'Georgia';
                           color: blue;
                           }
                           """
               , """QLabel
            {
            font-size: 18px;
            font-family: 'Georgia';
            color: blue;
            }
            """,
               """QToolButton{background-color: rgb(249, 228, 183);
                           color: black;
                           border-radius: 5px;
                           font-family: 'Georgia';
                           font-size: 20px;
                           }"""
               """QToolButton::hover
               {
               background-color: white;
               }
               """
               ]