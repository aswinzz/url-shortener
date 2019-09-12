## URL SHORTENER

### How to setup
- Clone this repo and open the directory in your terminal
- `virtualenv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py runserver`
- visit `localhost:8000` in your browser

### Screenshots
<p align="center"> 
<img src="https://github.com/aswinzz/url-shortner/blob/master/ss.png" />
</p>

### How it works
- URL shortning has been done by taking the hash of the url provided and saving it in the database along with the url, inorder to retrieve back the url from the shortened url. since hash is long i have taken the first 7 characters of the hash. To tackle the problem that two same url's will have the same shortened url, i have used unique id which is concatenated with the url and then hashed which will always give you an unique shortened url.
- Whenever a shortened URL is opened the count is also noted for analytics and it can be observed in the homepage which lists all the counts of shortened url's uptill date.

### Contributing
Your contributions are always welcome! Feel free to open up issues and create Pull Request if you feel like adding more features to this project. 🎉

Template for the UI has been taken from [Ava](https://onepagelove.com/ava)