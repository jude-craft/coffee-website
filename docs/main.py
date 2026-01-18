from bs4 import BeautifulSoup
with open('docs/index.html', 'r') as file: 
    content = file.read()
    soup = BeautifulSoup(content, 'lxml')
    menu_items = soup.find_all('div', class_='menu-item')
    for menu in menu_items:
      coffee_name = menu.h3
      coffee_price = menu.p.strong

    print(coffee_name)
    print(coffee_price)
