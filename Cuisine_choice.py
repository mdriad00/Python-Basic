#Here is the some famous cuisines from different countries
italian = ["Spaghetti Carbonara", "Margherita Pizza", "Risotto alla Milanese", "Lasagna", "Tiramisu", "Bruschetta", "Caprese Salad", "Osso Buco", "Prosciutto e Melone", "Gelato", "Fettuccine Alfredo", "Cannoli", "Panettone", "Minestrone Soup", "Panna Cotta", "Parmigiana", "Ravioli", "Bolognese Sauce", "Arancini", "Pesto Sauce"]
french = ["Coq au Vin", "Croissant", "Escargot", "Crème Brûlée", "Baguette", "Quiche Lorraine", "Bouillabaisse", "Ratatouille", "Foie Gras", "Crepes", "French Onion Soup", "Bœuf Bourguignon", "Macarons", "Duck Confit", "Tarte Tatin", "Pâté", "Niçoise Salad", "Moules Marinières", "Brie Cheese", "Éclair"]
chinese = ["Kung Pao Chicken", "Peking Duck", "Dim Sum", "Sweet and Sour Pork", "Spring Rolls", "Ma Po Tofu", "General Tso's Chicken", "Hotpot", "Dumplings", "Chow Mein", "Mapo Doufu", "Egg Fried Rice", "Shrimp Wonton Soup", "Baozi (Steamed Buns)", "Sichuan Hotpot", "Char Siu (Barbecued Pork)", "Xiaolongbao (Soup Dumplings)", "Congee", "Yangzhou Fried Rice", "Peking Duck"]
japanese = ["Sushi", "Sashimi", "Tempura", "Ramen", "Udon", "Miso Soup", "Yakitori", "Tonkatsu", "Sukiyaki", "Takoyaki", "Okonomiyaki", "Gyoza", "Unagi", "Matcha", "Mochi", "Nigiri", "Onigiri", "Shabu-Shabu", "Chawanmushi", "Soba"]
nepalese = ["Momos", "Dal Bhat", "Gundruk", "Sel Roti", "Yomari", "Newari Bara", "Dhido", "Kwati", "Sekuwa", "Gurkha Curry", "Thukpa", "Chatamari", "Aloo Tama", "Samay Baji", "Sukuti", "Tongba", "Sikarni", "Juju Dhau", "Phapar Ko Roti", "Kachila"]
american = ["Burger and Fries", "Hot Dog", "Apple Pie", "Buffalo Wings", "Clam Chowder", "Barbecue Ribs", "Cheeseburger", "Chocolate Chip Cookies", "Pulled Pork Sandwich", "Cornbread", "New York-Style Pizza", "Chili", "Reuben Sandwich", "Key Lime Pie", "Philly Cheesesteak", "Donuts", "Fried Chicken", "Biscuits and Gravy", "Tater Tots", "Pancakes"]
thai = ["Tom Yum Goong", "Pad Thai", "Green Curry", "Massaman Curry", "Som Tum (Papaya Salad)", "Pad See Ew", "Tom Kha Gai", "Khao Pad (Fried Rice)", "Tom Klong Pla Grab", "Panang Curry", "Pad Kra Pao (Basil Stir-Fry)", "Yam Nua (Spicy Beef Salad)", "Kai Med Ma Muang (Cashew Chicken)", "Gaeng Keow Wan Gai (Green Curry Chicken)", "Som Tum Thai", "Khao Soi", "Moo Pad Krapow", "Pla Rad Prik (Fried Fish with Chili Sauce)", "Gai Pad Pongali", "Kao Pad Nam Prik Kapi"]
german = ["Bratwurst", "Sauerkraut", "Pretzel", "Wiener Schnitzel", "Black Forest Cake", "Sauerbraten", "Kartoffelsalat" , "Apfelstrudel", "Currywurst", "Rouladen", "Bretzel" , "Kartoffelsuppe" , "Eisbein" , "Lebkuchen", "Spätzle", "Weisswurst", "Haxen" , "Königsberger Klopse" , "Schwarzbrot" , "Labskaus"]
turkish = ["Kebab", "Baklava", "Turkish Delight", "Doner Kebab", "Meze", "Pide", "Manti", "Lahmacun", "Iskender Kebab", "Kumpir", "Gozleme", "Simit", "Çılbır", "Karnıyarık", "Menemen", "Meyhane", "Pilaf", "Kofte", "Borek", "Raki"]
indonesian = ["Nasi Goreng", "Rendang", "Sate Ayam", "Nasi Padang", "Gado-Gado", "Bakso", "Soto Ayam", "Nasi Uduk", "Nasi Kuning", "Sambal Terasi", "Ayam Betutu", "Pisang Goreng", "Nasi Campur", "Sop Buntut", "Martabak Manis", "Babi Guling", "Pempek", "Ikan Bakar", "Sambal Oelek", "Lumpia"]
pakistani = ["Biryani", "Nihari", "Samosa", "Chapli Kebab", "Haleem", "Aloo Paratha", "Seekh Kebab", "Pakoras", "Karachi Biryani", "Aloo Keema", "Chana Chaat", "Saag", "Golgappa (Pani Puri)", "Malai Boti", "Karahi", "Nargisi Kofta", "Chapati", "Halwa Puri", "Paye", "Chapshurro"]
indian = ["Butter Chicken", "Biryani", "Masala Dosa", "Paneer Tikka", "Chole Bhature", "Samosa", "Tandoori Chicken", "Rogan Josh", "Gulab Jamun", "Aloo Paratha", "Vada Pav", "Palak Paneer", "Pani Puri", "Hyderabadi Biryani", "Dal Makhani", "Rajma Chawal", "Pav Bhaji", "Fish Curry", "Jalebi", "Chaat"]
bangladeshi = ["Rice and Fish Curry", "Biryani", "Panta Bhat", "Hilsha Fish", "Pitha", "Fuchka", "Bhapa Pitha", "Chingri Malai Curry", "Khichuri", "Bhuna Khichuri", "Bhorta", "Shingara", "Chomchom", "Mishti Doi", "Bakorkhani", "Chitol Maach", "Shorshe Ilish", "Mezban", "Bhorta", "Chingri Bhapa"]

dish = input("Enter the dish name: ")

if dish in italian:
    print(dish +' is Italian cuisine')
elif dish in french:
    print(dish +' is French cuisine')
elif dish in chinese:
    print(dish +' is Chinese cuisine')
elif dish in japanese:
    print(dish +' is Japanese cuisine')
elif dish in nepalese:
    print(dish +' is Nepalese cuisine')
elif dish in american:
    print(dish +' is American cuisine')
elif dish in thai:
    print(dish +' is Thai cuisine')
elif dish in german:
    print(dish +' is German cuisine')
elif dish in turkish:
    print(dish +' is Turkish cuisine')
elif dish in indonesian:
    print(dish +' is Indonesian cuisine')
elif dish in pakistani:
    print(dish +' is Pakistani cuisine')
elif dish in indian:
    print(dish +' is Indian cuisine')
elif dish in bangladeshi:
    print(dish +' is Bangladeshi cuisine')
else:
    print(dish+" is not in my knowledge, thanks.")