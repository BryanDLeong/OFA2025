"""name = input("type a name? ")
name = name[0].upper()+ name[1:len(name)]
showers = int(input("how many showers have you taken per week? "))
avg_showertime = float(input("What is your average shower time? "))
meals = int(input("how many meals have you eaten per week? "))
water_Waste = (showers*avg_showertime)*2
print(fr'''{name +"'s"} enviormental impact: 
    Water waste: {water_Waste} gallons
    Food waste: {meals}
    Total: {water_Waste+meals}''')"""

questions = [input("type a name? "), 
             int(input("how many showers have you taken per week? ")), 
             float(input("What is your average shower time? ")),
             int(input("how many meals have you eaten per week? ")),
             float(input("How many miles do you drive weekly? "))]

name = questions[0][0].upper()+ questions[0][1:len(questions[0])]

water_Waste = (questions[1]*questions[2])*2

meals = questions[3]
food_waste = meals*0.5

miles = questions[4]
co2_waste = miles*4

print(fr'''{name +"'s"} enviormental impact: 
    Water waste: {water_Waste} gallons 💧
    Food waste: {food_waste}lbs 🍔
    CO2 waste: {co2_waste} grams 🚗
    Total: {water_Waste+meals+co2_waste}''')

print(r'''
                _-o#&&*''?d:>b\_
          _o/"`''  '',, dMF9MMMMMHo_
       .o&#'        `"MbHMMMMMMMMMMMHo.
     .o"" '         vodM*$&&HMMMMMMMMMM?.
    ,'              $M&ood,~'`(&##MMMMMMH\
   /               ,MMMMMMM#b?#bobMMMMHMMML
  &              ?MMMMMMMMMMMMMMMMM7MMM$R*Hk
 ?$.            :MMMMMMMMMMMMMMMMMMM/HMMM|`*L
|               |MMMMMMMMMMMMMMMMMMMMbMH'   T,
$H#:            `*MMMMMMMMMMMMMMMMMMMMb#}'  `?
]MMH#             ""*""""*#MMMMMMMMMMMMM'    -
MMMMMb_                   |MMMMMMMMMMMP'     :
HMMMMMMMHo                 `MMMMMMMMMT       .
?MMMMMMMMP                  9MMMMMMMM}       -
-?MMMMMMM                  |MMMMMMMMM?,d-    '
 :|MMMMMM-                 `MMMMMMMT .M|.   :
  .9MMM[                    &MMMMM*' `'    .
   :9MMk                    `MMM#"        -
     &M}                     `          .-
      `&.                             .
        `~,   .                     ./
            . _                  .-
              '`--._,dd###pp=""''')
