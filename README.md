# di_reader
Simple webscraper written in Python using the Django frameworw.

## Descriptiom
The app is made for reading articles on Di.se (Swedish newspaper) and will bypass the paywall. 
The app could easily be modified to work with any site you like with a little tweaking.

## Todo
- Di.se uses <picture> tags for responsive images and I have not yet figured out how to make BeautifulSoup extract the proper image for the article. If anyone has an idea, please email me on niklas@aldenaudio.se
- Add a form on the result page so you can choose another link and not have to go back to view another site.
- Change from POST to GET in the request, this will make the URL nicer.

## Libraries used
BeautifulSoup4
Requests

## Contact
aldenaudio.se