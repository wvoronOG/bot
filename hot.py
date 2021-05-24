import sqlite3

with sqlite3.connect('bd/database.db') as hot:

    cursor = hot.cursor()
    query = """CREATE TABLE IF NOT EXISTS cookbd (ID,cook,dish,url)"""
    cursor.execute(query)
    chiken = """INSERT INTO cookbd ('ID','cook','dish','url') VALUES ('113','Рецепт курицы в сковороде','ингридиенты:1 кг курицы,200 грамм сметаны,3 больших луковицы,300 мл горячей воды,специи,соль,перец','видео готовки:https://www.youtube.com/watch?v=K48subsADYU')"""
    cursor.execute(chiken)
    chiken2 = """INSERT INTO cookbd ('ID','cook','dish','url') VALUES ('112','Рецепт курицы в духовке','ингридиенты:Куриная тушка,молотая паприка,Базилик,Оливковое масло,cоль и перец','https://www.youtube.com/watch?v=x0wVay7JGjY')"""
    cursor.execute(chiken2)
    soupc = """INSERT INTO cookbd ('ID','cook','dish','url') VALUES ('444','Рецепт куриного супа','Ингредиенты:Курица,Картофель - 500 г,Морковь - 160 г,Лук репчатый - 200 г,Чеснок - 3 зубчика,Масло растительное - 1 ст.л.,Масло сливочное - 30 г,Мука пшеничная - 150 г,Лавровый лист - 1 шт,Смесь сушеных овощей - 1 ст.л.,Куриные яйца - 2 шт,Вода  - 4 ст.л.,Свежая петрушка - 5 г,Зеленый лук - по вкусу,Куркума молотая - 1/2 ч.л.,Перец черный молотый - 1/2 ч.л.,Соль - 2,5 ч.л.','https://www.youtube.com/watch?v=V_Pni2Lx7bY')"""
    cursor.execute(soupc)
    soupb = """INSERT INTO cookbd ('ID','cook','dish','url') VALUES ('555','Рецепт борща','ингридиенты (на 2 л бульона):500 г Мясо на косточке,200 г свеклы,150 г капусты,110 г картофеля,100 г моркови,100 г лука,2 ст.л. томатного пюре,3 ч.л. уксуса 9%,3 ч.л. сахара,Чеснока,зелень,соль,перец болгарский','https://www.youtube.com/watch?v=ur_lfpcwjAY')"""
    cursor.execute(soupb)
    soupw = """INSERT INTO cookbd ('ID','cook','dish','url') VALUES ('888','рецепт Шурпы','Ингредиенты:говядина - 600гр.,горох нут - 80гр.,лук репчатый - 2шт.,лук белый - 1шт.,морковь - 3шт.,сладкий перец - 2шт.,помидор - 3шт.,картофель - 6 - 7шт.,чеснок - 5 зубков,масло топленое - 1.5ст.л.,кориандр - 0.5,ч.л.,кумин - 0.5 ч.л.,соль по вкусу,кипяток - 1.5 - 2л.','https://www.youtube.com/watch?v=7VpKhhr38V8')"""
    cursor.execute(soupw)
    wawlik = """INSERT INTO cookbd ('ID','cook','dish','url') VALUES ('999','рецепт шашлыка из свинины','Свинина 1кг,Приправа к шашлыку 15гр,Лук – 1-2шт,Растительное масло 1ст.л,Соль','https://www.youtube.com/watch?v=IxdOYS7A9OU')"""
    cursor.execute(wawlik)
    salat1 = """INSERT INTO cookbd ('ID','cook','dish','url') VALUES ('931','рецепт горячего салата:','400 г говядина,200 г огурцы,1 морковь,1 лук репчатый,250 г перец сладкий,2 ст.л кинзы,2-3 зубчика чеснока,1 ч.л сахар,1 ст.л рисовый уксус или 1 ч.л яблочный или любой,4 ст.л соевый соус,3 ст.л рстительное масло + 1 ст.л кунжутного,1 ст.л кунжут,красный перец по вкусу ','https://www.youtube.com/watch?v=lc-39kH7p4Q')"""
    cursor.execute(salat1)
    salat2 = """INSERT INTO cookbd ('ID','cook','dish','url') VALUES ('47','рецепт холодного салата:','400 г говядина,200 г огурцы,1 морковь,1 лук репчатый,250 г перец сладкий,2 ст.л кинзы,2-3 зубчика чеснока,1 ч.л сахар,1 ст.л рисовый уксус или 1 ч.л яблочный или любой,4 ст.л соевый соус,3 ст.л рстительное масло + 1 ст.л кунжутного,1 ст.л кунжут,красный перец по вкусу ','https://www.youtube.com/watch?v=bDD6I5M_EdE')"""
    cursor.execute(salat2)
    svinyadux = """INSERT INTO cookbd ('ID','cook','dish','url') VALUES ('15','рецепт свинины в духовке:','1,2 кг гудинки,2/3 ст.л соли,1 сn.л паприка,1 ч.л черный перец,1 ч.л кориандр,2 сn.л острый кетчуп или аджика + 1 ч/л меда +т1/2 ч/л паприка,Запекать 180С (360Ф) 40 мин + 20 мин с глазурью ','https://www.youtube.com/watch?v=Fl6M52kCyMs')"""
    cursor.execute(svinyadux)
    ggv = """INSERT INTO cookbd ('ID','cook','dish','url') VALUES ('59','рецепт говядины на сковороде:','Ингредиенты:Мякоть говядины - 1 кг,Лук репчатый - 150 г,Морковь - 150 г,Чеснок - 4 зубчика,Томатная паста - 2 ст.л.,Сливочное масло - 40 г,Растительное масло - 2 ст.л.,Мука пшеничная - 2 ст.л.,Соль - 1 ч.л.,Перец черный молотый - ½ ч.л.,Паприка сладкая - 1 ч.л.,Кориандр молотый - 1 ч.л.,Вода кипяток - 800 мл,Петрушка -  10 г,Зеленый лук - 10 г ','https://www.youtube.com/watch?v=3itytdo2dDk')"""
    cursor.execute(ggv)
    ggd = """INSERT INTO cookbd ('ID','cook','dish','url') VALUES ('228','рецепт говядины в духове:','говядина 3кг,оливовое масло 30мл,соль 10гр,черный перец 10гр','https://www.youtube.com/watch?v=b4yLP2ge4V4')"""
    cursor.execute(ggd)
    a = cursor.execute(f"SELECT cook , dish , url FROM cookbd WHERE ID = '{113}'").fetchone()
    b = cursor.execute(f"SELECT cook , dish , url FROM cookbd WHERE ID = '{112}'").fetchone()
    c = cursor.execute(f"SELECT cook , dish , url FROM cookbd WHERE ID = '{444}'").fetchone()
    d = cursor.execute(f"SELECT cook , dish , url FROM cookbd WHERE ID = '{555}'").fetchone()
    e = cursor.execute(f"SELECT cook , dish , url FROM cookbd WHERE ID = '{888}'").fetchone()
    h = cursor.execute(f"SELECT cook , dish , url FROM cookbd WHERE ID = '{999}'").fetchone()
    y = cursor.execute(f"SELECT cook , dish , url FROM cookbd WHERE ID = '{931}'").fetchone()
    p = cursor.execute(f"SELECT cook , dish , url FROM cookbd WHERE ID = '{47}'").fetchone()
    z = cursor.execute(f"SELECT cook , dish , url FROM cookbd WHERE ID = '{15}'").fetchone()
    l = cursor.execute(f"SELECT cook , dish , url FROM cookbd WHERE ID = '{59}'").fetchone()
    o = cursor.execute(f"SELECT cook , dish , url FROM cookbd WHERE ID = '{228}'").fetchone()