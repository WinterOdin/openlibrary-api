## Django book task
This is a recruitment task for NGLogic
There is schema and documentation available under
```
http://127.0.0.1:8000/api_schema/
```
### How to run it
create env and install dependencies
```
pip install -r req.txt
```
and then
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
### what is done?
 - Landing page as a form 
 - Forms are Django generated and submitted via ajax
 - Backend is mostly written in FBA's to make code reusable 
 - Pagination is done via JS, not Django paginator (for no reason)
 - bootstrap 5  and JQ (they were listed in the job posting)
 - form validation
 - saving to CSV
 - custom Django admin filter that lets you select a range 
 - API endpoint for authors and books (with schema) 
 - page doesn't reload
### things that don't work
 - collecting separate data about books, should I use threading or cellery?
 swagger is throwing template error TemplateDoesNotExist. I could do  'DIRS': [os.path.join(BASE_DIR,'templates')], 
but I wanted to keep templates separated from each other 
 