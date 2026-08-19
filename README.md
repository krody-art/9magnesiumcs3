zodiac = int(input("Enter your birth year: "))
if zodiac <= 1800:
    print("Invalid year. Please enter a year after 1800.")

else:
    zodiac_animals = ["Monkey (猴 / Hóu)", "Rooster  (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig  (猪 / Zhū)", "Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)"]
    year_of_user = (zodiac - 1800) % 12
    print("Your Chinese Zodiac sign is:", zodiac_animals[year_of_user])