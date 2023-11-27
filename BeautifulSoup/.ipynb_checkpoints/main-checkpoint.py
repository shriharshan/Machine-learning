from bs4 import BeautifulSoup
with open('Home.html','r') as html_file:
    content = html_file.read()
    #print(content)

    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())

    #course_html_tags = soup.find_all('h5')
    #print(tags)
    #for course in course_html_tags:
     #   print(course.text)

    Course_cards = soup.find_all('div',class_='card')
    for course in Course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1] # for printing only the price

        #print(course_name)
        #print(course_price)
        print(f'{course_name} costs: {course_price}')