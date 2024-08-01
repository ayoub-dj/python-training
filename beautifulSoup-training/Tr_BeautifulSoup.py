import requests
from bs4 import BeautifulSoup, SoupStrainer, Comment
import re

with open('content.txt', 'w') as f: 
    soup = BeautifulSoup('<b> Hello World </b>', 'lxml')
    # GET ALL attributes and methods
    # for i in dir(soup): f.writelines(f"{i}\n")

    # tag = soup.html
    # tag.name = "h2" # To change the tag

    # soup = BeautifulSoup('<input type="text" name="name" value="James">', 'lxml')
    # get_input = soup.input # To access an element
    # get_attr = get_input.attrs # To access it's Attributes
    # get_attr['value'] = 'Dexter' # To update Attribute value
    # del get_attr['name'] # To remove it
    # get_attr['id'] = 'input-field' # To add new one

    # htmlTags = "<div class='content'><!--This is a comment text in HTML--><p>Hello world</p></div>"

    # soup = BeautifulSoup(htmlTags, "lxml")
    # # get_text = str(soup.string) # You can use string methods
    # get_text = soup.find('p').string.replace('Hello', 'Welcome to').upper()
    # get_tags_with_formatting = soup.find('div').prettify() # Use prettify to get good formatting

    with open('index.html', 'r') as indexHTML:
        soup = BeautifulSoup(indexHTML, 'lxml')
        # Get Elements by tag and Attributes
        # --------------------------------------------
        # get_lis = soup.body.ul # Access element by name
        # find_all_hrefs = soup.find_all('a') # Get all Elements
        # find_the_first = soup.find(id='nm') # Get the first element
        # select_all_elements = soup.select('a.prog') # Select all elements
        # select_the_first = soup.select_one('.prog') # # Select the first element
        # find_all_elements = soup.find_all(attrs={"class": 'prog'}) # find all elements by class name
        # find_the_first = soup.find(attrs={"class": 'prog'}) # Get the first element by class name
        # find_all_by_type = soup.find_all(attrs={'type': 'text'})
        # select_all_by_type = soup.select('[type]')
        # select_one_by_type = soup.select_one('[type="text"]')

        # Searching the Tree
        # --------------------------------------------
        # form_children = list(soup.body.form.children) # Get all children from the Form
        # form_descendants = soup.body.form.descendants # descendants attribute returns a generator,
        # form_parent = soup.head.title.parent # Get The parent of element
        # tag_name = soup.head.title.name # Get the tag name of element

        # next_siblings = soup.find(attrs={"class": "title"}).next_siblings # Get all next siblings
        # next_sibling = soup.b.next_sibling # Get the next sibling (C)
        # previous_siblings = soup.find(attrs={"class": "tutorial"}).previous_siblings # Get all previous siblings
        # previous_sibling = soup.i.previous_sibling # Get The previous siblings (C)

        # next_elements = soup.b.next_elements # Get all next Elements (Include Text)
        # previous_elements = soup.u.previous_elements # Get all previous siblings
        # next_element = soup.find('a', id='link2').next_element # Get the next Element (Include Text)
        # previous_element = soup.find('a', id='link1').previous_element # Get the next Element (Include Text)



        # Modifying the Tree
        # --------------------------------------------
        # title_element = soup.find(attrs={"class": 'title'})
        # new_tag, new_string = soup.new_tag('i'), soup.new_string('World')
        # new_tag.append(new_string)
        # title_element.append(new_tag)

        # values = ['Home ', 'Contact us ', 'About us ']
        # title_element.extend(values)

        # get_links = soup.find(attrs={"class": 'links'})
        # for value in values:
        #     link = soup.new_tag('li')
        #     link.append(value)
        #     get_links.append(link)

        # title_element.insert(0, 'Welcome to World and ')
        # title_element.b.insert_after(' James')
        # title_element.b.insert_before('James, ')

        # get_html = soup.html
        # get_html.clear() # Clear all elements and text
        # extract_all = get_html.body.extract() # Extract all elements
        # remove_first_link = get_links.find_next().decompose() # Remove link from links

        # get_heading = soup.h2
        # # get_heading.string.replace_with('New Heading') # Replace value with text
        # obj1 = BeautifulSoup('<div class="text">New Text</div>', features="lxml")
        # # get_heading.string.replace_with(obj1) # Replace value with element
        # get_heading.string.wrap(soup.new_tag('i')) # Wrap Used to put the text of element into tag
        # get_heading.i.unwrap() # Wrap Used to remove the text from specified tag

        #  Parsing a Section of a Document
        #  --------------------------------------------
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        #     'Content-Type': 'application/json'
        # }
        # url = "https://sale.alibaba.com/category/theme/index.html?spm=a27aq.cp_6.8566172370.2.697d2a9a0unN2U&wx_navbar_transparent=true&path=/category/theme/index.html&ncms_spm=a27aq.27059075&cardType=101002650&cardId=101002650_6_kitchen_applianc&topOfferIds=1601011969944&categoryIds=6&tracelog=fy23_all_categories_home_lp"
        # r = requests.get(url, headers=headers)
        # get_part_of_doc = SoupStrainer(attrs={"class": "waterfall-column"}) # To parse a section from the a html documents
        # soup = BeautifulSoup(r.content, 'lxml', parse_only=get_part_of_doc)
        # trending_products = soup.select('a')

        # Find all Children of an Element
        # --------------------------------------------
        # get_ul_children = soup.ul.children  
        # get_ul_children = soup.ul.findChildren('li') # Find the children inside the ul (You can use selectors)


        # Find Elements by ID and Class and Attribute and Filtering
        # --------------------------------------------
        # get_elem = soup.find(id='nm')
        # get_elem_ = soup.find_all(id='nm')
        # get_elem_ = soup.select('#nm')
        # get_elem_ = soup.select_one('#nm')
        # get_elem_ = soup.select_one('#nm')
        # get_elem_ = soup.select_one('.elem')
        # get_elem_ = soup.find_all(attrs={"class": 'elem'})
        # get_elem_ = soup.find_all(attrs={"type":'email'})
        # get_elem = soup.select('[type]')
        # get_elem = soup.select('[name="text"]')
        # get_elem = soup.select('input:first-child')
        # get_elem = soup.select('input:nth-child(even)')
        # get_elem = soup.select('input:nth-child(odd)')

        # def iscomment(elem): return isinstance(elem, Comment) 
        # comments = soup.find_all(string=iscomment) # Get all comments


        # def start_with_A(c): return c.startswith('A') or c.startswith('a')
        # get_ul_dept = soup.find("ul", id="dept")
        # get_li_starts_with_A = get_ul_dept.find_all('li', string=start_with_A)

        # tags = soup.find_all('a')
        # all_p = [tag.contents for tag in tags if tag.name == 'li'] # get all lis tags and print their contents 
        # all_id_att = [tag for tag in tags if tag.has_attr('id')]
        # get_emails = [tag for tag in tags if tag.has_attr('href') and '@' in tag['href']]
        # get_text = soup.get_text() # To get the text only
        # tags = soup.find_all()
        # for tag in tags:
        #     if tag.has_attr('style'): del tag.attrs['style']
